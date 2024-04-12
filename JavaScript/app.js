// let titulo = document.querySelector("h1");
// titulo.innerHTML = "Hora do Desafio!";

// let paragrafro = document.querySelector("p");
// paragrafro.innerHTML = "Escolha um número entre 1 e 10: ";

let listaNumerosSorteados = [];
let limiteNumeros = 100;
let numeroSecreto = gerarNumero();
let tentativas = 1;


function gerarNumero(){
    let numeroEscolhido = parseInt(Math.random() * limiteNumeros + 1);
    let quantidadeElementosLista = listaNumerosSorteados.length;
    if(quantidadeElementosLista == limiteNumeros){
        listaNumerosSorteados = [];
    }
    if(listaNumerosSorteados.includes(numeroEscolhido)){
        return gerarNumero();
    } else{
        listaNumerosSorteados.push(numeroEscolhido);
        console.log(listaNumerosSorteados);
        return numeroEscolhido;
    }
}

function exibirTexto(tag, texto){
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

function exibirMensagem(){
    exibirTexto("h1", "Hora do Desafio!");
    exibirTexto("p", "Escolha um número entre 1 e 10: ");
}

exibirMensagem();

function limparCampo(){
    chute = document.querySelector("input");
    chute.value = "";
}

function reiniciarJogo(){
    numeroSecreto = gerarNumero();
    limparCampo();
    tentativas = 1;
    exibirMensagem();
    document.getElementById("reiniciar").setAttribute("disabled", true);
}

function verificarChute(){
    let chute = document.querySelector("input").value;
    let palavraTentativa = tentativas > 1 ? "tentativas" : "tentativa";
    let frase = `Você descobriu o número secreto com ${tentativas} ${palavraTentativa}`
    if(chute == numeroSecreto){
        exibirTexto("h1", "Parabéns!");
        exibirTexto("p",frase);
        console.log("Você acertou!");
        document.getElementById("reiniciar").removeAttribute("disabled");
    } else if (chute > numeroSecreto){
        exibirTexto("p", "Seu chute é maior");
        console.log("Seu chute é maior");
        limparCampo();
    } else{
        exibirTexto("p", "Seu chute é menor");
        console.log("Seu chute é menor");
        limparCampo();
    }
    tentativas++
}
