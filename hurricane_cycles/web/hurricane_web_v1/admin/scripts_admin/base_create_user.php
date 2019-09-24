<?php
/**
 * PHP Scripts for generating users without using the admin dashboard
 * Created by: Nick Moore
 * Date: Sept. 24, 2019
 */
?>

<?php
	$newPassword = $_GET['newPassword'];

	if($newPassword) {
		$hashedPassword = password_hash($newPassword, PASSWORD_DEFAULT);
	}
?>

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title>Create a User | No Dashboard</title>
	</head>
	<body>
		<form class="form" action="#" method="get">
			<input type="text" name="newPassword" id="new_password" placeholder="Enter password">
			<input type="submit" value="Generate">
		</form>
		<?php
			echo('<h1>Hashed Password: </h1><p>' . $hashedPassword . '</p>');
		?>
	</body>
</html>