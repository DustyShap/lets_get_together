$(document).ready(function(){


  var temp_participant_list = []
  var participant_list = []

  $("#input_form").submit(function(event){
    event.preventDefault();
    $("#error_message").text("")
    temp_participant_list.push(cleanName($("#participant_name").val().trim()))
    participant_list = removeDupes(temp_participant_list)
    runningTotal(participant_list)
    $("#participant_name").val("")
    $("#generate_groups").removeAttr("disabled")
  })

  $("#generate_groups").click(function(event){
    event.preventDefault();
    submitList(JSON.stringify(participant_list), $("#number_per_group").val())
  })

  $("#delete_user").click(function(event){
    event.preventDefault();
    var $user_to_delete = $("#user_to_delete").val();
    if ($user_to_delete){
      deleteUser($user_to_delete)
      $("#total_participants").html("Entered Names: " + participant_list.length);
    }
  })


  function deleteUser(name){
    var index = participant_list.indexOf(name);
    var index2 = temp_participant_list.indexOf(name);
    $("#"+participant_list.length).remove();
    participant_list.splice( index, 1 );
    temp_participant_list.splice( index, 1);
    $("#user_to_delete option[value="+name+"]").remove();
    submitList(JSON.stringify(participant_list), $("#number_per_group").val())
  }


  function cleanName(name){
    return name.toLowerCase().substr(0,1).toUpperCase()+name.substr(1)
  }


  function removeDupes(list) {
    let unique = {};
    list.forEach(function(i) {
      if(!unique[i]) {
        unique[i] = true;
      }
    });
    return Object.keys(unique);
  }


  function runningTotal(list){
    var total = list.length;
    $("#total_participants").html("Entered Names: " + total);
    if($("#"+total).length == 0){
      $("#number_per_group").append("<option id=" + total +
        " value="+ total + ">" + total + "</option>");
    } else {
      $("#error_message").text("Duplicate!")
      setTimeout(function(){$("#error_message").text("")}, 1000)
    }
  }


  function submitList(list,number){
      $("#user_to_delete").empty()
      $("#results").empty()
      $.ajax({
        data:{
          list_of_names: list,
          number_per_group: number
        },
        type:"POST",
        url:"/generate_groups"
      })
      .done(function(data){
        $("#generate_groups").text('Regenerate Groups')
        displayGroups(data)
      })
  }


  function displayGroups(data){
    for (var i=0; i < data.length; i++){

      var group_count = i+1
      var groups = data[i];
      var $result = $("<div class='result'><b>Group " + group_count + ":</b></div>");
      for (var j=0; j < groups.length; j++){
        $result.append("<span>"+groups[j]+"</span>")
        $("#user_to_delete").append("<option value=" + groups[j] + ">" + groups[j] + "</option>")
      }
      $("#results").append($result)
    }
  }


})
