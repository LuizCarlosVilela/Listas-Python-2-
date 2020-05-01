sexo=0
Alt=0
nome=0
insc=0
somaaltM = 0
somaaltF = 0
altMA = 0
altMB = 0
AltF = 0
AltM = 0
somaM=0
somaF=0
inscr=0

#Pede todos os dados do candidato altura,nome, sexo e a inscrição

while True:
     insc = int(input("Digite o número da inscrição:"))
     nome = input("Nome: ")
     sexo = input("Sexo[M/F]: ")
     Alt= float(input("Qual é a altura do candidato?:"))            
     Cont=input("Quer continuar? [S/N]") #Pergunta se deseja continuar se aperta N o programa para

#Adiciona +1 para determinado sexo depedendo de qual vc escolheu para o candidato, e faz a soma para a média e para ver quem é o maioreo menor
     
     if sexo == 'M': 
          somaM +=1
          somaaltM = somaaltM + Alt
          AltM = somaaltM/somaM
     if sexo == 'F':
          somaF +=1
          somaaltF = somaaltF + Alt
          AltF = somaaltF/somaF

     if somaM + somaF==1:
          altMA, inscrMA = Alt,insc
          antMB, inscrMB = Alt,insc

     if Alt > altMA:
          altMA, inscrMA = Alt,insc
          
     if Alt <altMB:
          altMB, inscrMB = Alt,insc
          
#Quando for digitado N o programa vai dar todos os dados calculados e somados, e depois o programa ira encerrar



     if Cont == 'N':
          print(15*"-=-")
          print("Número de homens:",somaM)
          print("Altura média dos homens:",AltM)
          print("Número de mulheres:",somaF)
          print("Altura média das mulheres:",AltF)
          print("O número de inscrição do(a) candidato(a) mais alto(a) é:",inscrMA)
          print("O número de inscrição do(a) candidato(a) mais baixo(a) é:",inscrMB)
          print(7*"-=-")
          print("Programa encerrado")
          print(7*"-=-")     
          break
     
     
     
    
     
     







     


    


