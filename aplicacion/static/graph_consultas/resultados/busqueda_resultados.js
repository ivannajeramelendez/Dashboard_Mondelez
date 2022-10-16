// SEARCH CON IDIOMA
$(document).ready(function () {
  $("#busqueda_filtro_completo").DataTable({
    info: false,
    dom: "Pt",
    searchPanes: {
      cascadePanes: true,
      layout: "columns-4",
    },
    responsive: true,
    pageLength: 20,
    columnDefs: [
      {
        searchPanes: {
          show: true,
        },
        targets: [0, 1, 3, 4],
      },
      {
        searchPanes: {
          show: false,
        },
        targets: [2, 3, 4, 5],
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
});
