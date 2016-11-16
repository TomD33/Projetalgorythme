Map = [0]*264
n = 0
while n <= 264:
    n <= 264
    if n >= 0 and n <= 22:
        Map[n] = "x"
    if n <= 22:
        Map[n] = "x"
    if n%23 == 0:
        Map[n] = "x"
    if n%22 == 0:
        Map[n] = "x"
    if n >= 242 and n >= 264:
        Map[n]= "x"
    n+=1

#possibilitées de deplacement
def deplacement() :
    int test
    xpos
    ypos
    if ypos == 0 or ypos == 10 or xpos == 20 xpos == 0 :
        mov = 10
    else mov = 1
    if deplacement==up) and (TABLEAU[xpos,ypos+mov]==test) :
        dep="y+"
        rep=true
    if (deplacement==down) and (TABLEAU[xpos,ypos-mov]==test) :
        dep="y-"
        rep=true
    if (deplacement==left) and (TABLEAU[xpos-mov,ypos]==test)
        dep="x+"
        rep=true
    if (deplacement==right) and (TABLEAU[xpos+mov,ypos]==test) :
        dep="x-"
        rep=true
    else:
        rep=false


def mouvement():
    ypos
    ent
        if rep is true:
            colones = lignes[ypos]
            xpos=liste.index(ent)
            colones[xpos]=
            if dep = "x+":
                xpos +=1
                colones[xpos]=ent
            if dep = "x-"
                xpos -= 1
                colones[xpos]=ent
            if dep = "y+"
                colones = lignes[ypos-1]
                colones[xpos]=ent
            if dep = "y-"
                colones = lignes[ypos+1]
                colones[xpos]=ent

def kill():

while state = "playing" :
#Move gohst
    dep_gohst = random.choice(['x+', 'x-', 'y+', 'y-'])
    deplacement(1,gohst_xpos,gohst_xpos)
    mouvement(gohst_xpos,gohst_xpos)

#Move player
    #test fantomes n3
    deplacement(3)
    if rep is true:
        if pacman == "invincible" :
            score += 100
            kill(gohst1)
        state="loose"
    #test déplacement n0
    deplacement(0)
    mouvement(0)
    #test bonbon
    deplacement(2) #bonbon
    mouvement(2) #bonbon

    )
