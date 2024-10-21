document.addEventListener('DOMContentLoaded', function () {
    // Configuración del gráfico
    const ctx = document.getElementById('myChart').getContext('2d');

    // Obtener datos de la API
    fetch('D:\FLASK\django_menu\ventas_ejemplo.xlsx')
        .then(response => response.json())
        .then(data => {
            const myChart = new Chart(ctx, {
                type: 'bar',  // Cambia el tipo de gráfico si es necesario
                data: {
                    labels: data.meses,  // Usar los meses del archivo Excel
                    datasets: [{
                        label: 'Ventas Mensuales',
                        data: data.ventas,  // Usar las ventas del archivo Excel
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error al obtener los datos:', error));
});
