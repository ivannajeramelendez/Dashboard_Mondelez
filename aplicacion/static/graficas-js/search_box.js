// SEARCH CON IDIOMA
$(document).ready(function() {
$('#search_box').DataTable( {
    "lengthMenu": [[20, 50, -1], [20, 50, "Todo"]],
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
} );
} );