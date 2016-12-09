#Map = [Case]
import time
#------Variables----------------------------------------------------
M = ["XXX",0]
V = ["   ",0]
R = [" . ",1]
P = [" P ",0]
F = [" F ",0]
F_R = [" F ",1]
F_C = [" F ",3]
C = [" ° ", 3]

Map = [
[M,M,M,M,M,M,M,V,V,M,M,M,M,M,M,M,M],    #0
[M,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,M],    #1
[M,R,M,M,M,M,M,M,M,M,M,M,M,M,M,R,M],    #3
[M,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,M],    #4
[V,R,M,M,M,M,R,R,R,R,V,R,R,R,R,R,V],    #5
[V,R,M,R,R,R,R,R,M,M,V,M,M,R,R,R,V],    #6
[M,R,M,R,M,M,R,R,M,V,F,V,M,R,R,R,M],    #7
[M,R,M,R,C,M,R,R,M,M,M,M,M,R,R,R,M],    #8
[M,R,M,M,M,M,R,R,R,R,R,R,R,R,R,R,M],    #9
[M,R,R,R,R,R,R,R,R,R,M,M,M,M,M,M,M],    #10
[M,R,M,M,M,M,M,M,M,R,M,M,M,M,M,R,M],    #11
[M,R,M,M,M,M,M,M,M,R,M,M,R,R,R,R,M],    #12
[M,P,R,R,R,R,R,R,R,R,R,R,R,R,M,M,M],    #13
[M,M,M,M,M,R,R,R,R,R,R,M,M,M,M,M,M],    #14
[M,M,M,M,M,M,M,V,V,M,M,M,M,M,M,M,M],    #15
]


x_P = 1
Y_P =13
x_F = 10
y_F = 7
Spawn_Fy = y_F
Spawn_Fx = x_F
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
    for  i  in  range(14) :
            for  t  in  range(17) :
                print(Map[i][t][0], end='')
            print()
def Spawn_F() :
    y_F = Spawn_Fy
    x_F = Spawn_Fx
    Map[y_F][x_F] = F
    Afficher()
def Test_Mouvement(entity, x, y) :
    if direction == "z" :
        if y == 0 :
            Path = 13
        else :
            Path = -1
        y2 = y+Path
        x2 = x
    if direction == "s" :
        if y == 13 :
            Path = -13
        else :
            Path = 1
        y2 = y+Path
        x2 = x
    if direction == "q" :
        if y == 0 :
            Path = 16
        else :
            Path = -1
        y2 = y
        x2 = x+Path
    if direction == "d" :
        if y == 0 :
            Path = 16
        else :
            Path = 1
        y2 = y
        x2 = x+Path
def Mouvement(entity,x,y) :
    if entity == P :
            if Map[y2][x2] == V :
                go(P)
            if Map[y2][x2] == R :
                go(P)
                Score += 1
            if Map[y2][x2] == F :
                if Force == P :
                    if Map[y2][x2][1] == 1 :
                        go(P)
                        Score += 4
                        Spawn_F()
                    else :
                        go(P)
                        Score += 3
                if Force == F :
                    Win= "no"
            if Map[y2][x2] == C :
                go(C)
                Score += 5
    if entity == F :
            if Map[y2][x2] == V :
                go(F)
            if Map[y2][x2] == R :
                go(F_R)
            if Map[y2][x2] == C :
                go(F_C)
            if Map[y2][x2] == P :
                if Force == P :
                    if Map[y][x][1] == 1 :
                        Score +=4
                    if Map[y][x][1] == 0 :
                        Score +=3
                    Spawn_F()
                if Force == F :
                    Win= "no"
def go(entity) :
    if entity == P :
        Map[x][y] = V
        y = y2 , x = x2
        Map[y][x] = entity
    if entity == F :
        if Map[x][y][1] == 1 :
            Map[y][x] = R
            y = y2 , x = x2
            Map[y][x] = entity
        if Map[x][y][1] == 3 :
            Map[y][x] = C
            y = y2 , x = x2
            Map[y][x] = entity
        else :
            Map[y][x] = V
            y = y2 , x = x2
            Map[y][x] = entity
#-----ALGO----------------------------------------------------------------
while Win == " " :
#    Direction_P = "no"
#    Direction_P = input("z q s d ?")
    time.sleep(0.5)
    Afficher()
#    if Direction_P != "no" :
#        Test_Mouvement(P, x_P, y_P,)
#        if Map[y2][x2] != M :
#            Mouvement(P ,x_P ,y_P )
#    Direction_F = random.choice(Path_F)
#    Test_Mouvement(F, x_F, y_F)
    Afficher()
    if Score == Score_Max :
        Win = "yes"
if Win == "yes" :
    print("oooooooooooooooooooooooooooooooooo")
    print("ooooooooooooooo GG ooooooooooooooo")
    print("oooooooooooooooooooooooooooooooooo")
if Win == "no" :
    print("ooooooooooooooooooooooooooooooooooo")
    print("oooooooooooooo  GAME  ooooooooooooo")
    print("oooooooooooooo  OVER  ooooooooooooo")
    print("ooooooooooooooooooooooooooooooooooo")
