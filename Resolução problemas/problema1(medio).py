print(f'{"Calculadora do Louzada":^40}') #Nesse caso, a formatação diferente dessa string se dá pois iremos colocar o texto centralizado em 40 caracteres, através do comando ":^40" -> 40 
                                         #é o número de caracteres / ^ é o símbolo que o texto "Calculadora do Louzada" ficará centralizado nos 40 caracteres

print("Olá, irei te ajudar a calcular o preço total de 3 produtos registrados. ")

print("="*40) #esse é um comando que printa 40 vezes o símbolo de igual no comando para fins estetéticos

#/////////cálculo do preço de cada produto e seus nomes/////////

produto1 = str(input("Digite qual é o primeiro produto: ")) #input de uma str irá registrar um texto registrado pelo usuário e passado ao computador 
preco1 = float(input("Digite o preço do primeiro produto: R$ ")) #input de um float irá registrar um número com vírgulas registrado pelo usuário e passado ao computador 

produto2 = str(input("Digite qual é o segundo produto: "))
preco2 = float(input("Digite o preço do segundo produto: R$ "))

produto3 = str(input("Digite qual é o terceiro produto: "))
preco3 = float(input("Digite o preço do terceiro produto: R$ "))

print("="*40) #esse é um comando que printa 40 vezes o símbolo de igual no comando para fins estetéticos

#/////////cálculo do valor total gasto/////////

precototal = preco1 + preco2 + preco3  

print(f"Os produtos digitados foram {produto1}, {produto2} e {produto3}.") #aqui temos um print formatado. Para isso, você deve colocar a letra f antes das aspas"" e colocar o que você quer 
                                                                           #inserir no texto dentro das chaves{}. Dessa forma, ao invés de escrever "produto1" na mensagem, o programa vai escrever o que foi atribuído como produto 1 no código 

print(f"O preço total dos produtos é R${precototal}") #aqui você printa o valor total que havia sido somado