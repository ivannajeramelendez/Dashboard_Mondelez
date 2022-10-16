function calculo_leader() {
try {
  var a = parseInt(document.getElementById("basic_1_leader").value) || 0,
      b = parseInt(document.getElementById("basic_2_leader").value) || 0,
      c = parseInt(document.getElementById("basic_3_leader").value) || 0,
      d = parseInt(document.getElementById("basic_4_leader").value) || 0,
      e = parseInt(document.getElementById("basic_5_leader").value) || 0,
      f = parseInt(document.getElementById("intelligence_1_leader").value) || 0,
      g = parseInt(document.getElementById("intelligence_2_leader").value) || 0,
      h = parseInt(document.getElementById("intelligence_3_leader").value) || 0,
      i = parseInt(document.getElementById("intelligence_4_leader").value) || 0,
      j = parseInt(document.getElementById("intelligence_5_leader").value) || 0,
      k = parseInt(document.getElementById("eradication_1_leader").value) || 0,
      l = parseInt(document.getElementById("eradication_2_leader").value) || 0,
      ñ = parseInt(document.getElementById("eradication_3_leader").value) || 0,
      o = parseInt(document.getElementById("eradication_4_leader").value) || 0,
      p = parseInt(document.getElementById("eradication_5_leader").value) || 0,
      q = parseInt(document.getElementById("eradication_6_leader").value) || 0,
      r = parseInt(document.getElementById("eradication_7_leader").value) || 0,
      s = parseInt(document.getElementById("prevention_1_leader").value) || 0,
      t = parseInt(document.getElementById("prevention_2_leader").value) || 0,
      w = parseInt(document.getElementById("prevention_3_leader").value) || 0,
      x = parseInt(document.getElementById("prevention_4_leader").value) || 0,
      y = parseInt(document.getElementById("prevention_5_leader").value) || 0,
      // Calculos Acreditacion
      longitud = 88;
      suma = a + b + c + d + e + f + g + h + i + j + k + l + ñ + o + p + q + r + s + t + w + x + y;
      porcentaje = suma * 100 / longitud;
      // Resultados
      document.getElementById("calificacion").value = porcentaje.toFixed(0);
      //document.getElementById("tiempo_maximo").value = (tiempo_maximo);
      //document.getElementById("tiempo_operativo").value = (display/maquina).toFixed(0);
      //document.getElementById("quality_loss_min").value = quality_loss.toFixed(0);
      //document.getElementById("ge").value = ((tiempo_operativo_ge) / tiempo_usado_ge * 100).toFixed(2);
      //document.getElementById("tiempo_usado").value = (resta_minutos);
    } catch (e) {}
  }
