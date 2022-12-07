<?PHP

$file_handle = fopen("estado.txt", "rb");
$line_of_text = fgets($file_handle);
$parts = explode('=', $line_of_text);

if ($parts[0] ==0){
	$estado = "<font color = \"red\">DESACTIVADO</font>";
	$texto = "Para activar el sistema haga click en el siguiente link: <a href =\"activar.php\" target=\"derecha\"> Activar</a>"; 
} else{		
	$estado = "<font color = \"green\">ACTIVADO</font>";
	$texto = "Para desactivar el sistema haga click en el siguiente link: <a href =\"desactivar.php\" target=\"derecha\"> Desactivar</a>";
		
}
fclose($file_handle);

echo "<h2> Estado del sistema</h2><hr><br>";
echo "El estado del sistema es: <b>". $estado . "</b><br>";
echo $texto . "<br>";
?>
