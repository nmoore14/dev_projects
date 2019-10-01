<?php 
/*
* Author: Nick Moore
* Date: 9-4-2019
* Admin page for Hurricane Cycles
*/
?>

<?php 
  session_start();
  include('scripts_admin/user_validate.php');

  $isLoggedIn = false;

  if(isset($_POST['submit'])) {
    checkLogin();
  }

  function checkLogin() {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $isLoggedIn = verify_user($username, $password);

    if($isLoggedIn){
      header('Location: http://localhost/dev_project/hurricane_cycles/web/hurricane_web_v1/admin/dashboard.php');
      exit;
    }
  };
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <!-- CSS Links -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
		<link rel="stylesheet" href="./css_admin/main.css">

			<!-- FONTS -->
		<link href="https://fonts.googleapis.com/css?family=Bangers&display=swap" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,600&display=swap" rel="stylesheet">


    <!-- JS Links -->
		<script src="https://kit.fontawesome.com/be0ebd7a0a.js"></script>
    <title>Hurricane Cycles | Admin</title>

  </head>
  <body>
    <div class="container-fluid adminContainer">
      <div class="row">
        <div class="col-12 col-md-4 empty"></div>
        <div class="col-12 col-md-4">
          <h2 class="display-4 text-center">Welcome</h2>
          <form method="POST" action="#" id="login_form" class="loginForm">
            <div class="form-group">
              <input type="text" name="username" id="admin_username_input" class="form-control" placeholder="Username">
              <input type="password" name="password" id="admin_password_input" class="form-control" placeholder="Password">
            </div>
            <div class="text-center">
              <button type="submit" class="btn btnLogin center-block hidden" id="login_button" name="submit">Login</button>
            </div>
          </form>
        </div>
        <div class="col-12 col-md-4 empty">
          <a href="./scripts_admin/base_create_user.php">Generate User</a>
        </div>
      </div>
    </div>
    
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.js" crossorigin="anonymous"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
			integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
		<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
      integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script src="./js_admin/main.js"></script>
  </body>
</html>