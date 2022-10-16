$(function() {
    const table = Highcharts.Data.prototype.parseTable.call({
      options: {
        table: "datatable_4"
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
  
      Highcharts.chart("container_4", {
      colors: ['#058DC7'],
      chart: {
          type: 'bar'
      },
      title: {
          text: ''
      },
      tooltip: {
        pointFormat: 'Porcentaje: <b>{point.y:.1f} %</b>'
      },
      plotOptions: {
        series: {
            borderWidth: 0,
            dataLabels: {
                enabled: true,
                format: '{point.y:.0f}%'
            }
        }
      },
      data: {
          table: "datatable_4"
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