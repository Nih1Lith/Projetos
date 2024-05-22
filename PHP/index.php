<?php
$idade = 18;
$pessoas = 2;
echo "Olá Mundo" . PHP_EOL;
echo "Idade igual a $idade.";

if ($idade >= 18){
    echo "Permitido, idade igual a $idade.".PHP_EOL;
} else if($idade < 18 && $pessoas > 1){
    echo "Idade igual a $idade e acompanhado, permitido.".PHP_EOL;
} else {
    echo "Negado, idade igual a $idade.".PHP_EOL;
}

$contador = 1;
while($contador <= 10){
    echo "$contador";
    $contador++;
}

for($num=1; $num<=20; $num++){
    echo "$num" .PHP_EOL;
}

$div = 0;
while($div <= 100){
    if($div%2 != 0){
        echo "$div".PHP_EOL;
    }
    $div++;
}

for($i = 1; $i <= 10; $i++){
    if($i%2 != 0){
        echo"$i".PHP_EOL;
    }
}

$tabuada = readline("Escolha um número: ");
$multi = 1;

while($multi <= 10){
    echo "$tabuada x $multi = ", "$tabuada" * "$multi".PHP_EOL;
    $multi++;
}

$peso = readline("Qual seu peso? ");
$altura = readline("Qual sua altura? ");
$imc = round($peso/($altura**2),2);
if($imc < 18.5){
    echo "IMC = $imc - Magreza";
} else if($imc <24.9){
    echo "IMC = $imc - Normal";
} else if($imc < 30){
    echo "IMC = $imc - Sobrepeso";
} else{
    echo "IMC = $imc - Obesidade";
}
