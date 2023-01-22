print("Calculador da média ponderada de Pedrito")

print("Lembrando que, as notas vão de 0 a 10 e que Pedrito precisa de 6 para passar")

#/////////Cálculo da nota e do peso de cada trimestre/////////

nota1tri = float(input("Digite a nota do primeiro trimestre: "))  #input de um float irá registrar um número com vírgulas registrado pelo usuário e passado ao computador
peso1tri = float(input("Digite o peso do primeiro trimestre: "))  #não usamos int para registrar o peso de cada trimestre pois iríamos ter problemas de incompatibilidade na divisao dos valores float por int
 
nota2tri = float(input("Digite a nota do segundo trimestre: "))
peso2tri = float(input("Digite o peso do segundo trimestre: "))

nota3tri = float(input("Digite a nota do terceiro trimestre: "))
peso3tri = float(input("Digite o peso do terceiro trimestre: "))

#/////////Cálculo da média ponderada de Pedrito/////////

mediaPedrito = ((nota1tri * peso1tri) + (nota2tri * peso2tri) + (nota3tri * peso3tri)) / (peso1tri + peso2tri + peso3tri) #Neste cálculo, é importante lembrar de inserir os parenteses para 
#indicar a prioridade de cada cálculo

#/////////funções condicionais////////

if mediaPedrito >= 6: #nesse aspecto condicional, o código analisa a media de pedrito, e, se ela foi maior ou igual(simbolo representado por >=) a 6, o print de "parabéns" irá aparecer na tela
                      #Veja que você precisa colocar depois dos elementos condicionais os dois pontos: 
    
    print(f"Parabéns! Pedrito, você passou de ano com uma média de {mediaPedrito}") #este print precisa ser escrito clicando o comando shift antes. Para que ele seja formatado dentro da condição
                                                                                    #if. Ou seja, ele será um elemento dentro do comando condicional de if

else: #nesse caso, o programa irá analisar que qualquer coisa diferente do que está dentro de if será executado desta maneira. Ou seja, o "else" ou "senão"
    
    print(f"Desculpa Pedrito, mas você não passou pois sua média foi {mediaPedrito}")