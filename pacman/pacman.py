#Map = [Case]
#------Variables----------------------------------------------------
M = ["X",0]
V = ["  ",0]
R = ["o ",1]
P = ["P ",0]
F = ["F ",0]
F_R = ["F",1]

Map = [R, X, X,
 R, P, V,
  X, X, X]

x_P =
Y_P =
x_F =
y_F =
Win = " "
Score = 0
Path_F = ["z","q","s","d"]
Force = "F"
#------FONCTIONS--------------------------------------------------
def Afficher():
    for saute_ligne in range(50) :
            print()
    print("Score :", Score)
    print("-----Déplacez vous avec Z Q S D -----")
    print()
    for  i  in  range(13) :
            for  t  in  range(21) :
                print(Map[i][t], end='')
            print()
def spawn_F():
    y_F = Spawn_Fy
    x_F = Spawn_Fx
    Map[y_F][x_F] = F
    Afficher()


def go() :
    if Map[x][y][1] = 1:
        Map[y][x] = R
    else :
        Map[x][y] = V
    y = y2 , x = x2
    Map[y][x] = entity

def Test_Mouvement(entity,x,y,Direction) :
    if direction == "z" :
        y2 = y-1
        x2 = x
        if Map[y-1][x] != M
            Mouvement(entity,x,y,Direction)
    if direction == "s" :
        y2 = y+1
        x2 = x
    if direction == "q" :
        y2 = y
        x2 = x-1
    if direction == "d" :
        y2 = y+1
        x2 = x+1
def Mouvement(entity,x,y) :
    if entity = "P" :
            if Map[y2][x2] == V :
                go()
            if Map[y2][x2] == R :
                go(P)
                Map[y][x] = P
                Score += 1
            if Map[y2][x2] == F :
                if Force == "P"
                    if Map[y2][x2][1] == 1
                        go(P)
                        Map[y][x] = P
                        Score += 4
                    else :
                        go()
                        Map[y][x] = P
                        Score += 3
                if Force == "F"
                    Win= "no"
    if entity == "F" :
            if Map[y2][x2] == V :
                go(F)
            if Map[y2][x2] == R :
                go(F_R)
            if Map[y2][x2] == P :
                if Force == "P" :
                    if Map[y][x][1] == 1 :
                        Score +=4
                    if Map[y][x][1] == 0 :
                        Score +=3
                    spawn_F()
                if Force == "F" :
                    Win= "no"
#-----ALGO----------------------------------------------------------------
while Win== " " :
    Direction_P="no"
    Direction_P=input("zqsd")
    time.sleep(0.5)
    Afficher()
    if Direction_P != "no" :
        mouvement("P", P_x, P_y,Direction_P)
    Direction_F = random.choice(Path_F)
    mouvement("F", F_x, F_y,Direction_F)
    Afficher()
    if Score == Score_Max :
        Win = "yes"
if Win == "yes" :
    print("==================================")
    print("=============== GG ===============")
    print("==================================")
if Win == "no" :
    print("===================================")
    print("==============  GAME  =============")
    print("==============  OVER  =============")
    print("===================================")
