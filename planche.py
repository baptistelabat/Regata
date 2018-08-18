# -*- coding: cp1252 -*-

###################################
#                                 #
#  Programme : Jeu du serpent     #
#  Auteur : Baptiste              #
#  Date de creation : 19/05/07    #
#                                 #
###################################

# Importations des fonctions necessaires

from Tkinter import *
from random import randrange
from math import *

# Declarations des fonctions

# Cette fonction permet de reinitialiser le jeu

def new_game():
    global dx,dy,flag,planche1,planche2,coord_planche1,coord_planche2,score,f,flag2,angle1,angle2,vent,Cx

    flag2=0
    
    can1.delete(ALL)

    can1.create_rectangle(0,0,10,600,fill="black")
    can1.create_rectangle(0,0,800,10,fill="black")
    can1.create_rectangle(790,0,800,600,fill="black")
    can1.create_rectangle(0,600,800,590,fill="black")
    
    x=400
    y=100
    yb=500
    f=can1.create_oval(x,y,x+10,y+10,fill="black")
    can1.create_oval(x,yb,x+10,yb+10,fill="black")

    longueur=20
    coord_planche1=[450,500]
    coord_planche2=[350,500]
    angle1=-pi/4
    angle2=-pi/4
    
    couleur=['white','light green','green','light yellow','yellow','orange','red','red','purple','#ee00dd']
    vent=[]
    print vent
    vent.append(10)
    i=0
    j=0
    while j<=60:
      while i<=80:
        if vent[i]+randrange(3)-1>6:
          if vent[i]+randrange(3)-1<13:
            vent.append(vent[i]+randrange(3)-1)
          else :
            vent.append(14-randrange(2))
        else :
          vent.append(5+randrange(2))

    
      can1.create_rectangle(i*10,j*10,(i+1)*10,(j+1)*10,fill=couleur[vent[i+j*80]-5], outline=couleur[vent[i+j*80]-5])
      i=i+1
    i=0
    print vent
    j=j+1

   
    planche1=can1.create_line(coord_planche1[0]+longueur*sin(angle1),coord_planche1[1]+longueur*cos(angle1),coord_planche1[0]-longueur*sin(angle1),coord_planche1[1]-longueur*cos(angle1),width=15,fill='red')
    planche2=can1.create_line(coord_planche2[0]+longueur*sin(angle2),coord_planche2[1]+longueur*cos(angle2),coord_planche2[0]-longueur*sin(angle2),coord_planche2[1]-longueur*cos(angle2),width=15)
    voile1=can1.create_line(coord_planche1[0],coord_planche1[1],coord_planche1[0]+longueur*sin(angle1/2.0),coord_planche1[1]+longueur*cos(angle1/2.0),width=3)
    voile2=can1.create_line(coord_planche2[0],coord_planche2[1],coord_planche2[0]+longueur*sin(angle2/2.0),coord_planche2[1]+longueur*cos(angle2/2.0),width=3)

   
    dy1=cos(angle1)
    dx1=sin(angle1)
    dy2=cos(angle2)
    dx2=sin(angle2)
   
    vitesse1=abs(sin(angle1/1.5))*vent[int(coord_planche1[0]/10)+int(coord_planche1[1]/10)*80]*Cx
    vitesse2=abs(sin(angle2/1.5))*vent[int(coord_planche2[0]/10)+int(coord_planche2[1]/10)*80]*Cx
   
    score=0
    flag2=0
    
    if flag==0:
        flag=1
        print flag
        move()

    
    
# Cette fonction permet d'effectuer une pause en cours de partie

def pause(event):
    global flag,pause,flag2
    if flag2!=1:
        if flag==1:
            pause=can1.create_text(250,150,font=('Fixedsys',18),text="PAUSE")
            flag=0
        elif flag==0:
            flag=1
            can1.delete(pause)
            move()
      

# Cette fonction va permettre de mettre le serpent en mouvement de mani‚àö¬Ære automatique

def move():
    global dx1,dy1,dx2,dy2,flag,f,planche1,planche2,coord_planche1,coord_planche2,score,flag2,angle1,angle2,vitesse1,vitesse2,vent,Cx

    finertie=0.6
    # On fait avancer la planche 1
    
    angle1=(angle1+pi)%(2*pi)-pi
    vitesse1=finertie*vitesse1+abs(sin(angle1/1.5))*vent[int(coord_planche1[0]/10)+int(coord_planche1[1]/10)*80]*Cx
    coord_planche1[0]=coord_planche1[0]-vitesse1*dx1
    coord_planche1[1]=coord_planche1[1]-vitesse1*dy1

    # On fait avancer la planche 2
    angle2=(angle2+pi)%(2*pi)-pi
    vitesse2=finertie*vitesse2+abs(sin(angle2/1.5))*vent[int(coord_planche2[0]/10)+int(coord_planche2[1]/10)*80]*Cx
    coord_planche2[0]=coord_planche2[0]-vitesse2*dx2
    coord_planche2[1]=coord_planche2[1]-vitesse2*dy2
    


    # Si la planche touche le mur la partie s'arrete

    if coord_planche1[0]>=790 or coord_planche1[0]<=0 or coord_planche1[1]>=590 or coord_planche1[1]<=0 or coord_planche2[0]>=790 or coord_planche2[0]<=0 or coord_planche2[1]>=590 or coord_planche2[1]<=0:
        flag=0
        flag2=1
        perdu=can1.create_text(250,150,font=('Fixedsys',18),text="Score : "+str(score))

    can1.coords(planche1,coord_planche1[0]+longueur*sin(angle1),coord_planche1[1]+longueur*cos(angle1),coord_planche1[0]-longueur*sin(angle1),coord_planche1[1]-longueur*cos(angle1))

    can1.coords(planche2,coord_planche2[0]+longueur*sin(angle2),coord_planche2[1]+longueur*cos(angle2),coord_planche2[0]-longueur*sin(angle2),coord_planche2[1]-longueur*cos(angle2))

    can1.coords(voile1,coord_planche1[0],coord_planche1[1],coord_planche1[0]+longueur*sin(angle1/2.0),coord_planche1[1]+longueur*cos(angle1/2.0))
    can1.coords(voile2,coord_planche2[0],coord_planche2[1],coord_planche2[0]+longueur*sin(angle2/2.0),coord_planche2[1]+longueur*cos(angle2/2.0))
    
    if flag>0:
        fen1.after(50,move)
        
