<?php
  /**
   * Validate users to login and CRUD for the user database
   * Created by: Nick Moore
   * September 30, 2019
   */

  // Pulling in the MySQL connection credientials
  $database = include('config/mysql_config.php');

  $host = $database['host'];
  $db = $database['db'];
  $user = $database['user'];
  $pass = $database['pass'];

  function verify_user($username, $password) {
    $connection = "mysql:host=$host;db=$pass";

    try {
      $pdo = new PDO($connection, $user, $pass);
      $sql = $pdo->prepare('SELECT * username FROM admin_users WHERE username = :username AND password = :password');
      $sql->execute(["username" => $username, "password" => $password]);
      $data = $sql->fetchAll();

      if(count($data) > 0) {
        return true;
      } else {
        return false;
      }

    } catch (\PDOException $e) {
      throw new \PDOException($e->getMessage(), (int)$e->getCode());
    }
  }
?>