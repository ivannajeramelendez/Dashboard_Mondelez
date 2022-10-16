$(function() {
  const table = Highcharts.Data.prototype.parseTable.call({
    options: {
      table: "ge_global_share"
    },
    columns: [],
    dataFound: () => {}
  });

  const scatterData = table[0].reduce((filtered, elem) => {
    const value = +elem;
    if (!isNaN(value)) {
      filtered.push(value);
    }
    return filtered;
  }, []);

  Highcharts.chart("ge_pie_consolidado", {
    colors: ['#2AB540', '#DF7120', '#2084DF'],
    chart: {
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false,
      type: "pie"
    },
    title: {
      style: {
        color: 'grey',
        font: 'bold 16px "Trebuchet MS", Verdana, sans-serif'
    },
      text: ""
    },
    tooltip: {
      pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>"
    },
    accessibility: {
      point: {
        valueSuffix: "%"
      }
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: "pointer",
        dataLabels: {
          enabled: true,
          format: "<b>{point.name}:</b> {point.percentage:.1f} %"
        },
        showInLegend: true
      }
    },
    data: {
      table: "ge_global_share"
    }
  });
});
