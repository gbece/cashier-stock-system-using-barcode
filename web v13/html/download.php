<?php
$dbhost = 'localhost';
$port = '3306';
$dbuser = 'root';
$dbpass = 'service';
$database_path = "./database/";
$dbname = "stock";
$backup_file = $database_path.$dbname . '.sql';

//comando SQL a ejecutar
$command = "mysqldump -h$dbhost -u$dbuser -p$dbpass -P$port"." stock  > $backup_file";

// se ejecuta en consola del sistema el comando SQL
system($command);

// lo siguiente forza a descargar el archivo .sql
header("Content-disposition: attachment; filename=" . $dbname . ".sql");
header("Content-type: application/sql");
readfile($backup_file);
echo("El archivo de base de datos se descargar&aacute autom&aacuteticamente en unos segundos...");

?>
