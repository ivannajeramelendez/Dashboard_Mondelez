// FUNCION PARA MOVER EL BOTON DE EXPORTAR
var org_buildButton = $.fn.DataTable.Buttons.prototype._buildButton;
$.fn.DataTable.Buttons.prototype._buildButton = function(config, collectionButton) {
    var button = org_buildButton.apply(this, arguments);
    $(document).one('init.dt', function(e, settings, json) {
       if (config.container && $(config.container).length) {
          $(button.inserter[0]).detach().appendTo(config.container)
       }
   })    
   return button;
}

// SEARCH CON IDIOMA
  $(document).ready(function () {
    DataTable = $("#filtro_menus_entradas_consulta_extracto_gwf").DataTable({
    dom: 'PtBt',
    //buttons: [ {
    //    extend: 'excelHtml5',
    //    autoFilter: true,
    //    className: "btn btn-primary",
    //    sheetName: 'Exported data',
    //    text: 'Exportar a Excel',
    //} ],
    buttons: {
      buttons: [
        {
          text: "Exportar a Excel",
          extend: 'excelHtml5',
          autoFilter: true,
          sheetName: 'Exported data',
          container: '#boton_exportar_excel'
        }
      ],
      dom: {
        button: {
          tag: "button",
          className: "btn btn-sm btn-warning"
        },
        buttonLiner: {
          tag: null
        }
      }
    },
    info: false,
    searchPanes: {
      cascadePanes: true,
      layout: "columns-5",
    },
    responsive: true,
    pageLength: 20,
    columnDefs: [
      {
        searchPanes: {
          show: true,
        },
        targets: [19, 20, 21, 22, 23],
      },
      {
        searchPanes: {
          show: false,
        },
        targets: [0, 1, 2, 3, 4, 5, 6 , 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 24, 25, 26, 27],
      },
    ],
    lengthMenu: false,
    paginate: false,
    language: {
      lengthMenu: " _MENU_ Entradas Máximas",
      zeroRecords: "No se encontro considencias ",
      info: "Pagina _PAGE_ de _PAGES_",
      infoEmpty: "No hay considencias",
      infoFiltered: "(Numero de datos _MAX_ total)",
      decimal: "",
      emptyTable: "No hay infomación disponible",
      infoPostFix: "",
      thousands: ",",
      loadingRecords: "Cargando...",
      processing: "Procesando...",
      search: "Buscar: ",
      zeroRecords: "No se encontraron resultados",
      searchPanes: {
        clearMessage: "Limpiar Filtro",
        title: {
          _: "Filters Selected - %d",
          0: "Sin Selección",
          1: "1 Filtro",
          2: "2 Filtros",
          3: "3 Filtros",
        },
        collapse: { 0: "Busqueda", _: "Search Options (%d)" },
      },
      paginate: {
        first: false,
        last: false,
        next: false,
        previous: false,
      },
    },
  });

  $("#busqueda_input_extracto_gwf").keyup(function () {
    DataTable.search($(this).val()).draw();
  });

});
