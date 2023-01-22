from time import sleep #biblioteca do python importada para inserir um delay no programa. Lembrado que 
                       #a biblioteca é o time e a função é o sleep. Então, basicamente, você importa a função
                       #sleep da biblioteca time; isso que o código está dizendo

print("Mensagem de Aniversário para o Bruno") #Nome do programa 

print("10,", end="") #Nesse caso, nós estamos printando os números da contagem regressiva descrescente de 10 até 0 
                     #Para cada elemento, iremos digitar o valor numérico correspondente, e adicionar a função end="",
                     #que delimita que as linhas de código não serão quebradas no console; as mensagens serão escritas umas 
                     #ao lado das outras, como se fosse uma mensagem contínua
sleep(1)#Esse é o comando sleep que importamos da biblioteca time que adiciona um delay de 1 segundo ao tempo em que 
        #a mensagem é escrita no console

print("9,", end="")
sleep(1)
print("8,", end="")
sleep(1)
print("7,", end="")
sleep(1)
print("6", end="")
sleep(1)
print("5,", end="")
sleep(1)
print("4,", end="")
sleep(1)
print("3,", end="")
sleep(1)
print("2,", end="")
sleep(1)
print("1,", end="")
sleep(1)
print("0,", end="")
sleep(1)

print("\n\033[33mPARABÉNS BRUNO!!!\033[33m")#Após o término da contagem regressiva, é printada na tela uma mensagem 
                                            #de parabéns para o Bruno.
                                            #Na mensagem, o \n faz a função de quebrar a linha, ou seja, escreve 
                                            #a mensagem que vem depois do \n em outra linha. 
                                            #Já o comando \033[33m é o comando de cor do python, através deste código 
                                            #é possível escrever uma mensagem de texto em várias cores e estilos.
                                            #Caso você queira ver mais opções de formatação, dê uma olhada na seção
                                            #de explicações do pyhton

#outra resolução 

print("Mensagem de Aniversário para o Bruno")

for n in range(0,11,-1): #Nessa outra solução, nós estabelecemos um loop limitado com o comando for, o qual 
                      #explicita que, entre os números 0 e 10, o programa irá contar de maneira regressiva,
                      #ou invertida (isso que significa o -1) de 10 até 0. Se você quer contar até 10, escreve-se 
                      #11, pois o python irá sempre cortar o último número. Além disso, o n é uma posição 
                      #"imaginária" criada pelo python, na qual os números da contagem regressiva assumem a posição n
                      #Por exemplo, a primeira posição do programa, para execução das funções pelos parâmetros que 
                      #passamos é o número 10, então nós vamos executar as linhas subsequentes nessa posição 10.
                      #Resumindo, a leitura deste for seria. Para cada posição númerica n dentro da contagem, faça 
                      #um print do número que está na posição em uma mesma linha e adicione um vírgula. Além disso
                      #espere 1 segundo entre cada execução

    print(n, end="") #Nesse caso, esse print mostra na tela o número x que está na posição n. Sendo assim, se a 
                     #posição n é um 1, o programa vai printar 10, já que a contagem é inversa.
    
    sleep(1) #delay adicionado para execução do programa

print("\033[33mPARABÉNS BRUNO!!!\033[33m") #print com cores fora da repetição for, que será executado somente uma 
                                           #vez depois da repetição ser concluída 


