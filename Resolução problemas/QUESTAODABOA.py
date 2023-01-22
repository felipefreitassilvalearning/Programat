print("Contador do número total de amigos e doces")

#/////////Registro das variáveis/////////

totaldoces = 0 #nesse caso, precisamos chamar a variável antes dela ser mencionada, pois, caso o contrário, o programa não irá aceitá-la. Por isso, devemos mencionar ela antes de ela 
               #ser executada em qualquer momento e atribuir um valor 0, que, no nosso código, não irá prejudicar o desenvolvimento do código

totalamigos = 0 

while True: #while é uma condição na qual o programa irá ficar executando linhas de código sem parar enquanto ela for verdadeira. Nesse caso, o programa irá executar as linhas até elas serem
            #falsas. Preste atenção que a formatação é similar ao comando if e for: os códigos subsequentes devem aparecer com shift e devemos inserir os dois pontos

    totaldoces = int(input("Quantos doces essa pessoa comeu: ")) #Nesse momento, você ira atribuir um novo valor ao total de doces. Sendo assim, a partir de agora, o total de doces será o valor 
                                                                 #que você digitou.
    
    totalamigos = totalamigos + 1 #O nome desta função é contador. Ela serve para realizar uma contagem dentro do código. Neste caso, a cada vez que você registrar novos doces, o programa 
                                  #adiciona mais uma pessoa a contagem, e soma esta pessoa ao total de pessoas
    
    totaldoces +=totaldoces # Neste caso, nós estamos atribuindo outra contagem ao programa. Se você adicionar mais doces, ele será somado ao total de doces prévios. A exemplo, se você disser 
                            #que alguém comeu 2 doces na primeira repetição deste while, este será o total de doces. Se, na segunda execução você disser que alguém comeu 3 doces, esses 3 doces 
                            #vão ser adicionados ao total de doces prévios 2 e você terá agora um total de 5 doces. 
    
    resposta = str(input("Você quer continuar a registrar pessoas [S/N]? ")).upper().strip() #Esta é uma estratégia utilizada nestes programas para limitar a atuação do while. Para isso, atribuímos
                                                                                             #uma variável de resposta, que registra um valor S ou N que será utilizado depois do while.
                                                                                             #No caso de .upper(), este comando faz com que os valores de texto digitados sempre sejam reescritos pelo computador
                                                                                             #em letras maiúsculas, para não termos alterações ou direneças nas respostas. Já .strip() corta todos os espaços 
                                                                                             #adicionais digitados pelo usuário
                                                                                           
    if resposta == "N": #Neste caso, nós temos uma função condicional if, que executa uma função de que, se a variável respostas for igual a N, a função while é quebrada, e o programa sai desta
                        #condição. Ou seja, o while passa a não ser mais True, então, como ele agora é falso, ele para de ser executado.
        
        break #break é a condição de quebra do while 

    if resposta == "S": #Neste caso, nós temos outro if, que, caso a resposta do usuário seja S, o while, ou seja, a função de contagem de doces, continuará a ser executada. E o programa permanecer 
                        #neste loop.
        
        continue #esse é o comando para a condição while continuar a ser executada
    
    else: #esta é uma condição adicional que colocamos para caso o usuário digite algo diferente de S ou N. Sendo assim, o código vai criar outro loop que passa a executar um "sub-código para tratar 
          #as respostas inválidas 

        while resposta not in "NS": #como tinha mencionado, essa é da resposta ser diferente de S ou N. Para isso dizemos que enquanto as respostas não estiverem (not in) dentro das possibilidades 
                                    #válidas, que são S e N, o programa irá executar algumas linhas específicas.

            print("Digite uma resposta válida!") #aqui o programa demonstra que a respota foi inválida 

            resposta = str(input("Você quer continuar a registrar pessoas [S/N]? ")).upper().strip() #nesta parte, o programa executa novamente a pergunta sobre a resposta do usuário, e confome a resposta
                                                                                                     #ele executa as linhas designadas, tal como ocorre nas partes anteriores do programa;

print("Programa encerrado") #essas são as funções executadas depois do programa sair do loop de while. Ou seja, se o while for quebrado, ele passa a executar estas funções. 

print(f"Total de pessoas registradas: {totalamigos}") #neste caso, temos o print do contador de amigos. Ou seja, o programa vai mostrar quantas amigos foram cadastrados 

print(f"Total de doces comidos: {totaldoces}") #neste caso, temos o print do contador de doces. Ou seja, o programa vai mostrar quantos doces foram cadastrados

