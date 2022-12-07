<?php

$csv = array_map('str_getcsv', file('TempTransaccion.csv'));
$flag = False;
foreach($csv as $line){
    if($line[1] == $_POST["name"]){
	    //do what ever you wan
	    $flag = True;
	    echo "<h2> Se encontro el producto</h2><hr><br>";
	    echo "ID: " . $line[0] ."<br>" ;
	    echo "Codigo de Barras: " . $line[1] ."<br>";
	    echo "Producto: " . $line[2] ."<br>";
	    echo "Precio:" . $line[3] ."<br>";
	    echo "Cantidad: " . $line[4] ."<br>";
    }
}
if ($flag == False){
	     echo "<h2> No se encontro el producto</h2><hr><br>";
    }

?>
