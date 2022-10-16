am4core.ready(function () {
  // Themes inicio
  am4core.useTheme(am4themes_animated);
  // Themes fin

  // Crear chart instancia
  var chart = am4core.create("dona", am4charts.PieChart);
  // Exportar
  // chart.exporting.menu = new am4core.ExportMenu();

  // Agregar data
  chart.data = [
    {
      nombre: "GE",
      porcentaje: 78,
    },
    {
      nombre: "GE Tg",
      porcentaje: 16.72,
    }
  ];

  // Agregar y configurara Series
  var pieSeries = chart.series.push(new am4charts.PieSeries());
  pieSeries.dataFields.value = "porcentaje";
  pieSeries.dataFields.category = "nombre";
  pieSeries.slices.template.stroke = am4core.color("#fff");
  pieSeries.slices.template.strokeWidth = 2;
  pieSeries.slices.template.strokeOpacity = 1;

  // Esto crea la animacion incial
  pieSeries.hiddenState.properties.opacity = 1;
  pieSeries.hiddenState.properties.endAngle = -90;
  pieSeries.hiddenState.properties.startAngle = -90;
}); // fin am4core.ready()
