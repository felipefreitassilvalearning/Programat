print("Eai Lucas, vou te ajudar com esse programa a calcular o preço da sua compra ")
print("="*40) #esse é um comando que printa 40 vezes o símbolo de igual no comando para fins estetéticos

#/////////preço individual dos produtos///////// 

precopao = float(input("Digite o preço do pão francês: R$ ")) #input de um float irá registrar um número com vírgulas registrado pelo usuário e passado ao computador

precorosquinha = float(input("Digite o preço da rosquinha (o desconto será aplicado automaticamente na soma total): R$ "))

precobolo = float(input("Digite o preço do bolo (o desconto será aplicado automaticamente na soma total): R$ "))

precobanana = float(input("Digite o preço da banana: R$ "))

precosucodelaranja = float(input("Digite o preço do suco de laranja: R$ "))

print("="*40)

#/////////preco com desconto dos doces/////////

precorosquinhadesconto = precorosquinha * 0.7 #cálculo do desconto de 30%. O desconto é aplicado multiplicando o valor total do produto por 0.7. Ou seja, 30% a menos que o total.

precobolodesconto = precobolo * 0.7

#/////////preco total dos produtos/////////

precopaototal = precopao * 5 #multiplicação do preço de cada produto pelo número de membros da família

precobananatotal = precobanana * 5 

precosucodelaranjatotal = precosucodelaranja* 5

precobolodescontototal = precobolodesconto * 5 #multiplicação do preço descontado de cada doce  pelo número de membros da família

precorosquinhadescontototal = precorosquinhadesconto * 5

#/////////demonstração do total a ser pago/////////

print(f"Preço pago total pelos pães: R${precopaototal}") #aqui temos um print formatado. Para isso, você deve colocar a letra f antes das aspas"" e colocar o que você quer 
# inserir no texto dentro das chaves{}. Dessa forma, ao invés de escrever "produto1" na mensagem, o programa vai escrever o que foi atribuído como produto 1 no código 


print(f"Preço pago total pelas rosquinhas: R${precorosquinhadescontototal}")

print(f"Preço pago total pelos bolos: R${precobolodescontototal}")

print(f"Preço pago total pelas bananas: R${precobananatotal}")

print(f"Preço pago total pelos sucos de laranja: R${precosucodelaranjatotal}")

print(f"Preço total da compra: R${precopaototal + precorosquinhadescontototal + precobolodescontototal + precobananatotal + precosucodelaranjatotal}")#aqui temos a soma de todos os valores 
#registrados dentro de um print formatado