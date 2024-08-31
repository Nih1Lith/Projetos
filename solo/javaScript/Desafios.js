function stringConverter(palavra){
    //let conversor = parseInt(palavra);
    //alert(conversor)
    return parseInt(palavra);
}

function calculadora(){
    alert("executando função");
    let escolha = parseInt(prompt("Digite 1 para soma: \nDigite 2 para subtração: \nDigite 3 para multiplicação: \nDigite 4 para divisão: "));
    let x = parseInt(prompt("Digite o primeiro número: "));
    let y = parseInt(prompt("Digite o segundo número: "));
    if(escolha == 1){
        let soma = x+y;
        alert(soma);
    } else if(escolha == 2){
        let sub = x-y;
        alert(sub);
    } else if(escolha == 3){
        let multi = x*y;
        alert(multi);
    } else if(escolha == 4){
        let div = x/y;
        alert(div);
    } else{
        alert("Opção inválida");
    }
}

function parImpar(x){
    if(x%2 == 0){
        alert(`O número ${x} é par.`);
    } else{
        alert(`O número ${x} é ímpar.`);
    }
}

function conversorTemp(){
    let escala = parseInt(prompt("Digite 1 para converter para Fahrenheit:\n Digite 2 para converter para Celsius: "));
    let temp = parseInt(prompt("Digite a temperatura: "));
    let converter = 0;

    if(escala == 1){
        converter = ((temp*9)+(5*32))/5;
        alert(`A tempereratura é: ${converter.toFixed(1)}Fº`);
    } else if(escala == 2){
        converter = ((temp-32)*5)/9;
        alert(`A tempereratura é: ${converter.toFixed(1)}Cº`);
    } else{
        alert("Digite uma opção válida.");
    }
}

conversorTemp();