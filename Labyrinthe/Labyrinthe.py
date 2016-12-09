#Variables
Map = [["XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX"],
["XX","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","XX","FF","FF","XX"],
["XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","  ","  ","XX","  ","  ","XX"],
["XX","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","XX","  ","  ","XX"],
["XX","  ","  ","  ","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","  ","  ","XX","  ","  ","XX"],
["XX","  ","  ","  ","XX","  ","  ","  ","  ","  ","  ","  ","  ","  ","XX","  ","  ","XX","  ","  ","XX"],
["XX","  ","  ","  ","XX","  ","  ","  ","  ","XX","  ","  ","  ","  ","XX","  ","  ","XX","  ","  ","XX"],
["XX","  ","  ","  ","XX","  ","  ","  ","  ","XX","  ","  ","  ","  ","XX","  ","  ","XX","  ","  ","XX"],
["XX","  ","  ","  ","XX","  ","  ","  ","  ","XX","  ","  ","  ","  ","XX","  ","  ","  ","  ","  ","XX"],
["XX","  ","  ","  ","XX","  ","  ","  ","  ","XX","  ","  ","  ","  ","XX","  ","  ","XX","XX","XX","XX"],
["XX","  ","  ","  ","XX","  ","  ","  ","  ","XX","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","XX"],
["XX","  "," P","  ","XX","  ","  ","  ","  ","XX","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","XX"],
["XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX","XX"]]
y = 11
x = 2
fin = 0
#fonctions
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
