alert("Boas Vindas ao Jogo de Advinhação");
let numeroMaximo = Math.random()*1000;
let numeroSecreto = parseInt(Math.random()*numeroMaximo + 1);
console.log(numeroSecreto);
let chute;
let tentativas = 1;
let palavraTentativa = tentativas > 1 ? "tentativas" : "tentativa";
let centena = numeroSecreto <= 100 ? "100" : numeroSecreto <= 500 ? "500" : "1000"; 

while (chute != numeroSecreto){
    chute = prompt(`Escolha um número entre 1 e ${centena}:`);
    if (chute == numeroSecreto) {
        alert(`Você descobriu o número secreto ${numeroSecreto} com ${tentativas} ${palavraTentativa}.`);
        break;
    } else {
        if(chute > numeroSecreto){
            alert(`Você Errou, ${chute} é maior que o número secreto`);
        } else {
            alert(`Você Errou, ${chute} é menor que o número secreto`);
        }
    }
    tentativas++
}
