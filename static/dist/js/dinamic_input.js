// Constantes para el div contenedor de los inputs y el botón de agregar
const contenedor = document.querySelector('#dinamic');
const btnAgregar = document.querySelector('#agregar');

// Variable para el total de elementos agregados
let total = 1;

/**
 * Método que se ejecuta cuando se da clic al botón de agregar elementos
 */
btnAgregar.addEventListener('click', e => {  
    let div = document.createElement('div');
    div.innerHTML = `<br><div class="row"><div class="col-8"><input type="text" class="form-control" name="area[]" placeholder="Ingrese un área"></div><div class="col-4"><button class="btn btn-primary" onclick="eliminar(this)">Eliminar</button></div></div>`;
    contenedor.appendChild(div);
})

/**
 * Método para eliminar el div contenedor del input
 * @param {this} e 
 */
const eliminar = (e) => {

    const divPadre = e.parentNode.parentNode.parentNode;
    contenedor.removeChild(divPadre);
    actualizarContador();
};

/**
 * Método para actualizar el contador de los elementos agregados
*/
const actualizarContador = () => {
    let divs = contenedor.children;
    total = 1;
    for (let i = 0; i < divs.length; i++) {
        //divs[i].children[0].innerHTML = total++;
    }//end for
};