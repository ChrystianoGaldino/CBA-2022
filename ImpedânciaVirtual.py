'''

                                                XXIV Congresso Brasileiro de Automática (CBA 2022) 

Artigo: Utilização de um Simulador de Rede para Estudos de Integração de Geração Distribuída às Redes Elétricas	


CHRYSTIANO ALVES GALDINO

Mestrado em Eng.Elétrica 
Programa de Pós Graduação em Engenharia Elétrica - UFMG
Belo Horizonte - MG 


'''''

#Importar o módulo de socket do Python
import socket #modulo para conexão
import time   #módulo para usar tempo
import numpy as np #módulo para usar números float
import matplotlib.pyplot as plt  #para plotar gráficos
from drawnow import *
import math as math
import cmath
from math import floor
import csv   #módulo para usar arquivos CSV



#declaração de variáveis
plt.ion() # Informa ao matplolib que será utilizado o modo interativo para plotar os dados em tempo real

#variaveis de tempo
Tsimula = 120   # t em segundos de simulação
end_time = time.time() + Tsimula
countTimer = 0
sleepTime = 100*(10**(-6))  # passo de simulação  2 us (Esse valor interfere nos erros de transitório !) (10 tempo padrao , no lugar do 100)

# Estabilizar a conexão do socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #variável s com os parametros 
s.settimeout(20)   #valor original era 1, mudei para 10
s.connect(("192.168.0.149", 5025))        #endereço e porta de conexão

#Envio de comandos 

#clear da máquina
data6 = "*CLS\r\n"
s.send(data6.encode())

#limpar os dados de medição acumulados para o instrumento
data19 = "MEAS:RESET:ALL\r\n"
s.send(data19.encode())

#Ligar a saída
data1 = "SOUR:OUTP 1\r\n"
s.send(data1.encode())

#mudar a tensão para 220 v
data2 = "SOUR:VOLT: 220\r\n"
s.send(data2.encode())

# Utilizar arrays para medir tensão e correntes (senoidais)
#escolhe o instrumento 1 para medição
data5 = "INST:NSEL 1\r\n"
s.send(data5.encode())

#inicia uma nova sequencia de aquisição
data8 = "INIT\r\n"
s.send(data8.encode())


#Declaração da função para converter um vetor de strings em um vetor de float
def converte(vetor):
    #convertendo os dados de string unico para vários strings 
    aux = vetor.split(',')
    #converter a lista de strings para o tipo numpy
    array = np.array(aux)
    #converte a variavel array para uma lista de float
    vet_float = array.astype(float)
    #retorna o vetor convertido em um vetor de float
    return vet_float

#Declara a função que plota o gráfico
def makeFig():

    # Teste plot com várias figuras
    plt.subplot(511)
    plt.plot(vet,'r',label='tensão')
    plt.legend()
    plt.grid(True) #habilita o grid
    plt.autoscale #configura os eixos x e y automaticamente
    
    plt.subplot(512)
    plt.plot(vetC,'g--',label='corrente')
    plt.legend() #adiciona o conteudo de legenda declarado acima junto aos plots
    plt.grid(True) #habilita o grid
    plt.autoscale #configura os eixos x e y automaticamente

    plt.subplot(513)
    plt.plot(vetPF,'b-.',label='FP')
    plt.legend() #adiciona o conteudo de legenda declarado acima junto aos plots
    plt.grid(True) #habilita o grid
    plt.autoscale #configura os eixos x e y automaticamente
    #plt.title('Senoide 3') #título do gráfico

    plt.subplot(514)
    plt.plot(vetpot,'k',label='Potência Ativa')
    plt.legend()
    plt.grid(True) #habilita o grid
    plt.autoscale #configura os eixos x e y automaticamente
    #plt.title('Senoide 1') #título do gráfico

    plt.subplot(515)
    plt.plot(vetapp,'m',label='Potência Aparente')
    plt.legend()
    plt.grid(True) #habilita o grid
    plt.autoscale #configura os eixos x e y automaticamente
    #plt.title('Senoide 1') #título do gráfico
  

    plt.show()  #Mostra o grafico na tela

   
    

 

#Declara a função que realiza as mediçõeos
def medeV():
    #inicia uma nova sequencia de aquisição
    data8 = "INIT\r\n"
    s.send(data8.encode())

    #tensão senoidal da fase A
    data14 = "MEAS:VOLT?\r\n"
    s.send(data14.encode())
    dadosRecebidos14 = s.recv(2048)

    # Fase A
    #recebendo os dados do aparelho
    medidas = dadosRecebidos14.decode()
    return medidas


