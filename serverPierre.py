import socket
import random

# Mettre en ligne le server
s = socket.socket()
host = "127.0.0.1"
port = 8080
s.bind((host,port))

s.listen(5)

print("Serveur en ligne !")
print("Attente de la connexion d'un joueur....")

# Attendre la connexion du joueur et tour du client
c,addr = s.accept()
print "Connection de la machine ",addr
print("Vous etes le joueur 2. Attendez votre tour...")
coupRecu = c.recv(1024)
print("\n\nLe joueur 1 a fini ! A votre tour ! ")

# C'est le tour du joueur
choisi = raw_input("Entrez votre coup : ")
c.send(choisi)
c.close 

# Afficher la fin de la partie
print("\n\nFin de la partie !")
print("Le joueur 1 a jouer {}".format(coupRecu))
print("Vous avez jouer {}".format(choisi))
