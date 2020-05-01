#Soma Infinita
print("Soma Infinita.")
print(10*"-=-")
num = 0
soma = 0

#manda o usuario digitar outro número ou zero para encerra o programa
while True:
    nume= int(input("Digite um numero intero [0 para terminar]:"))
    soma = soma + nume

    if nume==0:
        print(10*"-=-")
        print("Programa encerrado")
        print(10*"-=-")
        break
  
#idique o resultado ao usúario de cada número que ele digitar
    print("A soma foi: ", soma)

#Infelizmente não consegui fazer que o programa diga quem é o maior e quem é o menor 




