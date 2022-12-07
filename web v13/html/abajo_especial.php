<?php
include 'mysql_conexion.php'; //se inlcuye libria de configuracion del servidor

$secondsWait = 1;
header("Refresh:$secondsWait");

$result = mysqli_query($conn,"SELECT * FROM errorlog");
$counter = 0;
$numResults = mysqli_num_rows($result);

while ($row = mysqli_fetch_array($result)){
	if (++$counter == $numResults) {
		 echo $row['descripcion'];
			 
	 }
}

?>
