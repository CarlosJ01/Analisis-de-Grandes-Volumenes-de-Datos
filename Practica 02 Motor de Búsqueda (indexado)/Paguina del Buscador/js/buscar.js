$(document).ready(function () {
    $('#formBuscador').submit(function (e) { 
        e.preventDefault();
        window.location=`enlaces.php?query=${$('#palabra').val()}`;
    });
});