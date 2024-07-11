let actions = {
    getPaginas: function () {  
        $.ajax({
            type: "post",
            url: `http://127.0.0.1:8080/buscar/${$('#query').val()}`,
            data: {},
            dataType: "json",
            success: function (response) {
                links=response.links.length;
                $('#links').text("Se han encontrado alrededor de "+links+" resultado(s):")
                $.each(response.links, function (i, obj) {
                    console.log(obj);
                    card=`<a href="${obj.url}" target="_blank">${obj.titulo}</a>
                    <p>${obj.descripcion} <span class="text-sm text-muted"> ${obj.keywords} </span></p><hr>`;
                    $('#body').append(card);  
                });
            }
        });
    }
}
$(document).ready(function () {
    actions.getPaginas();
});