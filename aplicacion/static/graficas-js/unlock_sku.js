function success() {
  if (document.getElementById("maquina_sku").value === "") 
  {
    document.getElementById("linea_sku").disabled = true;
    document.getElementById("kg_sku").disabled = true;
    document.getElementById("ea_sku").disabled = true;
  } 
  else
  {
    document.getElementById("linea_sku").disabled = false;
    document.getElementById("kg_sku").disabled = false;
    document.getElementById("ea_sku").disabled = false;
  }
}
