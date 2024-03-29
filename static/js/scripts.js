$(document).ready(function(){


  var participant_list = []

  $("#input_form").submit(function(event){
    event.preventDefault();
    $("#error_message").text("")
    var $name = $("#participant_name").val().trim().toLowerCase()
    participant_list.push(cleanName($name))
    participant_list = removeDupes(participant_list)
    participantCounter(participant_list)
    $("#participant_name").val("")
    $("#generate_groups").removeAttr("disabled")
  })


  $("#generate_groups").click(function(event){
    event.preventDefault();
    submitList(JSON.stringify(participant_list), $("#number_per_group").val())
  })


//Functions

function cleanName(name){
  return name.substr(0,1).toUpperCase()+name.substr(1)
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


function participantCounter(list){
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
    }
    $("#results").append($result)
  }
}


})
