let draw = false;

init();

/** FUNCIONES */

function init() {
  // Inicia DATATABLE 
  const table = $("#ge_pie_slab").DataTable({
    "info":     false,
    "dom": 't', //OCULTA EL SEARCH
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
    "paginate": {
    "first":      false,
    "last":       false,
    "next":       false,
    "previous":   false
        }
    }
});
  // Buscar en otro input
  $('#search_ge_pie_slab').on( 'keyup', function () {
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

  // Loop en rows
  table.rows({ search: "applied" }).every(function() {
    const data = this.data();
    countryArray.push(data[0]);
    populationArray.push(parseInt(data[14].replace(/\,/g, "")));
    densityArray.push(parseInt(data[18].replace(/\,/g, "")));
  });

  // Almacena toda la data en un dataArray
  dataArray.push(countryArray, populationArray, densityArray);

  return dataArray;
}

function createHighcharts(data) {
  Highcharts.setOptions({
    lang: {
      thousandsSep: ","
    }
  });

  Highcharts.chart("graph_ge_pie_slab", {
    title: {
      text: ""
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
          text: "Tg"
        },
        min: 0,
        opposite: true
      }
    ],
    series: [
      {
        name: "GE",
        color: "#16709C",
        type: "pie",
        data: data[1],
        tooltip: {
          valueSuffix: "%"
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
    legend: {
      backgroundColor: "#ececec",
      shadow: true
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