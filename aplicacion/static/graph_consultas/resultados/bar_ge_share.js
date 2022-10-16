let draw = false;

init();

/** FUNCIONES */

function init() {
  // Inicia DATATABLE 
  const table = $("#ge_bar_slab").DataTable({
    "info":     false,
    "dom": 'Pt', // P OCULTA EL SEARCH
    searchPanes: {
      cascadePanes: true,
      layout: 'columns-3'
    },
    responsive: true,
        pageLength: 20,
    columnDefs: [
      {
          searchPanes: {
              show: true
          },
          targets: [0, 1, 8]
      },
      {
          searchPanes: {
            show: false
          },
          targets: [2, 3, 4, 5 , 6 , 7 , 9 , 10, 11, 12, 13, 14, 15, 16, 17, 18]
      }
    ],

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
  // Buscar en otro input
  $('#search_ge_bar_slab').on( 'keyup', function () {
    table.search( this.value ).draw();
  } );
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
    fallasArray = [];
    min_fallasArray = [];

  // Loop en rows
  table.rows({ search: "applied" }).every(function() {
    const data = this.data();
    countryArray.push(data[0]);
    populationArray.push(parseInt(data[14].replace(/\,/g, "")));
    densityArray.push(parseInt(data[18].replace(/\,/g, "")));
    fallasArray.push(data[15]);
    min_fallasArray.push(parseInt(data[17].replace(/\,/g, "")));
  });

  // Almacena toda la data en un dataArray para ser usada en orden
  dataArray.push(countryArray, populationArray, densityArray, fallasArray, min_fallasArray);

  return dataArray;
}

function createHighcharts(data) {
  Highcharts.setOptions({
    lang: {
      thousandsSep: ","
    }
  });

  Highcharts.chart("graph_ge_bar_slab", {
    title: {
      text: "GE Share"
    },
    subtitle: {
      text: ""
    },
    xAxis: [
      {
        categories: data[0],
        labels: {
          rotation: -15
        }
      }
    ],
    yAxis: [
      {
        // Primer yaxis
        title: {
          text: "GE %"
        }
      },
      {
        // Segundo yaxis
        title: {
          text: "Tg %"
        },
        min: 0,
        opposite: true
      }
    ],
    series: [
      {
        name: "GE",
        color: "#16709C",
        type: "column",
        data: data[1],
        tooltip: {
          valueSuffix: " %"
        }
      },
      {
        name: "Tg",
        color: "#2AB540",
        type: "spline",
        data: data[2],
        yAxis: 1
      }
    ],
    tooltip: {
      shared: true
    },
    plotOptions: {
      series: {
        borderWidth: 0,
        dataLabels: {
          enabled: true,
          format: '{point.y:.1f}%'
        }
      }
    },
    legend: {
      backgroundColor: "#fff",
      shadow: false
    },
    credits: {
      enabled: true
    },
    noData: {
      style: {
        fontSize: "16px"
      }
    }
  });

  Highcharts.chart("graph_failure_loss_bar_slab", {
  chart: {
    type: 'column'
  },
  title: {
      text: 'Failure Modes'
  },
  subtitle: {
      text: ''
  },
  xAxis: {
      type: 'category',
      categories: data[3],
      labels: {
          rotation: -0,
          style: {
              fontSize: '11px',
              fontFamily: 'Verdana, sans-serif'
          }
      }
  },
  yAxis: {
      min: 0,
      title: {
          text: 'Min Totales'
      }
  },
  legend: {
      enabled: false
  },
  tooltip: {
      pointFormat: '<b>{point.y:.0f} minutos</b>'
  },
    series: [
      {
        name: "Total Minutos",
        color: "#16709C",
        data: data[4],

        dataLabels: {
          enabled: true,
          //rotation: -90,
          color: 'black',
          align: 'center',
          format: '{point.y:.0f} min', // one decimal
          y: 10, // 10 pixels down from the top
          style: {
              fontSize: '11px',
              fontFamily: 'Verdana, sans-serif'
          }
      }
      }
    ],
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