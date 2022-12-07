<?php
$fichero = 'estado.txt';
// Abre el fichero para obtener el contenido existente
$actual = file_get_contents($fichero);
$actual = "0";
// Escribe el contenido al fichero
file_put_contents($fichero, $actual);

echo "<font color = \"red\"><h2> El sistema se ha DESACTIVADO</h2><hr><br></font>";
?>
