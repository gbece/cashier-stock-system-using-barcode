<?php


$csv = array_map('str_getcsv', file('config.csv'));
$flag = False;
foreach($csv as $line){
	$host = $line[0];
	$user = $line[1];
	$password = $line[2];
	$database = $line[3];
	$port = $line[4];
}

$target_dir = "database/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));


// Se verifica el tama√o del archivoe
if ($_FILES["fileToUpload"]["size"] > 500000) {
	echo "No se puede subir el archivo, es muy grande.";
	$uploadOk = 0;
}
// Se descartan archivos que no sean SQL
if($imageFileType != "sql") {
	echo "Solamente archivos con extensi&oacuten sql son permitidos.";
	$uploadOk = 0;
}
// Se verifica si  $uploadOk es seteado  en 0 debido a alg√∫n error
if ($uploadOk == 0) {
	echo "No se pudo subri el archivo.<br>";
	// si todo esta ok, se intenta subir el archivo
} else {
	if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
	
		//comando SQL a ejecutar
		$command = "mysql -u$user -p$password  $database  < $target_file";

		// se ejecuta en consola del sistema el comando SQL
		system($command);

		echo "El archivo ". basename( $_FILES["fileToUpload"]["name"]). " fue subido exitosamente.";


	} else {
		echo "Sucedi&oacute un error al subir el archivo..";
	}
}

?>