#Declara a função que realiza as medições de corrente
def medeC():
    #inicia uma nova sequencia de aquisição
    data8 = "INIT\r\n"
    s.send(data8.encode())

    #corrente senoidal 
    data14 = "MEAS:CURR?\r\n"
    s.send(data14.encode())
    dadosRecebidos14 = s.recv(2048)

    #recebendo os dados do aparelho
    medidas = dadosRecebidos14.decode()
    return medidas


def medPF():
    #inicia uma nova sequencia de aquisição
    data8 = "INIT\r\n"
    s.send(data8.encode())

    #mede o fator de potência
    data14 = "MEAS:PF?\r\n"
    s.send(data14.encode())
    dadosRecebidos14 = s.recv(2048)

    #recebendo os dados do PF
    fatorP = dadosRecebidos14.decode()
    return fatorP 

def medP():
    #inicia uma nova sequencia de aquisição
    data8 = "INIT\r\n"
    s.send(data8.encode())

    #mede potência ativa
    data14 = "MEAS:POW?\r\n"
    s.send(data14.encode())
    dadosRecebidos14 = s.recv(2048)

    #recebendo os dados do P
    Pativa = dadosRecebidos14.decode()
    return Pativa

def medS():
    #inicia uma nova sequencia de aquisição
    data8 = "INIT\r\n"
    s.send(data8.encode())

    #mede potência aparente
    data14 = "MEAS:POW:APP?\r\n"
    s.send(data14.encode())
    dadosRecebidos14 = s.recv(2048)

    #recebendo os dados do P aparente
    Papparent = dadosRecebidos14.decode()
    return Papparent



def medTempo():
    #inicia o tempo de  medição

    start = time.time() #retorna o tempo em segundos

    #efetua a leitura de um valor de tensão por meio função
    tensaoV = medeV()
    #correnteC = medeC()

    stop = time.time()

    #para o tempo de medição

    tempo = stop - start

    #retorna o tempo de execução 
    return tempo


#Definição das funções para utilizar a impedancia virtual

def pol2cart(raio,ang):

    #conversão para coordenadas cartesianas
    x = raio * math.cos(ang)
    y = raio * math.sin(ang)
    
    return x,y   # a função retorna uma tupla (forma de uma funçao retornar mais de um valor)

def cart2pol(x,y):

  #retorna a representação em coordenadas polares
  num = complex(x,y)

  #fase do numero complexo
  theta = cmath.phase(num)

  #módulo do número complexo
  mod = abs(num)

  return mod,theta   # a função retorna uma tupla (forma de uma funçao retornar mais de um valor)

def AngTheta(Fpot):  #implementar uma forma de saber se é capacitivo ou indutivo e armazenar em uma variavel
    if Fpot > 1:     #a maquina está apresentando FP = 1.0007 que é maior que 1 , da erro no acosseno.
     aux = floor(Fpot)      #arredonda para 1 se for maior que 1
     angulo = math.acos(aux)    #calcula o angulo em radianos
     #sinal = -1  # variável que vai retornar se o fp é indutivo (-1) ou capacitivo (1)
     #return angulo,sinal  # a função retorna uma tupla (forma de uma funçao retornar mais de um valor)
     return angulo
     

    angulo = math.acos(Fpot)
    #sinal = -1  # variável que vai retornar se o fp é indutivo (-1) ou capacitivo (1)
    #return angulo,sinal  # a função retorna uma tupla (forma de uma funçao retornar mais de um valor)
    return angulo

def Vsaida(Vc,thetaVC,V,I,FP,signal):

    #Variaveis

    f =60; #frequencia
    w = 2*math.pi*f;

    #Impedancia virtual
    Rs = 0.1;
    Ls = 100*(10**(-3));
   
   #Impedância virtual - Caso base
    #Rs = 0.1;
    #Ls = 0.001;

   #Impedância virtual - 5 x o Caso base
    #Rs = 0.5;
    #Ls = 0.005;

    #Impedância virtual - 10 x o Caso base
   # Rs = 1;
   # Ls = 0.01;

    #calculo do angulo entre V e I
    aux = AngTheta(FP)  # angulo em radianos sem o sinal pra ver se e capacitivo ou indutivo

    theta =  signal * aux;   #considerando o fator de potência detectado como capacitivo ou indutivo 

    #sinal para teste com fp Indutivo
    #theta =  - aux;   #considerando apenas o fator de potência indutivo, fazer o teste para ver se é capacitivo ou indutivo

    #sinal para teste com fp Capacitivo
   # theta =   aux;  #para fator de potência capacitivo

    #Componentes cartesianos dos valores
    Vx,Vy = pol2cart(V,theta);
    Ix,Iy = pol2cart(I,theta);
    
    #Componente real da tensão VF
    VFreal = Vc - Ix*Rs + w*Ls*Iy;

    #Componente imaginário da tensão VF
    VFimg = thetaVC - Ix*w*Ls - Iy*Rs;

    #Converter VF de cartesiano para polar
    VFmag,VFtheta = cart2pol(VFreal,VFimg);  #angulo em radianos

    return VFmag,VFtheta

