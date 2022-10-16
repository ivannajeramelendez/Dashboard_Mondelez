$(function() {
  const table = Highcharts.Data.prototype.parseTable.call({
    options: {
      table: "data_gwf_loss_bar"
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

  Highcharts.chart("grafica_gwf_loss_bar", {
    colors: ['#16709C'],
    chart: {
      type: "column"
    },
    title: {
      style: {
        color: 'grey',
        font: 'bold 16px "Trebuchet MS", Verdana, sans-serif'
    },
      text: ""
    },
    plotOptions: {
      series: {
        borderWidth: 0,
        dataLabels: {
          enabled: true,
          format: '{point.y:.1f}%'
        }
      }
    },
    tooltip: {
      pointFormat: "Porcentaje: <b>{point.y:.0f}</b> %"
    },
    data: {
      table: "data_gwf_loss_bar"
    },
    dataLabels: {
      enabled: true,
      rotation: -90,
      color: "#FFFFFF",
      align: "right",
      format: "{point.y:.1f}", // one decimal
      y: 10, // 10 pixels down from the top
      style: {
        fontSize: "13px",
        fontFamily: "Verdana, sans-serif"
      }
    }
  });
});
