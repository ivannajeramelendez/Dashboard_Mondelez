function calculo() {
try {
  var a = parseInt(document.getElementById("basic_1").value) || 0,
      b = parseInt(document.getElementById("basic_2").value) || 0,
      c = parseInt(document.getElementById("basic_3").value) || 0,
      d = parseInt(document.getElementById("basic_4").value) || 0,
      e = parseInt(document.getElementById("basic_5").value) || 0,
      f = parseInt(document.getElementById("intelligence_1").value) || 0,
      g = parseInt(document.getElementById("intelligence_2").value) || 0,
      h = parseInt(document.getElementById("intelligence_3").value) || 0,
      i = parseInt(document.getElementById("intelligence_4").value) || 0,
      j = parseInt(document.getElementById("intelligence_5").value) || 0,
      k = parseInt(document.getElementById("eradication_1").value) || 0,
      l = parseInt(document.getElementById("eradication_2").value) || 0,
      ñ = parseInt(document.getElementById("eradication_3").value) || 0,
      o = parseInt(document.getElementById("eradication_4").value) || 0,
      p = parseInt(document.getElementById("eradication_5").value) || 0,
      q = parseInt(document.getElementById("eradication_6").value) || 0,
      r = parseInt(document.getElementById("eradication_7").value) || 0,
      s = parseInt(document.getElementById("prevention_1").value) || 0,
      t = parseInt(document.getElementById("prevention_2").value) || 0,
      w = parseInt(document.getElementById("prevention_3").value) || 0,
      x = parseInt(document.getElementById("prevention_4").value) || 0,
      y = parseInt(document.getElementById("prevention_5").value) || 0,
      // Calculos Acreditacion
      longitud = 88;
      suma = a + b + c + d + e + f + g + h + i + j + k + l + ñ + o + p + q + r + s + t + w + x + y;
      porcentaje = suma * 100 / longitud;
      // Resultados
      document.getElementById("acreditacion").value = porcentaje.toFixed(0);
      //document.getElementById("tiempo_maximo").value = (tiempo_maximo);
      //document.getElementById("tiempo_operativo").value = (display/maquina).toFixed(0);
      //document.getElementById("quality_loss_min").value = quality_loss.toFixed(0);
      //document.getElementById("ge").value = ((tiempo_operativo_ge) / tiempo_usado_ge * 100).toFixed(2);
      //document.getElementById("tiempo_usado").value = (resta_minutos);
    } catch (e) {}
  }
