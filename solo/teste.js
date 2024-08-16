for(let numero = 1; numero <= 100; numero++){
    if(numero%5 == 0){
        console.log(numero);
    }
}

let minhaLista = [];
minhaLista.push(1,2,3);
console.log('Adicionando elementos: ', minhaLista);
let segundaLista = [4,5,6];

let novaLista = segundaLista.concat(minhaLista).sort();
console.log("Array = ",novaLista);

novaLista.pop()
console.log("Pop = ", novaLista);

function embaralha(lista){
    for(let i = lista.length; i; i--){
        const indiceAleatorio = Math.floor(Math.random()*i);
        const elemento = lista[i-1];
        lista[i-1] = lista[indiceAleatorio];
        lista[indiceAleatorio] = elemento;
    }
    console.log("Algoritmo de Fisher-Yates(Knuth Shuffle) = ",lista);
}

embaralha(novaLista);

function removerDuplicatas(array){
    return [... new Set(array)];
}

let novaListaDuplicatas = removerDuplicatas(novaLista);
console.log("Remover duplicatas: ", novaListaDuplicatas);


function verificaNumero(num){
    if(num > 0){
        alert("O número " + num + " é positivo.");
    }else if(num < 0){
        alert(`O número ${num} é negativo.`);
    }else{
        alert(`O número é zero(${num})`)
    }
}

verificaNumero(0);

function verificaIdade(idade){
    if(idade >= 18){
        alert(`Idade de ${idade}, você é maior de idade.`);
    }else{
        alert(`Idade de ${idade}, você é menor de idade.`);
    }
}

function verificaString(frase){
    return texto === "" ? "String vazia." : `String não vazia: ${frase}`;
}

let frase = prompt("Digite uma frase: ");
verificaString(frase);

function verificaAno(ano){
    if(ano%4 == 0){
        alert("O ano é bissexto.")
    }else{
        alert("O ano não é bissexto.")
    }

}

verificaAno(1996);

console.log(Math.round(Math.random()*10));
let conjunto = [];
let contador = 0;
while (contador < 5){
    conjunto.push(Math.round(Math.random()*10));
    contador++;
}

function verificaArray(array){
    let tamanho = array.length;
    alert(`O array possui ${tamanho} elemento(s).\nE os elementos são: ${conjunto.sort()}`);
}

verificaArray(conjunto);

function incluso(array){
    if(array.includes(1)){
        alert("O conjunto possui o número 1.");
    }else{
        alert("O conjunto não possui o número 1.");
    }
}

incluso(conjunto);

function incluso2(array, elemento){
    if(array.includes(elemento)){
        alert(`O conjunto possui o elemento ${elemento}`);
    }else{
        alert(`O conjunto não possui o elemento ${elemento}`);
    }
}

incluso2(conjunto, 2);

let frutas = ["banana", "uva", "abacaxi", "tomate", "laranja", "acerola"];
if(frutas.includes("kiwi")){
    alert("Temos kiwi");
}else{
    alert("Não temos kiwi");
}

function verificaObjetoNoArray(arr, objeto){
    /*"JSON.strigify" método estático converte um valor JavaScript em uma string JSON, opcionalmente substituindo
    valores se uma função de substuição for especificada ou opcionalmente incluindo apenas as propriedades
    especificadas se uma matriz de substituição for especificada.*/
    //O método ".some()" testa se ao menos um dos elementos no array passa no teste implementado pela função atribuída e retorna true ou false.
    return arr.some(item => JSON.stringify(item) === JSON.stringify(objeto));
}

const alunos = [
    {id: 1, nome: "João", idade: 20},
    {id: 2, nome: "Maria", idade: 22},
    {id: 3, nome: "Pedro", idade: 21},
    {id: 4, nome: "Ana", idade: 19}
];

const alunoProcurado = {id: 2, nome: "Maria", idade: 22};
const objetoEstaPresente = verificaObjetoNoArray(aluno, alunoProcurado);

if(objetoEstaPresente){
    console.log("O aluno está presente no array.");
}else{
    console.log("O aluno não está presente no array.");
}

function calcularSomaProduto(array){
    let somaPares = 0;
    let produtoImpares = 1;

    for(let numero of array){
        if(numero % 2 === 0){
            somaPares += numero;
        }else{
            produtoImpares *= numero;
        }
    }
    return{
        somaPares,
        produtoImpares
    }
}

const numeros = [1,2,3,4,5];
const resultado = calcularSomaProduto(numeros);
console.log("Soma os pares: ", resultado.somaPares);
console.log("Produto soma dos ímpares: ", resultado.produtoImpares);
