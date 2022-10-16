//let draw = false;

init();

/** FUNCIONES */

function init() {
  // Inicia DATATABLE 
  const table = $("#filtro_menus_entradas_consulta_captura").DataTable({
    //"info":     false,
    "dom": 'Pt', // P OCULTA EL SEARCH
    searchPanes: {
      cascadePanes: true,
      layout: 'columns-4'
    },
    responsive: true,
        pageLength: 20,
    columnDefs: [
      {
          searchPanes: {
              show: true
          },
          targets: [20, 21, 22, 19]
      },
      {
          searchPanes: {
            show: false
          },
          targets: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23, 24, 25]
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
  $('#busqueda_input_captura').on( 'keyup', function () {
    table.search( this.value ).draw();
  } );

  // #columna 0 - PLANTA
  $('#filtro_planta_captura').on( 'keyup', function () {
  table
      .columns( 19 )
      .search( this.value )
      .draw();
  } );

  // #columna 1 - AREA
  $('#filtro_area_captura').on( 'keyup', function () {
  table
      .columns( 20 )
      .search( this.value )
      .draw();
  } );

  // #columna 2 - LINEA
  $('#filtro_linea_captura').on( 'keyup', function () {
  table
      .columns( 21 )
      .search( this.value )
      .draw();
  } );

  // #columna 4 - TURNO
  $('#filtro_turno_captura').on( 'keyup', function () {
  table
      .columns( 23 )
      .search( this.value )
      .draw();
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
    fechaArray = [];

  // Loop en rows
  table.rows({ search: "applied" }).every(function() {
    const data = this.data();
    countryArray.push(data[0]);
    populationArray.push(parseInt(data[14].replace(/\,/g, "")));
    densityArray.push(parseInt(data[18].replace(/\,/g, "")));
    fallasArray.push(data[15]);
    min_fallasArray.push(parseInt(data[17].replace(/\,/g, "")));
    fechaArray.push(data[7]);
  });

  // Almacena toda la data en un dataArray para ser usada en orden
  dataArray.push(countryArray, populationArray, densityArray, fallasArray, min_fallasArray, fechaArray);

  return dataArray;
}

function createHighcharts(data) {
  Highcharts.setOptions({
    lang: {
      thousandsSep: ","
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
