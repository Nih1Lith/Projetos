console.log("Bem Vindo");
let nome = "Gabriel";
console.log("Olá, " + nome);
alert(`Olá ${nome}`);

let linguagemFavorita = prompt("Qual sua linguagem de programação favorita? ");

let valor1 = 5;
let valor2 = 4;
let resultado = valor1 + valor2;
console.log(`A soma de ${valor1} e ${valor2} é igual a ${resultado}.`);
let resultado2 = valor1 - valor2;
console.log(`A diferença entre ${valor1} e ${valor2} é igual a ${resultado2}`);

let idade = parseInt(prompt("Qual sua idade? ")) > 18 ? "maior de idade" : "menor de idade";
alert(idade);

let numero = parseInt(prompt("Digite um número: "));
if(numero > 0){
    alert("Número positivo");
} if(numero < 0){
    alert("Número negativo");
} else {
    alert("Número igual a 0");
}

let loop = 1;
while(loop <= 10){
    console.log(loop);
    loop += 1;
}

let nota = 9 > 7 ? "Aprovado" : "Reprovado";
console.log(nota);

console.log(Math.random());
console.log(Math.round(Math.random()*10));
console.log(Math.round(Math.random()*1000));
