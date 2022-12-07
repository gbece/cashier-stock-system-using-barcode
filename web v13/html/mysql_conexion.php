<?php
$csv = array();
if(($handle = fopen("config.csv", "r")) !== FALSE)
{
	while(($data = fgetcsv($handle, 1000, ",")) !== FALSE)
	{
		$csv[] = $data;
	}
}

fclose($handle);

$servername = $csv[0][0];
$username = $csv[0][1];
$password = $csv[0][2];
$dbname = $csv[0][3];
$port = $csv[0][4];
// Crea la conexion
 $conn = new mysqli($servername . ":" . $port, $username, $password, $dbname);

 //Verifica la conexion
 if ($conn->connect_error) {
     die("Error de conexion con la base de datos: " . $conn->connect_error);
     } 
    // echo "Conexion con exito";  //para debuggear si es exitosa



?>