def concatena(numerofloat):

 #converte o numero float em string de texto
 texto = str(numerofloat);

 #Soma de strings para formar o comando de tensão
 comando = "SOUR:VOLT: " + texto + "\r\n"

 #print(comando)
 return comando


#Declara a função ajusta o valor de Vc
def tensaoVC(V):
 #Tensão da rede   - tensão mais baixa para partir o motor
 vc = V;   #modulo de vc
 thetaVC = 0;  #fase 0
 ax1,ax2 = cart2pol(vc,thetaVC);  #angulo e modulo de VC

 VC = ax1/cmath.sqrt(2);
 ThetaVc = ax2/cmath.sqrt(2);
 return VC,ThetaVc


###Funções que medem V e I senoidais
def medeVsen():
    #inicia uma nova sequencia de aquisição
    data8 = "INIT\r\n"
    s.send(data8.encode())

    #tensão senoidal da fase A
    data14 = "FETC:ARR:VOLT?\r\n"
    s.send(data14.encode())
    dadosRecebidos14 = s.recv(2048)

    # Fase A
    #recebendo os dados do aparelho
    Vsen = dadosRecebidos14.decode()
    return Vsen

#Declara a função que realiza as medições de corrente
def medeCsen():
    #inicia uma nova sequencia de aquisição
    data8 = "INIT\r\n"
    s.send(data8.encode())

    #corrente senoidal 
    data14 = "FETC:ARR:CURR?\r\n"
    s.send(data14.encode())
    dadosRecebidos14 = s.recv(2048)

    #recebendo os dados do aparelho
    Csen = dadosRecebidos14.decode()
    return Csen

#Função que armazena o sinal do fator de potência (ind ou cap)

def sinalFP(vetV,vetC):
    
    #converte para tipo list

    c = converte(vetC)
    v = converte(vetV)

    corr = c.ravel().tolist()
    tens = v.ravel().tolist()

    ##print(corr)
    ##print(tens)

    #Encontra os valores de pico das senoides
    max_C = max(corr)
    max_V = max(tens)

    index_C = corr.index(max_C)
    index_V = tens.index(max_V)

   #Verifica se FP esta atrasado ou adiantado
    if (index_C>index_V):
       sinal = -1   #FP indutivo corrente atrasada
    else:
     if (index_C<index_V):
          sinal = 1   #FP capacitivo corrente adiantada 

     else:

      sinal = 1    #FP unitário, o angulo é zero

    return sinal


def moving_average(a, n) :     #Função cálculo da média móvel
    tamanho = len(a)
    if tamanho<n:  # se o vetor não tiver o numero de elementos igual a janela da media movel, igual a janela ao tam do vetor
      n=tamanho
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


#variaveis usadas no Loop de medição
aux=0
cont = 0
vet = []   #Vetor com valores de tensão
vetC = []  #Vetor com valores de corrente
vetPF = []  #Vetor com valores do fator de potência
vetpot = [] #Vetor com valores de potência ativa
vetapp = [] #Vetor com valores de potência aparente
plt.ion()

#Variaveis para o uso com a impedancia virtual

#Tensão da rede
vc = 220;   #modulo 100 v
VC,ThetaVc = tensaoVC(vc)


##Leitura de dados do teclado
valor_lido = 'n';
while valor_lido != 's':    #Mantem a tensão do simulador de rede constante até que a impedancia seja ligada

 valor_lido = input("Digite s para ligar a Impedância Virtual: ")

#inicia o tempo de  medição
start = time.time() #retorna o tempo em segundos


####################### Leitura de arquivos CSV ##########################################
#cria o arquivo
f = open('arquivo_de_dados.csv', 'w', newline='', encoding='utf-8')

#cria o objeto de gravação
w = csv.writer(f)

