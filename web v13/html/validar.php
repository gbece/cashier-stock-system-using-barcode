<html>
<head>
	<title>Gestion de STOCK</title>
</head>
<?php 
$modo = shell_exec("gpio -g read 25"); // leo el valor del GPIO 25 usando wiringPi
if ($modo == 0){
	echo '<script type="text/javascript">',
		'window.paret.replace("inicio_normal.html");',
      		'</script>'
		; // redirecciono a modo especial
	
}
else {
	echo '<script type="text/javascript">',
		'window.parent.replace("mantenimiento.html");',
      		'</script>'
		; // redirecciono a modo normal
		
}
?>

</html>
