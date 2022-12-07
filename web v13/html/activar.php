<?php
$fichero = 'estado.txt';
// Abre el fichero para obtener el contenido existente
$actual = file_get_contents($fichero);
$actual = "1";
// Escribe el contenido al fichero
file_put_contents($fichero, $actual);

echo "<font color = \"green\"><h2> El sistema se ha ACTIVADO</h2><hr><br></font>";
?>
