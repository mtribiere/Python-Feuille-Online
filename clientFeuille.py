import socket

s = socket.socket()
host = "127.0.0.1"
port = 80

# Connexion au serveur et tour du client
s.connect((host,port))
print("Connection au serveur reussi !")
print("Vous etes le joueur 1 ! C'est votre tour !")
choisi = input("Entrez votre coup : ")
s.send(bytes(choisi,'utf-8'))

# Attendre le coup du server
print("\n\nAttendez que le joueur 2 joue...")
coupRecu = s.recv(1024)
s.close()

# Afficher la fin de la partie
print("\n\nFin de la partie !")
print("Vous avez jouer {}".format(choisi))
print("Le joueur 2 a jouer {}".format(bytes.decode(coupRecu)))
s.close()
