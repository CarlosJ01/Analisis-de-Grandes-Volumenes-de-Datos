function info(id) {
  $('#footer-' + id).removeClass("d-none");
  $('#col-' + id+'-1').removeClass("d-none");
  $('#col-' + id+'-2').removeClass("d-none");

  $('#btn-'+id).addClass("d-none");
}

$(document).ready(function () {
  $.ajax({
    type: "get",
    url: "http://127.0.0.1:8080/datos",
    dataType: "json",
    success: function (data) {
      console.log(data);
      prob=0;
      data.marcadores.forEach(task => {
        for(var i=0; i<task.length; i++){
          if(task[i]>prob){
            prob=task[i];
          }
        }
      });
      var cont=0;
      var word="";
      for(var i=0; i<data.partido.equipo1.length; i++){
        word += data.partido.equipo1[i]+`<br>`;
      }
      var tbd=`<tr><th rowspan="7" class="bg-light">`+word+`</th></tr>`;
      data.marcadores.forEach(task => {
        tbd+=`<tr><th>`+cont+`</th>`;
        for(var i=0; i<task.length; i++){
          if(task[i]==prob){
            tbd+=`<th class="text-success">`+task[i]+`</th>`;
          }
          else{
            tbd+=`<td>`+task[i]+`</td>`;
          }
        }
        cont++;
      });
      tbd+=`</tr>`;


      cad=`<div class="col-md-8 offset-md-2">
      <div class="card mb-3 rounded-3 shadow-sm">
        <div class="card-header py-2">
          <h4 class="my-0 fw-normal">`+data.partido.tipo+`</h4>
        </div>
        <div class="card-body">
          <div class="row">
            <div class="col-md-5">
              <img style="width: 30px;" class="card-img-top" src="`+data.partido.logo1+`"
                alt="Card image cap">
              <span class="col">`+data.partido.equipo1+`</span>
            </div>
            <div class="col-md-2">
              <img style="width: 30px;" class="card-img-top" src="images/vs.png" alt="Card image cap">
            </div>
            <div class="col-md-5">
              <img style="width: 30px;" class="card-img-top" src="`+data.partido.logo2+`" alt="Card image cap">
              <span class="col">`+data.partido.equipo2+`</span>
            </div>
            <div class="col-md-12 mt-4">
              <span>`+data.partido.fecha+`</span>
            </div>
            <div class="col-md-4 offset-md-4 mt-4">
              <button type="button" class="btn btn-light" onclick="info(`+data.partido.id+`)" id="btn-`+data.partido.id+`">
                Ver más
              </button>
            </div>            
            <div class="col-md-6 d-none" id="col-`+data.partido.id+`-1">
              <p><strong>Ataque: </strong>`+data.equipo1.ataque+`</p>
              <p><strong>Defensa: </strong>`+data.equipo1.defensa+`</p>
              <p><strong>Exito: </strong>`+data.equipo1.exito+`</p>
            </div>
            <div class="col-md-6 d-none" id="col-`+data.partido.id+`-2">
            <p><strong>Ataque: </strong>`+data.equipo2.ataque+`</p>
            <p><strong>Defensa: </strong>`+data.equipo2.defensa+`</p>
            <p><strong>Exito: </strong>`+data.equipo2.exito+`</p>
            </div>

          </div>
        </div>
        <div class="card-footer d-none" id="footer-`+data.partido.id+`">
          <div class="bg-white">
            <div class="table-responsive">
              <table class="table table-sm table-bordered">
                <thead>
                  <th><td></td><td colspan="8" class="bg-light">`+data.partido.equipo2+`</th></tr>
                  <tr>
                  <th width="10%"></th>
                  <th width="10%"></th>
                    <th width="13%">0</th>
                    <th width="13%">1</th>
                    <th width="13%">2</th>
                    <th width="13%">3</th>
                    <th width="13%">4</th>
                    <th width="13%">5</th>
                  </tr>
                </thead>
                <tbody>
                  `+tbd+`
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>`;
      $('#partidos').append(cad)
    }
  });
});