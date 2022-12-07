<?php

include 'mysql_conexion.php'; //se inlcuye libria de configuracion del servidor

echo "<h2> Lista de productos en el stock</h2><hr><br>";
echo "<html><head>
	<style>
	table, th,td{font-family: Arial; font-size: 15pt;}
	</style>
	</head><body><table>\n\n";

echo "<table border='1'>
	<tr>
	<th>id</th>
	<th>Codigo</th>
	<th>Descripcion</th>
	<th>Precio</th>
	<th>Cantidad</th>
	<th>Umbral</th>
	</tr>";

$result = mysqli_query($conn,"SELECT * FROM productos");
while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['id_producto'] . "</td>";
echo "<td>" . $row['codigo'] . "</td>";
echo "<td>" . $row['descripcion'] . "</td>";
echo "<td>" . $row['precio'] . "</td>";
echo "<td>" . $row['cantidad'] . "</td>";
echo "<td>" . $row['umbral'] . "</td>";
echo "</tr>";
}
echo "</table>";


?> 

