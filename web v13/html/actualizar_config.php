<?php
$list = $_POST["host"].",".$_POST["user"].",".$_POST["password"].",".$_POST["database"].",".$_POST["port"];

$file = fopen("config.csv","w");
fputs($file,$list);
fclose($file);


echo "
<h2> Se actualiz&oacute la configuraci&oacuten</h2><hr><br>
  <h3>
  Host: " .  $_POST["host"] . "<br>
  User: " . $_POST["user"] . "<br>
  Password: " . $_POST["password"] . "<br>
  Database: " . $_POST["database"] . "<br>
  Port: " . $_POST["port"] . "<br>
  <br>
  </h3>

";

?>
