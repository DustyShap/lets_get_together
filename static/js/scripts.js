$(document).ready(function(){


  var temp_participant_list = []
  var participant_list = []

  $("#input_form").submit(function(event){
    event.preventDefault();
    $name = $("#participant_name").val().trim()
    temp_participant_list.push(cleanName($name))
    participant_list = removeDupes(temp_participant_list)
    var $running_total = participant_list.length
    $("#generate_groups").removeAttr("disabled")
    $("#participant_name").val("")
    $("#total_participants").html("Entered Names: " + $running_total);
    if($("#"+$running_total).length == 0){
      $("#number_per_group").append("<option id=" +$running_total +
        " value="+ $running_total + ">" + $running_total + "</option>");
    } else {
      $("#error_message").text('Duplicate!')
      setTimeout(function(){$("#error_message").text('')}, 400)
    }

  })

  $("#generate_groups").click(function(event){
    event.preventDefault();
    submitList(JSON.stringify(participant_list),$("#number_per_group").val())
  })


  function submitList(list,number){
        $("#results").empty()
        $.ajax({
          data:{
            list_of_names: list,
            number_per_group: number
          },
          type:"POST",
          url:'/generate_groups'
        })
        .done(function(data){
          $("#generate_groups").text('Regenerate Groups')
          displayGroups(data)
        })
  }


  $("#file_input_button").click(function(){
    var myFile = document.getElementById("fileinput").files[0];
    var reader = new FileReader();
    reader.readAsText(myFile);
    reader.onload = function(e) {
      var uploaded_list = reader.result.split("\n").join(",")
      var temp_list = []
      var temp = new Array();
      temp = uploaded_list.split(",");
      temp.pop()
      for (var i=0; i < temp.length; i++){
        temp_list.push(cleanName(temp[i]))
      }
      temp_participant_list = removeDupes(temp_list)
      submitList(JSON.stringify(temp_participant_list),$("#group_number").val())
    }
  })


  function removeDupes(names) {
    let unique = {};
    names.forEach(function(i) {
      if(!unique[i]) {
        unique[i] = true;
      }
    });
    return Object.keys(unique);
  }

  function cleanName(name){
    return name.toLowerCase().substr(0,1).toUpperCase()+name.substr(1)
  }

  function displayGroups(data){
    for (var i=0; i < data.length; i++){
      var group_count = i+1
      var groups = data[i];
      var $result = $("<div class='result'><b>Group " + group_count + ":</b></div>");
      for (var j=0; j < groups.length; j++){
        $result.append("<span>"+groups[j]+"</span>")
      }
      $("#results").append($result)
    }
  }
})