while True:  

    while time.time() < end_time:


        #leitura de tensão por meio de função
        medidas = medeV()

        #leitura da corrente por meio de função
        medC = medeC()

        #leitura do fator de potência
        fpot = medPF()

        #leitura da potência ativa
        pativa = medP()

        #leitura da potência aparente
        paparente = medS()


        #obtendo o vetor de float por meio da função - corrente
        medidasC = converte(medC)

        #obtendo o vetor de float por meio da função - tensão
        medidasA = converte(medidas)

        #obtendo o vetor de float por meio da função - fator de potência
        fatorP = converte(fpot)

        #obtendo o vetor de float por meio da função - potência ativa
        Pa = converte(pativa)

        #obtendo o vetor de float por meio da função - potência aparente
        Ps = converte(paparente)


        #carrega o vetor com os valores lidos
        vet.append(medidasA)
        vetC.append(medidasC)
        vetPF.append(fatorP)
        vetpot.append(Pa)
        vetapp.append(Ps)

     ##################################################################################################################
       #verifica o sinal do fator de potência
      
        #leitura de tensão por meio de função
        vetorVsen = medeVsen()

        #leitura da corrente por meio de função
        vetorCsen = medeCsen()
      
        #função que calcula o sinal do FP
        #sinal = sinalFP(vetorVsen,vetorCsen)

        sinal = -1   # considerando o FP Indutivo

        #sinal = 1   # considerando o FP Capacitivo


        ################Filtro média móvel ###################
        MM = 8 #coeficiente do filtro média móvel

        Vtensao = moving_average(vet,MM)
        Vcorrente = moving_average(vetC,MM)
        VfatorP = moving_average(vetPF,MM)
        Vpot = moving_average(vetpot,MM)
        Vapp = moving_average(vetapp,MM)

       
        ############################################################################
       #calculo de VF por meio de função
        modVF,angVF = Vsaida(VC,ThetaVc,Vtensao[-1],Vcorrente[-1],VfatorP[-1],sinal)  #o indice -1 pega o ultimo elemento da lista


        ax =(angVF *180) /math.pi  #angulo em graus 
        print('Valor de tensão para ser aplicado no simulador de rede:  Modulo = %0.2f, Ângulo em graus= %0.3f' %(modVF,ax))
        print('Tensão de pico (V):  Modulo = %0.2f' %(math.sqrt(2)*modVF))
        print('Corrente (A) = %0.3f' %(medidasC[0]))
        print('Potência ativa (w) = %0.3f' %(Pa[0]))
        print('Potência aparente (VA) = %0.3f' %(Ps[0]))
        print('Sinal do FP = ',sinal)

        #Utilizar o valor de VF no simulador de rede

        #converte o VF para valor de pico (multiplica por raiz de 2)
        VFaux = math.sqrt(2)*modVF; 
        VF = round(VFaux,3);    #arredonda para 3 casas decimais

        
       ######### Escreve os valores no arquivo CSV ###################
       # dados no arquivo: (contador,modulo de Vf, angulo de Vf, Vf de pico, tensão, corrente,fator de potência, potencia ativa, potencia aparente)     

      #escreve no arquivo marcando o tempo
        stop = time.time()
        tempo = stop  - start #retorna o tempo em segundos
        w.writerow([tempo,modVF, angVF, VF, medidasA[0], medidasC[0], fatorP[0], Pa[0], Ps[0]])


        #cria o comando de tensão em string
        ComandoVF = concatena(VF)

        #mudar a tensão para o valor de VF 
        #data2 = "SOUR:VOLT: 100\r\n"
        data2 = ComandoVF

        #proteção contra tensões extremas  
        #if(VF>250):
          #  data2 = '250'
           # s.send(data2.encode()) 
      #  elif (VF< 200):
      #      data2 = '200'
       #     s.send(data2.encode()) 
      #  else: 
            
        s.send(data2.encode())   #envia o valor calculado de VF para o Simulador de REDE

        #if(cont>50):
        if(cont>40):
            
            #Remove o elemento na posição zero para liberar memória
            vet.pop(0)
            vetC.pop(0)
            vetPF.pop(0)
            vetpot.pop(0)
            vetapp.pop(0)
            

        #plote do gráfico
        drawnow(makeFig)   # chama a função drawnow para atualizar o gráfico em tempo real
        plt.pause(.0000005)


        cont = cont + 1
        aux = aux + 1
        countTimer += sleepTime #incrementa o tempo de simulação

        
    ######### Fecha o arquivo CSV ###################
    #w.close()
    f.close()

    #limpar os dados de medição acumulados para o instrumento
    data19 = "MEAS:RES\r\n"
    s.send(data19.encode())

    #para o tempo de medição
    stop = time.time()

    #mudar a tensão para 220 v antes de desligar a impedancia virtual
    data2 = "SOUR:VOLT: 220\r\n"
    s.send(data2.encode())
        
    break   # termina o loop infinito


        


