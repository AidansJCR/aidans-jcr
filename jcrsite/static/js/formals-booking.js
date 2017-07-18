jQuery(document).ready(function() {
  const BASE_URL = window.origin
  const ADD_GROUP_PATH = '/formals-booking/api/add_group'

  var groupEditorUpdate = function() {

    // clear the field
      $('#group-settings').empty();
    // get values of radio buttons
    console.log("Shall create new group");
    var shallCreateNewGroup = $('#new-group-id-btn').prop('checked');
    if(shallCreateNewGroup) {
      // clear the extra group info
      var spacer = $('<td></td>');
      var content = $('<td></td>');

      // create a button with a function that makes an AJAX request to the server

      var newGroupButton = $('<input></input>', {
        type: 'button',
        class: 'btn',
        value: 'Generate new group',
        click: function() {
          renderNewGroup()
        }
      });
      console.log(newGroupButton)
      // create a field that is filled in with javascript
      var groupIDField = $('<input></input>', {
        type: 'text',
        disabled: 'disabled',
        name: 'group_id',
        id: 'group-id-field',
        class: ''
      });
      console.log(groupIDField);
      content.append(newGroupButton);
      content.append(groupIDField);
      $('#group-settings').append(spacer);
      $('#group-settings').append(content);
    }



  }

  var renderNewGroup = function() {
    console.log("Call to render group")
    $.get(BASE_URL + ADD_GROUP_PATH).then(function(resp) {
        if(resp.err) {
          alert("Something went wrong :(");
        }
        else {
          $('#group-id-field').val(resp.group_id);
        }
    });
  }

  // on ready, update the group editor
  groupEditorUpdate();

  $('input[type=radio]').click(groupEditorUpdate);

});
