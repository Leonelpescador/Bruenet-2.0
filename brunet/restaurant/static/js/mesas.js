document.addEventListener('DOMContentLoaded', function () {
    const mesas = document.querySelectorAll('.mesa');

    mesas.forEach(mesa => {
        mesa.addEventListener('click', function (event) {
            event.stopPropagation();
            closeAllMenus();

            const menu = mesa.querySelector('.menu-desplegable');
            if (menu) {
                menu.style.display = 'block';
            }
        });
    });

    document.addEventListener('click', function () {
        closeAllMenus();
    });

    function closeAllMenus() {
        const menus = document.querySelectorAll('.menu-desplegable');
        menus.forEach(menu => {
            menu.style.display = 'none';
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const metodoPago = document.getElementById('metodo_pago');
    const montoPagado = document.getElementById('monto_pagado');
    const vuelto = document.getElementById('vuelto');
    const montoTotal = document.getElementById('monto_total').value;

    metodoPago.addEventListener('change', function () {
        if (metodoPago.value === 'efectivo') {
            document.getElementById('efectivo_section').style.display = 'block';
            document.getElementById('vuelto_section').style.display = 'block';
        } else {
            document.getElementById('efectivo_section').style.display = 'none';
            document.getElementById('vuelto_section').style.display = 'none';
        }
    });

    montoPagado.addEventListener('input', function () {
        const pagado = parseFloat(montoPagado.value) || 0;
        const total = parseFloat(montoTotal) || 0;
        vuelto.value = (pagado - total).toFixed(2);
    });
});
