<!DOCTYPE html>
<html>


<head>
<!-- 	<meta http-equiv="refresh" content="1" > -->
</head>


<body>


<?php
$secondsWait = 1;

header("Refresh:$secondsWait");

$csv = array();
$fecha = date("Y-m-d"); // estos datos deberian ser provisto por el archivo
$hora = date("h:m:s");  
 
if(($handle = fopen("codME.csv", "r")) !== FALSE)
{


	while(($data = fgetcsv($handle, 1000, ",")) !== FALSE)
	{
		$csv[] = $data;

	}	
	echo "<h2>" . $csv[0][1] ." " . $csv[0][2] .  "</h2><br>";
	if ($csv[0][0] == "2"){
		header("Location: actualizar_producto.php" );

	}	
}

fclose($handle);
?>


</body>
</html>
