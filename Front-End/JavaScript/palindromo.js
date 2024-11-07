//Function declaration, esse tipo de função aceita hoisting, ela pode ser chamado antes dela.
palindromo();
function palindromo(){
    let palavra = "rever";
    let separadorPalavra = palavra.split("");
    let palavraRevertida = separadorPalavra.reverse("");
    palavraRevertida = palavraRevertida.join("");
    if(palavra == palavraRevertida){
        alert("A palavra " + palavra + " é um palíndromo.");
    } else {
        alert(`A palavra ${palavra} não é um palíndromo.`)
    }
}

//Function expression, esse tipo de função só pode ser chamada após ela.
//Recebendo uma parâmetro vindo de fora da função.
const palindromo2 = function(palavra){
    let separadorPalavra = palavra.split("");
    let palavraRevertida = separadorPalavra.reverse("");
    palavraRevertida = palavraRevertida.join("");
    if(palavra == palavraRevertida){
        alert("A palavra " + palavra + " é um palíndromo.");
    } else {
        alert(`Função palindromo2: A palavra ${palavra} não é um palíndromo.`)
    }
}

palindromo2("radar");

function ordenadorDeNumeros(a, b, c){
    const numerosOrdenados = [a, b, c].sort((x, y) => x - y);
    console.log(`Números ordenados: ${numerosOrdenados.join(",")}`)
}

ordenadorDeNumeros(3, 1, 5);