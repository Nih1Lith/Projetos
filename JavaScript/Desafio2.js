let DiaDaSemana = prompt("Qual o dia da semana? ");
if (DiaDaSemana == "sabado" && "domingo"){
    alert("Bom Fim de Semana!");
} else {
    alert("Boa Semana!");
}

let numero = prompt("Digite um número: ");
if(numero < 0){
    alert("Número Negativo");
}

let pontuacao1 = 105;
if(pontuacao1 >= 100){
    console.log("Voce ganhou");
} else {
    console.log("Voce perdeu");
}

// Consertar
let numeroSecreto = 5;
let pontuacao = 0;
let chute
while(pontuacao < 100){
    chute = prompt("Digite um número: ");
    console.log(numeroSecreto);
    if(chute == numeroSecreto){
        pontuacao += 50
        alert("Parabéns, sua pontuação atual é," + pontuacao);
    } else{
        pontuacao -= 2;
        alert("Você errou, sua pontuação é, " + pontuacao);
        continue;
    }
    break;
    alert("Fim de Jogo" + pontuacao);
}


let nome = prompt("Digite seu nome");
alert(`Bem vindo, ${nome}`);
