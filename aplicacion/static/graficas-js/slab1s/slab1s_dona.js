am4core.ready(function () {
  // Themes inicio
  am4core.useTheme(am4themes_animated);
  // Themes fin

  // Crea chart instancia
  var chart = am4core.create("barras1s", am4charts.XYChart);

  // Exportar
  chart.exporting.menu = new am4core.ExportMenu();

  // Data para both series
  var data = [
    {
      linea: "1s",
      real: 20,
      target: 21,
    },
    {
      linea: "3s",
      real: 26,
      target: 29,
    },
    {
      linea: "6s",
      real: 30,
      target: 32,
    }
  ];

  /* Crea axes */
  var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
  categoryAxis.dataFields.category = "linea";
  categoryAxis.renderer.minGridDistance = 30;

  /* Crea valor axis */
  var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

  /* Crea series */
  var columnSeries = chart.series.push(new am4charts.ColumnSeries());
  columnSeries.name = "Real";
  columnSeries.dataFields.valueY = "real";
  columnSeries.dataFields.categoryX = "linea";

  columnSeries.columns.template.tooltipText =
    "[#fff font-size: 15px]{name} in {categoryX}:\n[/][#fff font-size: 20px]{valueY}[/] [#fff]{additional}[/]";
  columnSeries.columns.template.propertyFields.fillOpacity = "fillOpacity";
  columnSeries.columns.template.propertyFields.stroke = "stroke";
  columnSeries.columns.template.propertyFields.strokeWidth = "strokeWidth";
  columnSeries.columns.template.propertyFields.strokeDasharray = "columnDash";
  columnSeries.tooltip.label.textAlign = "middle";

  var lineSeries = chart.series.push(new am4charts.LineSeries());
  lineSeries.name = "Target";
  lineSeries.dataFields.valueY = "target";
  lineSeries.dataFields.categoryX = "linea";

  lineSeries.stroke = am4core.color("#4071e3");
  lineSeries.strokeWidth = 3;
  lineSeries.propertyFields.strokeDasharray = "lineDash";
  lineSeries.tooltip.label.textAlign = "middle";

  var bullet = lineSeries.bullets.push(new am4charts.Bullet());
  bullet.fill = am4core.color("#4071e3"); // tooltips grab fill from parent by default
  bullet.tooltipText =
    "[#fff font-size: 15px]{name} in {categoryX}:\n[/][#fff font-size: 20px]{valueY}[/] [#fff]{additional}[/]";
  var circle = bullet.createChild(am4core.Circle);
  circle.radius = 4;
  circle.fill = am4core.color("#fff");
  circle.strokeWidth = 3;

  chart.data = data;
}); // fin am4core.ready()
