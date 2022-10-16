$(function() {
  const table = Highcharts.Data.prototype.parseTable.call({
    options: {
      table: "falla_ctos"
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

    Highcharts.chart("falla_ctos_graph", {
    colors: ['#058DC7'],
    chart: {
        type: 'column'
    },
    title: {
        text: ''
    },
    tooltip: {
      pointFormat: 'Frecuencia: <b>{point.y:.0f}</b>'
    },
    plotOptions: {
        series: {
            borderWidth: 0,
            dataLabels: {
                enabled: true,
                //format: '{point.y:.1f}%'
            }
        }
    },
    data: {
        table: "falla_ctos"
    },
    dataLabels: {
      enabled: true,
      rotation: -90,
      color: '#FFFFFF',
      align: 'right',
      format: '{point.y:.1f}', // one decimal
      y: 10, // 10 pixels down from the top
      style: {
          fontSize: '13px',
          fontFamily: 'Verdana, sans-serif'
      }
  }
    
  });
});