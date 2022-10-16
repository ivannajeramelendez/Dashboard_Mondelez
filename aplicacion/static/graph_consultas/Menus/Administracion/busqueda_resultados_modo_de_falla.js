function filterGlobal() {
  $("#filtro_menus_entradas_consulta_modo_de_falla")
    .DataTable()
    .search($("#global_filter").val())
    .draw();
}

// INIICO DE BUSQUEDA EN TABLA
var table = $("#filtro_menus_entradas_consulta_modo_de_falla").DataTable({
  info: false,
  dom: "t",
  responsive: true,
  pageLength: 20,
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

// BUSQUEDA EN OTRO INPUT
$("input.global_filter").on("keyup click", function () {
  filterGlobal();
});
