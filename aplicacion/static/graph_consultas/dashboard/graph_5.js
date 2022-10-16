$(document).ready(function () {
    // Crea DataTable
    var table = $('#busqueda').DataTable({
        //dom: 'Pfrtip',
        "lengthMenu": [[10, 50, -1], [10, 50, "Todo"]],
        "paginate":     true,
        "language": {
        "lengthMenu": " _MENU_ Entradas Máximas",
        "zeroRecords": "No se encontro considencias ",
        "info": "Pagina _PAGE_ de _PAGES_",
        "infoEmpty": "No hay considencias",
        "infoFiltered": "(Numero de datos _MAX_ total)",
        "decimal":        "",
        "emptyTable":     "No hay infomación disponible",
        "infoPostFix":    "",
        "thousands":      ",",
        "loadingRecords": "Cargando...",
        "processing":     "Procesando...",
        "search":         "Buscar: ",
        "zeroRecords":    "No se encontraron resultados",
        "paginate": {
        "first":      "Primero",
        "last":       "Ultimo",
        "next":       false,
        "previous":   false
            }
        }
    });
    // Crea el gráfico con datos iniciales.  *COLOCAS BEFORE O AFTER SEGUN CASO*
    var container = $('<div/>').insertBefore(table.table().container());
    var chart = Highcharts.chart(container[0], {
        chart: {
            type: 'column',
        },
        title: {
            text: 'Slab',
        },
        //subtitle: {
        //    text: 'Procentaje de Ge en Slab'
        //},
        xAxis: {
            type: 'category',
            labels: {
                rotation: -45,
                style: {
                    fontSize: '10px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Resultados'
            }
        },
        legend: {
            enabled: true,
            align: 'right',
            verticalAlign: 'middle',
            layout: 'vertical',
            padding: 3,
            itemMarginTop: 5,
            itemMarginBottom: 5,
            itemStyle: {
                lineHeight: '14px'
            },
            symbolHeight: 12,
            symbolWidth: 12,
            symbolRadius: 6
        },
        tooltip: {
            formatter: function () {
                return '<b>' + ' ' + this.point.name.toLowerCase();
            }
        },
        series: [
            {
                name: '% Ge',
                data: chartData(table),
                type: 'spline'
            },
            {
                name: 'T. Usado',
                data: chartData2(table),
                type: 'column'
            },
            {
                name: 'T. Operativo',
                data: chartData3(table),
                type: 'column'
            }
        ],
    });
    // En cada busqueda, actualice los datos en el gráfico.
    table.on('draw', function () {
        chart.series[0].setData(chartData(table));
        chart.series[1].setData(chartData2(table));
        chart.series[2].setData(chartData3(table));
    });
});

function chartData(table) {
    var counts = {};
    // Cuente el número de entradas para cada puesto.
    table
        .column(12, { search: 'applied' })
        .data()
        .each(function (val) {
            if (counts[val]) {
                counts[val] += 1;
            } else {
                counts[val] = 1;
            }
        });
    // Y mapearlo al formato que usa highcharts.
    return $.map(counts, function (val, key) {
        return {
            name: key,
            y: val,
        };
    });
}

function chartData2(table) {
    var counts = {};
    // Cuente el número de entradas para cada puesto.
    table
        .column(10, { search: 'applied' })
        .data()
        .each(function (val) {
            if (counts[val]) {
                counts[val] += 1;
            } else {
                counts[val] = 1;
            }
        });
    // Y mapearlo al formato que usa highcharts.
    return $.map(counts, function (val, key) {
        return {
            name: key,
            y: val,
        };
    });
}

function chartData3(table) {
    var counts = {};
    // Cuente el número de entradas para cada puesto.
    table
        .column(11, { search: 'applied' })
        .data()
        .each(function (val) {
            if (counts[val]) {
                counts[val] += 1;
            } else {
                counts[val] = 1;
            }
        });
    // Y mapearlo al formato que usa highcharts.
    return $.map(counts, function (val, key) {
        return {
            name: key,
            y: val,
        };
    });
}

