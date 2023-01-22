from datetime import date #biblioteca do python importada para demonstrar o ano do seu computador 

print("="*40) #esse é um comando que printa 40 vezes o símbolo de igual no comando para fins estetéticos


print(f'{"PARDAL DA POLÍCIA FEDERAL":^40}') #Nesse caso, a formatação diferente dessa string se dá pois iremos colocar o texto centralizado em 40 caracteres, através do comando ":^40" -> 40 
                                            #é o número de caracteres / ^ é o símbolo que o texto "Calculadora do Louzada" ficará centralizado nos 40 caracteres

print("="*40)

#/////////Parametros para aplicação da multa/////////
print("Limite de velocidade: 70 km/h")
print ("Valor aplicado por km/h acima do limite: R$0.90")

print("="*40)

#/////////Valores a serem registrados na multa/////////

anoAtual = date.today().year #variável para indicar o ano atual. Ou seja, estamos chamando a função date.today que está na biblioteca datetime e irá mostrar o year (ano) atual

velocidadeLouzada = float(input("Digite a velocidade do carro do Louzada: ")) #registro

limitedevelocidade = 70 #parametro do limite de velocidade 

acimadoLimite = velocidadeLouzada - limitedevelocidade #calculo de quantos km/h o Louzada estava acima do limite 

#/////////Aspectos condicionais do código/////////

if velocidadeLouzada > 70: #nesse aspecto condicional, o código analisa a velocidade do Louzada, e, se ela for maior que 70, os prints referentes a aplicação da multa serão demonstrados na tela
                           #Veja que você precisa colocar depois dos elementos condicionais os dois pontos: 
    print("O meliante estava acima do limite de velocidade, iremos emitir uma multa")

    print(f'{"EMISSÃO DE MULTA":^40}')

    print(f"Ano de emissão: {anoAtual}") #demonstração do ano em que a multa foi emitida com base na variável que você havia criado e com base no ano do seu computador 

    print(f"Velocidade acima do limite: {acimadoLimite}km/h") #demonstração de quantos km/h a cima do limite Louzada estava

    print(f"Multa aplicada: R${acimadoLimite*0.9}") #cálculo da multa aplicada com base na multiplicação do valor por km/h acima do limite que você estabeleceu 

if velocidadeLouzada <= 70: #nesse aspecto condicional, o código analisa a velocidade do Louzada, e, se ela for menor ou igual a 70, os prints referentes a não aplicação da multa serão demonstrados na tela

    print(f"Sua velocidade era de {velocidadeLouzada}km/h. Então está liberado")




