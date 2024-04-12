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