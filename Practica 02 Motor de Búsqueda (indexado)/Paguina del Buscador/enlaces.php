<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Practica 02 Motor de Busqueda</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
	<script src="js/jquery-3.6.0.min.js"></script>
    <link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script type="text/javascript" src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
    <input type="hidden" id="query" value="<?php echo $_GET['query'];?>">
    <nav class="text-right">
		<a href="#">Analisis de Grandes Volumenes de Datos</a>
		<img src="img/g-menu.PNG">
		<button>Sign in</button>
	</nav>
    <hr>
    <section class="section-1 mb-3">
		<div class="container mt-3">
            <div class="text-right">
                <a href="index.html" class="btn btn-success">Volver a buscar</a>
            </div>

            <label class="font-weight-bold">Búsqueda realizada: </label>
            <input type="text" id="query" class="form-control" value="<?php echo $_GET['query'];?>" readonly>

            <small class="text-muted" id="links"></small>
            <div class="mt-4" id="body">
                
            </div>
        </div>
	</section>
    <footer>
		<div class="links">
			<div class="link-1">
				<a href="#">Carlos Castro</a>
				<a href="#">Giovanni Martinez</a>
				<a href="#">Jaime Velazquez</a>
			</div>
		</div>
	</footer>
    <script src="js/enlaces.js"></script>
</body>
</html>
