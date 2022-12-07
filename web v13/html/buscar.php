<!DOCTYPE html>
<html>


<head>
	<meta http-equiv="refresh" content="1" >
</head>


<body>


<?php
$csv = array();
$fecha = date("Y-m-d"); // estos datos deberian ser provisto por el archivo
$hora = date("h:m:s");  
 
if(($handle = fopen("TempTransaccion.csv", "r")) !== FALSE)
{


	echo "-----------------------------------------------------------------------------------------------------------------------------<br>";
	echo "<h2> Establecimiento ORT</h2>";
	echo "<h3>FECHA:  " .$fecha ." --- Hora: " . $hora . "<h3>";
	echo "<html><head>
		<style>
		table, th,td{font-family: Arial; font-size: 15pt;}
		</style>
		</head><body><table>\n\n";

	echo "<table border='1'>
		<tr>
		<th>Nro transaccion</th>
		<th>Codigo de barras</th>
		<th>Descripcion</th>
		<th>Precio por unidad</th>
		<th>Total acumulado</th>
		</tr>";


	while(($data = fgetcsv($handle, 1000, ",")) !== FALSE)
	{
		$csv[] = $data;

		echo "<tr>";
		foreach ($data as $cell) {
			echo "<td>" . htmlspecialchars($cell) . "</td>";
		}
		echo "</tr>\n";
	}
}

fclose($handle);
?>



</body>
</html>
