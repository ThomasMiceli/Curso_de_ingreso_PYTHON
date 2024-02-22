function comenzarIngreso() {
    let numeros = [];
    let sumaNegativos = 0;
    let sumaPositivos = 0;
    let cantidadPositivos = 0;
    let cantidadNegativos = 0;
    let cantidadCeros = 0;

    while (true) {
        let numero = prompt("Ingrese un número (presione Cancelar para terminar)");

    if (numero === null) {
    break;
    }

    let numeroParseado = parseFloat(numero);

    if (isNaN(numeroParseado)) {
        alert("Error: Por favor ingrese un número válido");
        continue;
    }

    numeros.push(numeroParseado);

    if (numeroParseado < 0) {
        sumaNegativos += numeroParseado;
        cantidadNegativos++;
    } else if (numeroParseado > 0) {
        sumaPositivos += numeroParseado;
        cantidadPositivos++;
    } else {
        cantidadCeros++;
    }
    }

    let diferencia = cantidadPositivos - cantidadNegativos;

    alert("Resultados:\n\n" +
        "A. Suma acumulada de los negativos: " + sumaNegativos + "\n" +
        "B. Suma acumulada de los positivos: " + sumaPositivos + "\n" +
        "C. Cantidad de números positivos ingresados: " + cantidadPositivos + "\n" +
        "D. Cantidad de números negativos ingresados: " + cantidadNegativos + "\n" +
        "E. Cantidad de ceros: " + cantidadCeros + "\n" +
        "F. Diferencia entre la cantidad de los números positivos ingresados y los negativos: " + diferencia);