var ctx = document.getElementById("cto_slab1s");
var a = document.getElementById("cto_totales");
var myChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["Slab1s", "Slab3s", "Slab6s", "EVUP", "Clorets", "CL6", "Halls", "Halls1's", "PB's", "Bubba"],
    datasets: [
      {
        label: "T. Prod",
        data: [600, 500, 400, 300, 200, 100, 200, 300, 400, 500],
        backgroundColor: 'rgba(62, 149, 205)'
      },
      {
        label: "T. Usad",
        data: [400, 300, 200, 100, 200, 300, 400, 300, 200, 100],
        backgroundColor: 'rgba(39, 174, 96)'
      }
    ]
  }
});

var ctx = document.getElementById("cto_ge");
var a = document.getElementById("cto_totales_ge");
var myChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["Slab1s", "Slab3s", "Slab6s", "EVUP", "Clorets", "CL6", "Halls", "Halls1's", "PB's", "Bubba"],
    datasets: [
      {
        label: "Ge",
        data: [90, 80, 70, 60, 70, 80, 90, 80, 70, 60],
        backgroundColor: 'rgba(243, 156, 18)'
      }
    ]
  }
});

