from random import *			#Variables
V = ["   ","v"]
Ligne = [V]*10
Map = [Ligne]*10
fin = False
#Placement
#PORTE AVION -----------------------------------------------------------
def Placer_Pavion():
	Orientation = random.choice(["v","h"])
	if Orientation = "v"
		Pavion_Center_X = random.randint(0, 9)
		Pavion_Center_Y = random.randint(4, 9)
		Pavion = [Pavion_Center_X, Pavion_Center_Y, Pavion_Center_Y - 1, Pavion_Center_Y - 2, Pavion_Center_Y - 3 Pavion_Center_Y - 4 ]
	if Orientation = "h"
		Pavion_Center_X = random.randint(4, 9)
		Pavion_Center_Y = random.randint(0, 9)
		Pavion = [Pavion_Center_X, Pavion_Center_Y, Pavion_Center_X - 1, Pavion_Center_X - 2, Pavion_Center_X -3, Pavion_Center_X - 4 ]
	return Pavion
#SOUS MARINS ------------------------------------------------------------
def Placer_Smarin() :
	Orientation = random.choice(["v","h"])
	if Orientation = "v"
		Smarin_Center_X = random.randint(0, 9)
		Smarin_Center_Y = random.randint(2, 9)
		Smarin = [Smarin_Center_X, Smarin_Center_Y, Smarin_Center_Y - 1, Smarin_Center_Y -2]
	if Orientation = "h"
		Smarin_Center_X = random.randint(2, 9)
		Smarin_Center_Y = random.randint(0, 9)
		Smarin = [Smarin_Center_X, Smarin_Center_Y, Smarin_Center_X - 1, Smarin_Center_X -2
	return Smarin
#TORPILLEUR -----------------------------------------------------------*
def Placer_Torpilleur() :
	Orientation = random.choice(["v","h"])
	if Orientation = "v"
		Torpilleur_Center_X = random.randint(0, 9)
		Torpilleur_Center_Y = random.randint(1, 9)
		Torpilleur = [Torpilleur_Center_X, Torpilleur_Center_Y, Torpilleur_Center_Y - 1]
	if Orientation = "h"
		Torpilleur_Center_X = random.randint(1, 9)
		Torpilleur_Center_Y = random.randint(0, 9)
		Torpilleur = [Torpilleur_Center_X, Torpilleur_Center_Y, Torpilleur_Center_X - 1]
	return Torpilleur
#CROISEUR-----------------------------------------------------------*
def Placer_Croiseur() :
	Orientation = random.choice(["v","h"])
	if Orientation = "v"
		Croiseur_Center_X = random.randint(0, 9)
		Croiseur_Center_Y = random.randint(3, 9)
		Croiseur = [Croiseur_Center_X, Croiseur_Center_Y, Croiseur_Center_Y - 1, Croiseur_Center_Y -2, Croiseur_Center_Y -3]
	if Orientation = "h"
		Croiseur_Center_X = random.randint(3, 9)
		Croiseur_Center_Y = random.randint(0, 9)
		Croiseur = [Croiseur_Center_X, Croiseur_Center_Y, Croiseur_Center_X - 1, Croiseur_Center_X - 2, Croiseur_Center_X - 3]
	return Croiseur

def Placement():
	Placement_Valide = False
	Bateau[Placer_Pavion(), Placer_Smarin(), Placer_Smarin, Placer_Croiseur(), Placer_Torpilleur,]
	while Placement_Valide = False :
		for a in range(5) :
			for b in range(4)+1 :
				for i in range(6) :
					if Bateau [a][i] = Bateau[b][i] and if Bateau [a][0] = Bateau[b][0]
						 if b = 1 :
							 Bateau[1] = Placer_Smarin()
							 b -= 1
							 i -= 1

						 if b = 2 :
							 Bateau[2] = Placer_Smarin()
							 b -= 1
							 i -= 1
						 if b = 3 :
							 Bateau[1] = Placer_Croiseur()
							 b -= 1
							 i -= 1
						 if b = 4 :
							 Bateau[1] = Placer_Torpilleur()
							 b -= 1
							 i -= 1
		else :
			Placement_Valide = True

Map[y][x]








def Afficher() :
		for saute_ligne in range(50) :
			print()
		print("-----Déplacez vous avec Z Q S D -----")
		print()
		for  i  in  range(13) :
			for  t  in  range(21) :
				print(Map[i][t], end='')
			print()

while fin == 0  :
	Afficher()
	deplacement=input("z q s d ?")
	if deplacement == "z" :    #deplacement Z
		if Map[y-1][x] == "FF" :
			Map[y][x] = "  "
			y -= 1
			Map[y][x] = " P"
			fin = 1
			print("=================================================")
			print("=====================END=========================")
			print("=================================================")  #test fin
		if Map[y-1][x] == "  " :
			Map[y][x] = "  "
			y -= 1
			Map[y][x] = " P"
	if deplacement == "q" :    #deplacement Q
		if Map[y][x-1] == "  " :
			Map[y][x] = "  "
			x-=1
			Map[y][x]=" P"
	if deplacement == "s" :   #deplacement S
			if Map[y+1][x] == "  " :
				Map[y][x]="  "
				y+=1
				Map[y][x]=" P"
	if deplacement == "d" :    #deplacement D
			if Map[y][x+1] == "  " :
				Map[y][x]="  "
				x+=1
				Map[y][x]=" P"
	if deplacement == "end" :
		fin = 1
		print("Perdu")
