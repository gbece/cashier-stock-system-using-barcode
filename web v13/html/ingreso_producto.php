<?php

$codigo = $_POST["codigo"];
$descripcion = $_POST["descripcion"];
$precio = $_POST["precio"]; 
$unidades = $_POST["unidades"]; 
$umbral = $_POST["umbral"];

	

include 'mysql_conexion.php'; //se inlcuye libria de configuracion del servidor

$sql = "INSERT INTO productos (codigo, descripcion, precio, cantidad, umbral)
	VALUES ('$codigo', '$descripcion', '$precio', '$unidades', '$umbral')";

if (mysqli_query($conn, $sql)) {
	    echo "Nuevo producto ingresado correctamente.";
	    } else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

mysqli_close($conn);
?>

