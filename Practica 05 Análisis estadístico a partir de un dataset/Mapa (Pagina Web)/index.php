<?php
	$nombre1 = $_GET["nombre1"];
	$longitud1 = $_GET["longitud1"];
	$latitud1 = $_GET["latitud1"];
	$presioMayor = $_GET["presioMayor"];
	
	$nombre2 = $_GET["nombre2"];
	$longitud2 = $_GET["longitud2"];
	$latitud2 = $_GET["latitud2"];
	$presioMenor = $_GET["presioMenor"];
?>

<!DOCTYPE html>
<html lang="es">
	<head>
		<title>Status de Gasolina Magna en México</title>
		<meta charset="utf-8" />
        <link rel="stylesheet" type="text/css" href="hoja_mapa.css" />
	</head>
    <body>
		<div class="textos" style="text-align:center;">
			<h1>Status de Gasolina magna en México</h1>
			<h2 style="color:red;">Gasolina de mayor precio (<?php echo $nombre1; ?>): <?php echo $presioMayor; ?></h2>
			<h2 style="color:blue;">Gasolina de menor precio (<?php echo $nombre2; ?>): <?php echo $presioMenor; ?></h2>
		</div>

        <div id="map"></div>
		
		<div id="nombre1" hidden><?php echo $nombre1; ?></div>
		<div id="longitud1" hidden><?php echo $longitud1; ?></div>
		<div id="latitud1"  hidden><?php echo $latitud1; ?></div>
		<div id="presioMayor"  hidden><?php echo $presioMayor; ?></div>

		<div id="nombre2" hidden><?php echo $nombre2; ?></div>
		<div id="longitud2" hidden><?php echo $longitud2; ?></div>
		<div id="latitud2"  hidden><?php echo $latitud2; ?></div>
		<div id="presioMenor"  hidden><?php echo $presioMenor; ?></div>

		<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false&language=es"></script>
		<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
		<script type="text/javascript" src="funciones_mapa.js"></script>
    </body>
</html>
