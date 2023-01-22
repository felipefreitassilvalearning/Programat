print(f'{"Pinturas do Paulo":^40}')  #Nesse caso, a formatação diferente dessa string se dá pois iremos colocar o texto centralizado em 40 caracteres, através do comando ":^40" -> 40 
                                     #é o número de caracteres / ^ é o símbolo que o texto "Calculadora do Louzada" ficará centralizado nos 40 caracteres

#/////////Parametros para a pintura e seu preço/////////

precoTinta = float(input('Preço por m² de tinta: ')) #Parametro a ser determinado pelo usuário do preço da tinta por m²

alturaParede = float(input('Digite a altura da parede [em m]: ')) #Parametro a ser determinado pelo usuário da altura da parede 

larguraParede = float(input('Digite a largura da parede [em m]: ')) #Parametro a ser determinado pelo usuário da largura da parede 

areaParede = alturaParede * larguraParede #cálculo da área da parede com base na altura e largura fornecidas 

precoPago = areaParede * precoTinta #calculo do preço a ser pago pelo serviço com base no preço da tinta multiplicado pela area total pintada 

print(f"Paulo pintou uma parede de {areaParede}m²") #demonstração da área pintada 

print(f'O custo da pintura foi de R${precoPago}') #demonstração do preço pago pelo serviço