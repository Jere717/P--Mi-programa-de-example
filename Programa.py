import random

numeroRandom = random.randint(27, 37)

print("La inteligencia artificial adivinira cuantos años viviras\n")

user = input("¿What is your name?\nTu nombre: ")
edad = int(input("¿How years old has?\nTu edad: "))
añosDeVida = edad + numeroRandom
colorFavorito = input("¿Cual es tu color favorito?\n Tu color favorito: ")
colorFavorito.lower()

coloresLegendarios = ["blue","azul",
                      "red","rojo",
                      "green","verde"]

if colorFavorito in coloresLegendarios:
    añosDeVida += 15

infoUser = (
    user,
    edad,
    colorFavorito,
)

añosDeVida = str(añosDeVida)
print("Datos que ingresaste: ","\n",infoUser[0],"\n",infoUser[1],"\n",infoUser[2])
print(infoUser)
print("La IA dice que viviras: "+añosDeVida+" años, disfrutalos, (:")