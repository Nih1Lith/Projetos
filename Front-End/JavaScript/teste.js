let listaGenerica = [];
let linguagensDeProgramacao = ["JavaScript", "C", "C++", "Kotlin", "Python"];
linguagensDeProgramacao.push["Java", "Ruby", "GoLang"];
console.log(linguagensDeProgramacao);
console.log(linguagensDeProgramacao[0]);
console.log(linguagensDeProgramacao[1]);
console.log(linguagensDeProgramacao[-1]);

let senhaDoSistema = "senhaTeste";
let senha = prompt("Digite a senha: ");
if(senha == senhaDoSistema){
    alert("Acesso Permitido");
} else {
    alert("Acesso Negado")
}

function media(){
    let num1 = parseInt(prompt("Função média\nDigite um número: "));
    let num2 = parseInt(prompt("Função média\nDigite outro número: "));
    let num3 = parseInt(prompt("Função média\nDigite o último número: "));
    let media = (num1 + num2 + num3)/3;
    return media.toFixed(2);
}

function maiorNum(){
    let num1 = parseInt(prompt("Função maiorNum\nDigite um número: "));
    let num2 = parseInt(prompt("Função maiorNum\nDigite outro número: "));
    if(num1 > num2){
        return num1;
    } else{
        return num2;
    }
}

function calcularIMC(peso, altura){
    let imc = peso/(altura**2);
    return console.log(imc < 18.5 ? "IMC: Abaixo do peso" : imc > 24.9  ? "IMC: Sobrepeso" : "IMC: Normal" );
}

let peso = 60;
let altura = 1.78;

calcularIMC(peso, altura);

function fatoracao(num1, num2){
    let calculo = num1/num2;
    return console.log(`O resultado da fatoração é ${calculo.toFixed(2)}`);
}

fatoracao(5,9);

function perimetroArea(altura, lado){
    console.log(`A área do retângulo é ${altura*lado} e o perímetro é ${altura+lado}`);
}

perimetroArea(10,8);

function circulo(raio){
    console.log(`A área do circulo é ${3.14**(2)*raio} e o perímetro é ${2*3.14*raio}`)
}

circulo(4);

function tabuada(num){
    num2 = 0;
    while(num2<=10){
        console.log(`${num} x ${num2} = ${num*num2}`);
        num2++;
    }
}

tabuada(2);

function tabuada2(num){
    for(num2 = 0; num2 <= 10; num2++){
        console.log(`${num} x ${num2} = ${num*num2}`);
    }
}

tabuada2(3);

function conversao(){
    let escolha = prompt("Conversão para dólar ou real");
    let valor = parseInt(prompt("Digite um valor: "));
    let conversaoDolar = (valor/5.0042);
    let conversaoReal = (valor*0.1998);
    if(escolha == "real"){
        return console.log(`O valor em reais é: R$${conversaoDolar.toFixed(2)}`);
    } else{
        return console.log(`O valor em dólar é: $${conversaoReal.toFixed(2)}`);
    }
}
conversao();

function calcularMedia(nota1, nota2, nota3, nota4){
    let media = (nota1 + nota2 + nota3 + nota4)/4;
    return media;
}

let nota1 = 7;
let nota2 = 6;
let nota3 = 3;
let nota4 = 5;

calcularMedia(nota1, nota2, nota3, nota4);

function verificarAprovacao(media){
    return console.log(media >= 5 ? "Aprovado" : "Reprovado");
}

verificarAprovacao(calcularMedia());

function num(){
    let numero = parseInt(prompt("Função num\nDigite um número: "));
    return numero*numero;
}

function saudacao(nome, numero){
    console.log(`Olá ${nome}`);
    console.log(numero*2);
    console.log(media());
    console.log(maiorNum());
    console.log(num());
}

saudacao("Gabriel", 3);


function alerta(){
    console.log("Eu amo JS");
}

function cidade(){
    cidade = prompt("Digite o nome de uma cidade: ");
    console.log(`Estive em ${cidade} e lembrei de você.`);
}

function soma(){
    num1 = parseInt(prompt("Digite um número: "));
    num2 = parseInt(prompt("Digite outro número: "));
    console.log(`A soma de ${num1} e ${num2} é ${num1 + num2}`);
}
