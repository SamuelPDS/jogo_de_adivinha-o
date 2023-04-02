from random import randint
from time import sleep

num = randint(0, 5)
#print(num)
print("~~"*10)
jogador = int(input("Tente adivinhar o número de 0 a 5 que o computador gerou: "))
print("Processando...")
sleep(2)
if jogador == num:
    print("Parabéns! Você adivinhou o numero")
else:
    print("Incorreto, tente novamente. Foi escolhido o {}".format(num))
print("~~"*10)


