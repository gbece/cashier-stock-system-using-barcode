<?php 
if(($handle = fopen("codME.csv", "r")) !== FALSE){
	while(($data = fgetcsv($handle, 1000, ",")) !== FALSE){
		$csv[] = $data;
	}
}	
echo "
	<!DOCTYPE html>
	<html>
	<body>

	<form action='ingreso_producto.php' method='post'> 
	  <h3>
	  Codigo: <input type='text' name='codigo' value=" . $csv[0][2] . "><br>
	  Descripcion: <input type='text' name='descripcion' value=''><br>
	  Precio unitario: <input type='text' name='precio' value=''><br>
	  Unidades: <input type='text' name='unidades' value=''><br>
	  Umbral: <input type='text' name='umbral' value=''><br>
	  <br>
	  </h3>

	 <input type='submit' value='Actualizar'>
	</form>

	</body>
	</html>
	";
	

?>
