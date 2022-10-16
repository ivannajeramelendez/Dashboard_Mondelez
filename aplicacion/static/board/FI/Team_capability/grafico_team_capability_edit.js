let draw = false;

init();

/** FUNCIONES */

function init() {
  // Inicia DATATABLE 
  const table = $("#data_calificacion").DataTable({
    //"info":     false,
    "dom": 'Pt', // P OCULTA EL SEARCH
    //"order": [[ 3, "desc" ]], el 3 es la column
    "lengthMenu": false,
    "paginate":     false,
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
    "search":         "",
    "zeroRecords":    "No se encontraron resultados",
    searchPanes: {
      clearMessage: 'Limpiar Filtro',
      title: {
        _: 'Filters Selected - %d',
        0: 'Sin Selección',
        1: '1 Filtro',
        2: '2 Filtros',
        3: '3 Filtros'
      },
      collapse: {0: 'Busqueda', _: 'Search Options (%d)'}
    },
    "paginate": {
    "first":      false,
    "last":       false,
    "next":       false,
    "previous":   false
        }
    }
  });

  // Obtiene la Data de la tabla
  const tableData = getTableData(table);
  // Crea Highcharts
  createHighcharts(tableData);
  // Evento de la tabla
  setTableEvents(table);
}

function getTableData(table) {
  const dataArray = [],
    countryArray = [],
    populationArray = [],
    densityArray = [];

  // Loop en rows
  table.rows({ search: "applied" }).every(function() {
    const data = this.data();
    countryArray.push(data[1]);
    populationArray.push(parseInt(data[2].replace(/\,/g, "")));
    densityArray.push(parseInt(data[2].replace(/\,/g, "")));
  });

  // Almacena toda la data en un dataArray para ser usada en orden
  dataArray.push(countryArray, populationArray, densityArray);

  return dataArray;
}

function createHighcharts(data) {
  Highcharts.setOptions({
    lang: {
      thousandsSep: ","
    }
  });

  Highcharts.chart("data_calificacion_graph", {
    chart: {
      polar: true,
      type: 'area'
    },
    accessibility: {
      description: ''
    },
    title: {
      text: '',
      x: -80
    },
    pane: {
      size: '90%'
    },
    xAxis: {
      categories: data[0],
      tickmarkPlacement: 'on',
      lineWidth: 0
    },
    yAxis: {
      gridLineInterpolation: 'polygon',
      lineWidth: 0,
      min: 0,
      max: 100
    },
    tooltip: {
      shared: true,
      pointFormat: '<span style="color:{series.color}">{series.name}: <b>{point.y:,.0f} %</b><br/>'
    },
    legend: false,
    series: [{
      name: 'Step Up Card',
      color: "#EE570C",
      data: data[2],
      pointPlacement: 'on'
    }],
    responsive: {
      rules: [{
        condition: {
          maxWidth: 500
        },
        chartOptions: {
          legend: {
            align: 'center',
            verticalAlign: 'bottom',
            layout: 'horizontal'
          },
          pane: {
            size: '70%'
          }
        }
      }]
    }
  });

}

function setTableEvents(table) {
  // Escucha le cambio de la pagina
  table.on("page", () => {
    draw = true;
  });

  // Escucha y ajusta el cambio de la pagina
  table.on("draw", () => {
    if (draw) {
      draw = false;
    } else {
      const tableData = getTableData(table);
      createHighcharts(tableData);
    }
  });
}
