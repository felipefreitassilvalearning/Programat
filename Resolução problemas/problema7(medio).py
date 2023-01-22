print("Resolvendo o Teorema de Pitágoras") #print do nome do código 

print("Teorema de Pitágoras: cateto oposto² + cateto adjacente ² = hipotenusa ²") #print do teorema de pitágoras. Para inserir o ², clique crtl + alt + 2 no teclado

print("Resolvendo o Teorema")

catetoOposto = float(input("Digite o valor do cateto oposto [em m]: ")) #atribuição do valor númerico ao cateto oposto em float, para, dessa forma, permitir valores virgulados.

catetoAdjacente = float(input("Digite o valor do cateto adjcente [em m]: ")) #atribuição do valor númerico ao cateto adjacente em float, para, dessa forma, permitir valores virgulados.

hipotenusaQuadrado = (catetoOposto**2) + (catetoAdjacente**2) #Cálculo do valor da hipotenusa elevado ao quadrado. Note que para elevar um número eao quadrado, precisamos inserir 2 astericos*

print(f"O valor da hipotenusa é {hipotenusaQuadrado**1/2}m") #Cálculo para demonstrar o valor da hipotenusa. Para isso, devemos calcular a raiz quadrada do quadrado da hipotenusa. Sendo assim,
                                                             #se elevarmos o quadrado da hipotenusa a 1/2, o denominador será o índice 2 da raiz quadrada