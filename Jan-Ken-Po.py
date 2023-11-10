print("")
import random
pedra = 1
papel = 2
tesoura = 3
print("Vamos Jogar Jan-Ken-Po!")
print("")
print("Escolha o Número de Jogadores")
print("1 Player / 2 Players")
player = int(input())
print("")
if player == 1:
    print("Digite o Seu Nome")
    player1 = input()
    print("Selecione Seu Movimento")
    print("1-Pedra / 2-Papel / 3-Tesoura")
    user1 = int(input())
    user2 = random.randint(1,3)
    player2 = "CPU"
    print("")
else:
    print("Digite o Nome do Primeiro jogador")
    player1 = input()
    print("")
    print("Digite o Nome do Segundo jogador")
    player2 = input()
    print("")
    print(player1, "Selecione Seu Movimento")
    print("1-Pedra / 2-Papel / 3-Tesoura")
    user1 = int(input())
    print("\n" * 100)
    print(player2, "Selecione Seu Movimento")
    print("1-Pedra / 2-Papel / 3-Tesoura")
    user2 = int(input())
    print("")
if user1 == pedra:
    print(player1, "Escolheu Pedra")
else:
    if user1 == papel:
        print(player1, "Escolheu Papel")
    else:
        print(player1, "Escolheu Tesoura")
if user2 == pedra:
    print(player2, "Escolheu Pedra")
else:
    if user2 == papel:
        print(player2, "Escolheu Papel")
    else:
        print(player2, "Escolheu Tesoura")   
if (user1 - user2 == 0):
    victory= ("Ninguém")
    lose = ("Ninguém")
    winner = ("Ninguém")
else:
    if (user1 - user2> 0):
        if (user1 - user2 > 1):
            victory= ("Pedra")
            lose = ("Tesoura")
            winner = player2
        else:
            if (user1 - user2 - user2 == 0):
                victory= ("Papel")
                lose = ("Pedra")
                winner = player1
            else:
                victory= ("Tesoura")
                lose = ("Papel")
                winner = player1
    else:
        if (user1 - user2 < -1):
            victory = ("Pedra")
            lose = ("Tesoura")
            winner = player1
        else:
            if (user1 - user2 + user1 == 0):
                victory= ("Papel")
                lose = ("Pedra")
                winner = player2
            else:
                victory= ("Tesoura")
                lose = ("Papel")
                winner = player2
print("")
print (winner, "Ganhou")
print (victory, "ganha de", lose)
