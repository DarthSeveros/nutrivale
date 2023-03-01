function setIdDelete(id, nombre, url){
    document.getElementById('deleteConfirm').href = url;
    document.getElementById('datoEliminado').textContent = nombre;
}

function onLoadModal(modalId){
    let html = '<div id="modalBack" class="modal-backdrop fade show" onclick="dismiss(modalBack)"></div>';
    document.body.insertAdjacentHTML('beforeend', html);
    let modal = document.getElementById(modalId);
    modal.classList.add('show');
    modal.style = 'display: block;';
}

function dismissDiv(div){
    document.getElementById(div).remove();
}

function dismissModal(modalId){
    modal = document.getElementById(modalId);
    modal.classList.remove('show');
    modal.style = 'display: none;';
    dismissDiv('modalBack');
}

function setIMC(id_peso, id_talla, id_IMC){
    let peso = document.getElementById(id_peso).value;
    let talla = document.getElementById(id_talla).value / 100;
    document.getElementById(id_IMC).value = peso / (talla * talla);
}

meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiempre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]

dias = [
    "Domingo",
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado"
]

function setFecha(year, month, day){
    if (month < 10){
        month = '0' + month.toString()
    }
    else{
        month = month.toString()
    }
    if (day < 10){
        day = '0' + day.toString()
    }
    else {
        day = day.toString()
    }
    document.getElementById("id_fecha").value = year.toString() + '-' + month + '-' + day
}

function setHoras(horas){
    document.getElementById("id_hora").innerText = null
    document.getElementById("id_hora").options.add(new Option("Seleccione...", ""))
    for (hora in horas){
        document.getElementById("id_hora").options.add(new Option(horas[hora], horas[hora]))
    }
    
}

function setHora(hora){
    document.getElementById("id_hora").value = hora
}

function removeModal(){
    document.getElementsByClassName("modal-backdrop")[0].remove()
}

function validate(){
    let form = document.getElementsByTagName("form")[0]
    form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
  
        form.classList.add('was-validated')
      }, false)
  
}

function showModal(){
    let modal = new bootstrap.Modal(document.getElementById('addItemModal'), {
        keyboard: false
      })
    
}
