document.addEventListener('DOMContentLoaded', function() {
    const resumenPedido = document.getElementById('resumenPedido');
    const categoriaFiltro = document.getElementById('categoriaFiltro');
    let pedido = [];

    // Evento para agregar platos al pedido
    document.querySelectorAll('.agregar-pedido').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const platoId = this.getAttribute('data-id');
            const platoPrecio = this.getAttribute('data-precio');
            const platoNombre = this.closest('.card').querySelector('.card-title').innerText;

            // Verificar si el plato ya existe en el pedido
            const itemExistente = pedido.find(p => p.plato_id == platoId);
            if (itemExistente) {
                itemExistente.cantidad += 1;
            } else {
                pedido.push({ plato_id: platoId, nombre: platoNombre, cantidad: 1, precio_unitario: platoPrecio });
            }

            renderPedido();
        });
    });

    // Manejo del envío del formulario
    document.getElementById('pedidoForm').addEventListener('submit', function(e) {
        e.preventDefault();  // Evitar el envío normal del formulario
        
        // Verifica si hay platos en el pedido
        if (pedido.length === 0) {
            alert("Por favor, agrega al menos un plato al pedido.");
            return;
        }

        // Enviar los datos del pedido al servidor usando fetch
        fetch(window.location.href, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ platos: pedido })
        }).then(response => response.json())
          .then(data => {
              if (data.success) {
                  alert('Pedido creado con éxito');
                  window.location.href = '/';  // Redirigir después de crear el pedido
              } else {
                  alert('Hubo un error al crear el pedido');
              }
          }).catch(error => console.error('Error:', error));
    });

    // Función para mostrar el resumen del pedido
    function renderPedido() {
        resumenPedido.innerHTML = '';
        pedido.forEach(plato => {
            const li = document.createElement('li');
            li.innerText = `${plato.nombre} - ${plato.cantidad} unidades - $${plato.precio_unitario * plato.cantidad}`;
            resumenPedido.appendChild(li);
        });
    }

    // Función para obtener el CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
