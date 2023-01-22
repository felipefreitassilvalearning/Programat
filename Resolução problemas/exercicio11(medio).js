var gastoJaneiro = 230;
var gastoFevereiro = 270;
var gastoMarco = 390;
var gastoAbril = 350;
var gastoMaio = 425;
var gastoJunho = 170;

var gastoTotal = gastoJaneiro + gastoFevereiro + gastoMarco + gastoAbril + gastoMaio + gastoJunho;

var gastoMedio = gastoTotal / 6; 

console.log("José gastou em Janeiro R$" + gastoJaneiro + 
            "\nJosé gastou em Fevereiro R$" + gastoFevereiro +
            "\nJosé gastou em Março R$" + gastoMarco +
            "\nJosé gastou em Abril R$" + gastoAbril +
            "\nJosé gastou em Maio R$" + gastoMaio +
            "\nJosé gastou em Junho R$" + gastoJunho +
            "\nO gasto médio de José nos 6 meses foi de R$" +gastoMedio)