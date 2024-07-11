/*  funciones_mapa.js   */
$(document).ready(function () {
        let nombre1 = $("#nombre1").text(),
        presioMayor = $("#presioMayor").text(),
        longitud1 = $("#longitud1").text(),
        latitud1 = $("#latitud1").text();
        
        let nombre2 = $("#nombre2").text(),
        presioMenor = $("#presioMenor").text(),
        longitud2 = $("#longitud2").text(),
        latitud2 = $("#latitud2").text();

        console.log("Nombre: "+nombre1+" Longitud1: "+longitud1+" Latitud1: "+latitud1+" Presio: "+presioMayor);
        console.log("Nombre: "+nombre2+" Longitud2: "+longitud2+" Latitud2: "+latitud2+" Presio: "+presioMenor);

        var mapDiv = document.getElementById('map');
        var mexico = new google.maps.LatLng(22.063477, -101.255729);
        var options = {
                center: mexico,
                zoom: 5,
                mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var mapa = new google.maps.Map(mapDiv, options);

        var punto_01 = new google.maps.Marker({
                position: new google.maps.LatLng(latitud1, longitud1),
                map: mapa,
                title: 'Titulo'
        });
        punto_01.addListener('click', function() {
                new google.maps.InfoWindow({
                        content: `
                                <strong>${nombre1}</strong>
                                <p>$ ${presioMayor}</p>
                        `
                }).open(map, punto_01);
        });

        var punto_02 = new google.maps.Marker({
                position: new google.maps.LatLng(latitud2, longitud2),
                map: mapa,
                icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
        });
        punto_02.addListener('click', function() {
                new google.maps.InfoWindow({
                        content: `
                                <strong>${nombre2}</strong>
                                <p>$ ${presioMenor}</p>
                        `
                }).open(map, punto_02);
        });
});
