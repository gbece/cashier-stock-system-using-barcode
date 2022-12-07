<?php

$csv = array_map('str_getcsv', file('config.csv'));
$flag = False;
foreach($csv as $line){

	echo "
<!DOCTYPE html>
<html>
<body>

<form action='/actualizar_config.php' method='post'>
  <h2> Configuraci&oacuten de la base de datos</h2><hr><br>
  <h3>
  Host: <input type='text' name='host' value=" . $line[0] . "><br>
  User: <input type='text' name='user' value=" . $line[1] . "><br>
  Password: <input type='text' name='password' value=" . $line[2] . "><br>
  Database: <input type='text' name='database' value=" . $line[3] . "><br>
  Port: <input type='text' name='port' value=" . $line[4] . "><br>
  <br>
  </h3>

 <input type='submit' value='Actualizar'>
</form>

</body>
</html>
";
	   
}

?>
