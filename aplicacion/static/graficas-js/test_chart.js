var table = document.getElementById("busqueda")
var tableLen = table.rows.length
var data = {labels: [], prod: [], ge: [], max: [], min: [] }

for (var i = 1; i < tableLen; i++) {
  data.labels.push(table.rows[i].cells[0].innerText)
  data.prod.push(table.rows[i].cells[11].innerText)
    
  data.ge.push(table.rows[i].cells[12].innerText)
  data.max.push(table.rows[i].cells[9].innerText)
  data.min.push(table.rows[i].cells[10].innerText)
}

var canvasP = document.getElementById("pieChart")
var ctxP = canvasP.getContext('2d')
var myPieChart = new Chart(ctxP, {
  type: 'bar',
  data: {
    labels: data.labels,
    datasets: [{
      data: data.prod,
      label: 'T. Prod',
      type: "line",
      borderColor: "#3e95cd",
        fill: false
    },
    {
        data: data.max,
        label: 'T. Max',
        type: "bar",
        backgroundColor: "#7FCA23",
      },
    {
        data: data.min,
        label: 'T. Min',
        type: "bar",
        backgroundColor: "#EB5F1E",
      }]
  },
  options: {
    legend: {
        display: true,
        position: "right"
    }
  }
})

