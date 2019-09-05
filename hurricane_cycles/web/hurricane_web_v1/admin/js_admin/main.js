$(document).ready(function () {
  /**
   * Globals
   */
  
  var loginButton = $("#login_button");

  var display_login_button = function () {
    if ($("#admin_username_input").val().length > 0 && $("#admin_password_input").val().length > 0) {
      loginButton.removeClass('hidden');
    } else {
      loginButton.addClass('hidden');
    }
  }

  $("#admin_username_input").keyup(function (e) {
    display_login_button();
  });

  $("#admin_password_input").keyup(function (e) { 
    display_login_button();
  });
});