# Ces fonction vont permettrent de controler la planche
# a l'aide des touches flechees du clavier
inertie=0.3
def left(event):
    global dx1,dy1,angle1,inertie
    angle1=angle1+0.08
    dx1=inertie*dx1+sin(angle1)
    dy1=inertie*dy1+cos(angle1)
        
def right(event):
    global dx1,dy1,angle1,inertie
    angle1=angle1-0.08
    dx1=inertie*dx1+sin(angle1)
    dy1=inertie*dy1+cos(angle1)

def gauche(event):
    global dx2,dy2,angle2,inertie
    angle2=angle2+0.08
    dx2=inertie*dx2+sin(angle2)
    dy2=inertie*dy2+cos(angle2)

def droite(event):
    global dx2,dy2,angle2,inertie
    angle2=angle2-0.08
    dx2=inertie*dx2+sin(angle2)
    dy2=inertie*dy2+cos(angle2)
    
     
# Programme principal

# Definition du canevas (espace de jeu)

fen1=Tk()
fen1.title("FUN")
can1=Canvas(fen1,width=800,height=600,bg="light blue")

# Definition des touches qui permettront de deplacer la planche

can1.bind_all("<Left>",left)
can1.bind_all("<Right>",right)
can1.bind_all("<q>",gauche)
can1.bind_all("<d>",droite)
can1.bind_all("<p>",pause)

can1.grid(row=0,column=0,rowspan=10)


# On cree le bouton New game qui va permettre de reinitialiser la partie

Button(fen1,text="New game",font=("Fixedsys"),command=new_game).grid(row=4,column=1,sticky=N,padx=5)
Button(fen1,text="Quit",font=("Fixedsys"),command=fen1.destroy).grid(row=6,column=1,sticky=N)

# Delimitations des limites (Creation des murs)
# que la planche ne doit pas outre passer pour ne pas finir dans le mur XD !!

can1.create_rectangle(0,0,10,600,fill="black")
can1.create_rectangle(0,0,800,10,fill="black")
can1.create_rectangle(790,0,800,600,fill="black")
can1.create_rectangle(0,600,800,590,fill="black")

# Liste des coordonnees de la planche

coord_planche1=[450,500]
coord_planche2=[350,500]
longueur=20
angle1=-pi/4
angle2=-pi/4

Cx=0.05




# Etablissement du vent
couleur=['white','light green','green','light yellow','yellow','orange','red','red','purple','#ee00dd']
vent=[]
vent.append(10)
i=0
j=0
while j<=60:
  while i<=80:
    if vent[i]+randrange(3)-1>6:
      if vent[i]+randrange(3)-1<13:
        vent.append(vent[i]+randrange(3)-1)
      else :
        vent.append(14-randrange(2))
    else :
      vent.append(5+randrange(2))

    
    can1.create_rectangle(i*10,j*10,(i+1)*10,(j+1)*10,fill=couleur[vent[i+j*80]-5], outline=couleur[vent[i+j*80]-5])
    i=i+1
  i=0
  j=j+1

# Definition des coordonnees de depart de la planche

planche1=can1.create_line(coord_planche1[0]+longueur*sin(angle1),coord_planche1[1]+longueur*cos(angle1),coord_planche1[0]-longueur*sin(angle1),coord_planche1[1]-longueur*cos(angle1),width=15,fill='red')
planche2=can1.create_line(coord_planche2[0]+longueur*sin(angle2),coord_planche2[1]+longueur*cos(angle2),coord_planche2[0]-longueur*sin(angle2),coord_planche2[1]-longueur*cos(angle2),width=15)

voile1=can1.create_line(coord_planche1[0],coord_planche1[1],coord_planche1[0]+longueur*sin(angle1/2.0),coord_planche1[1]+longueur*cos(angle1/2.0),width=3)

voile2=can1.create_line(coord_planche2[0],coord_planche2[1],coord_planche2[0]+longueur*sin(angle2/2.0),coord_planche2[1]+longueur*cos(angle2/2.0),width=3,fill='white')

# Definition du drapeau ( indicateur permettant d'arreter le programme )

flag=1

# On dessine la premiere bouee
x=400
y=100
yb=500
f=can1.create_oval(x,y,x+10,y+10,fill="black")
can1.create_oval(x,yb,x+10,yb+10,fill="black")
# Definition des pas d'avancement du serpent

dx1=sin(angle1)
dy1=cos(angle1)
dx2=sin(angle2)
dy2=cos(angle2)
vitesse1=abs(sin(angle1/1.5))*vent[int(coord_planche1[0]/10)+int(coord_planche1[1]/10)*80]*Cx
vitesse2=abs(sin(angle2/1.5))*vent[int(coord_planche2[0]/10)+int(coord_planche2[1]/10)*80]*Cx


# Le compteur de score

score=0
pause=0

# Ce compteur va permettre de ne pas remettre
# le jeu en route, a l'aide de la touche pause
# dans le cas ou le joueur aurait perdu :p

flag2=0

move()


fen1.mainloop()


