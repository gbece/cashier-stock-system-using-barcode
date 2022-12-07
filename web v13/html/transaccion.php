<?php


$desde =$_POST["desde"];
$hasta =$_POST["hasta"];



include 'mysql_conexion.php'; //se inlcuye libria de configuracion del servidor

echo "<h2> Lista de transacciones entre las fechas $desde y $hasta </h2><hr><br>";
echo "<html><head>
	<style>
	table, th,td{font-family: Arial; font-size: 15pt;}
	</style>
	</head><body><table>\n\n";

echo "<table border='1'>
	<tr>
	<th>id_transacc</th>
	<th>Fecha</th>
	<th>Codigo</th>
	<th>Descripcion</th>
	<th>Precio</th>
	</tr>";

//$result = mysqli_query($conn,"SELECT * FROM transacclog LEFT JOIN productos ON transacclog.id_producto=productos.id_producto WHERE transacclog.datetime =>  $desde  00:00:00 AND datetime =<  $hasta 23:59:59");


$result = mysqli_query($conn,"SELECT * FROM transacclog LEFT JOIN productos ON transacclog.id_producto=productos.id_producto WHERE transacclog.datetime BETWEEN '$desde 00:00:00' AND  '$hasta 23:59:59'");



while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['id_transacc'] . "</td>";
echo "<td>" . $row['datetime'] . "</td>";
echo "<td>" . $row['codigo'] . "</td>";
echo "<td>" . $row['descripcion'] . "</td>";
echo "<td>" . $row['precio'] . "</td>";
echo "</tr>";
}
echo "</table>";


?> 

