$(function() {
  const table = Highcharts.Data.prototype.parseTable.call({
    options: {
      table: "ge_ctos"
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

    Highcharts.chart('ge_ctos_graph', {
    colors: ['#2AB540', '#DF7120', '#2084DF'],
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: ''
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}:</b> {point.percentage:.1f} %'
            },
            showInLegend: true
        }
    },
    data: {
        table: "ge_ctos"
    },
});
})