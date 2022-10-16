function cal() {
try {
  var a = parseInt(document.getElementById("tiempooperativo").value) || 0,
      b = parseInt(document.getElementById("paro").value) || 0,
      c = parseInt(document.getElementById("tiempooperativo").value) || 0,  
      // Minutos totales fallas
      f = parseInt(document.getElementById("minuto1").value) || 0;
      g = parseInt(document.getElementById("minuto2").value) || 0;
      h = parseInt(document.getElementById("minuto3").value) || 0;
      i = parseInt(document.getElementById("minuto4").value) || 0;
      j = parseInt(document.getElementById("minuto5").value) || 0;
      k = parseInt(document.getElementById("minuto6").value) || 0;
      n = parseInt(document.getElementById("minuto7").value) || 0;
      m = parseInt(document.getElementById("minuto8").value) || 0;
      o = parseInt(document.getElementById("minuto9").value) || 0;
      p = parseInt(document.getElementById("minuto10").value) || 0;
      t = parseInt(document.getElementById("minuto11").value) || 0;
      u = parseInt(document.getElementById("minuto12").value) || 0;
      w = parseInt(document.getElementById("minuto13").value) || 0;
      x = parseInt(document.getElementById("minuto14").value) || 0;
      y = parseInt(document.getElementById("minuto15").value) || 0;
      // Quality Loss
      r = parseInt(document.getElementById("rework").value) || 0;
      s = parseInt(document.getElementById("scrap").value) || 0;
      // SKU, Velocidad de kg por minuto
      peso_kg = parseFloat(document.getElementById("sku").value) || 0;
      // Total Display
      display = parseInt(document.getElementById("total_display").value) || 0;
      // Maquina Velocidad
      maquina = parseFloat(document.getElementById("maquina_speed").value) || 0;
      // Calculos
      tiempo_maximo = c;
      resta_minutos = a - b - f - g - h - i - j - k - n - m - o - p - t - u - w - x - y;
      suma_minutos = a + b + f + g + h + i + j + k + n + m + o + p - t - u - w - x - y;
      quality_loss = (r + s) / peso_kg / 60 * 100;
      // GE
      tiempo_usado_ge = resta_minutos;
      tiempo_operativo_ge = display / maquina;
      // Speed Loss
      //produccion_teorica = (peso_kg * 60) * 397 / 1000 * 100;
      //produccion_real = (peso_kg * 60) / 359;
      tiempo_por_justificar = resta_minutos - (display/maquina)
      // Resultados
      document.getElementById("speed_loss").value = (tiempo_por_justificar - quality_loss).toFixed(0);
      document.getElementById("tiempo_maximo").value = (tiempo_maximo);
      document.getElementById("tiempo_operativo").value = (display/maquina).toFixed(0);
      document.getElementById("quality_loss_min").value = quality_loss.toFixed(0);
      document.getElementById("ge").value = ((tiempo_operativo_ge) / tiempo_usado_ge * 100).toFixed(2);
      document.getElementById("tiempo_usado").value = (resta_minutos);
    } catch (e) {}
  }
