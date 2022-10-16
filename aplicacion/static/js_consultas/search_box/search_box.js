// SEARCH CON IDIOMA
$(document).ready(function() {
$('#search_box').DataTable( {
    dom: 'Bfrtip',
    //buttons: ['copy', 'csv', 'excel', 'pdf'],
    buttons: [ {
        extend: 'excelHtml5',
        autoFilter: true,
        sheetName: 'Exported data',
        text: 'Exportar a Excel',
    } ],
    "lengthMenu": [[50, -1], [50, "Todo"]],
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
    "search":         "Buscar: ",
    "zeroRecords":    "No se encontraron resultados",
    "paginate": {
    "first":      false,
    "last":       false,
    "next":       false,
    "previous":   false
        }
    }
} );
} );