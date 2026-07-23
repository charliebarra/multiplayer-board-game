import turtle
import random
import time

# Colors firebrick1, gold, LightGreen, DodgerBlue1, DeepPink, AliceBlue

'''SETUP'''
background = turtle.Screen()
background.setup(width=800, height=800)
background.bgcolor("lightblue")
#Drawing config
t = turtle.Turtle()
t.shape("classic")
t.pensize(1)
t.speed(0)
t.penup()
t.goto(0,0)

#Player 1 config
p1 = turtle.Turtle()
p1.shape("turtle")
p1.color("DarkSlateGray")
p1.pensize("1")
p1.speed(1)
p1.penup()
p1.goto(0,0)

#Player 2 config
p2 = turtle.Turtle()
p2.shape("turtle")
p2.color("coral")
p2.pensize("1")
p2.speed(1)
p2.penup()
p2.goto(0,0)

#Player 3 config
p3 = turtle.Turtle()
p3.shape("turtle")
p3.color("MediumSeaGreen")
p3.pensize("1")
p3.speed(1)
p3.penup()
p3.goto(0,0)

#Player 4 config
p4 = turtle.Turtle()
p4.shape("turtle")
p4.color("VioletRed3")
p4.pensize("1")
p4.speed(1)
p4.penup()
p4.goto(0,0)

'''FUNCTIONS'''
#Function for each box
def draw_box(x,y,num,t_color):
    t.color(t_color)
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.goto(x,y+50)
    t.goto(x+50,y+50)
    t.goto(x+50,y)
    t.goto(x,y)
    t.end_fill()
    t.color("white")
    t.write(num, font=("Courier",30,"bold"))
    t.penup()

#Function for drawing dice
def draw_dice(num):
    t.goto(-200,250)
    t.color("azure3")
    t.pendown()
    t.begin_fill()
    t.fillcolor("AliceBlue")
    t.goto(-200,300)
    t.goto(-150,300)
    t.goto(-150,250)
    t.goto(-200,250)
    t.goto(-185,250)
    t.end_fill()
    t.color("grey3")
    t.write(num, font=("Courier",30,"bold"))
    t.penup()

#Runs the player movement
def player_controller(pX,pX_pos):
    #Allows player to control when they move
    roll = input("Type Y when you are ready to roll the dice. ")
    while roll != 'Y':
        roll = input("Type Y when you are ready to roll the dice. ")

    #Number that is rolled on the dice
    roll_num = random.randint(1,6)

    draw_dice(roll_num)
    
    #Movement Manager
    for i in range(roll_num):
        if pX_pos != (-125,-175):
            #Determines when to turn right
            if pX_pos == (-125,125) or pX_pos == (175,125) or pX_pos == (175,-175):
                pX.right(90)
            #Determines when to turn left
            if pX_pos == (-125,-75):
                pX.left(90)
            #Moves the piece
            pX.forward(50)
            pX_pos = pX.pos()

    time.sleep(1)

    #Mystery Space Manager
    if pX_pos == (-125,75) or pX_pos == (-25,125) or pX_pos == (125,125) or pX_pos == (175,25) or pX_pos == (175,-125):
        print("Mystery Move Triggered!")
        mystery_move = random.randint(1,4)
        if mystery_move == 1:
            print("You get to move forward 2 spaces!")
            for i in range(2):
                if pX_pos != (-125,-175):
                    #Determines when to turn right
                    if pX_pos == (-125,125) or pX_pos == (175,125) or pX_pos == (175,-175):
                        pX.right(90)
                    #Determines when to turn left
                    elif pX_pos == (-125,-75):
                        pX.left(90)
                    #Moves the piece
                    pX.forward(50)
                    pX_pos = pX.pos()

        if mystery_move == 2:
            print("You get to move back 3 spaces!")
            for i in range(3):
                if pX_pos != (-125,-175):
                    if i == 0:
                        pX.left(180)
                    #Determines when to turn right
                    if pX_pos == (-125,125) or pX_pos == (175,125) or pX_pos == (175,-175):
                        pX.left(90)
                    #Determines when to turn left
                    elif pX_pos == (-125,-75):
                        pX.right(90)
                    #Moves the piece
                    pX.forward(50)
                    pX_pos = pX.pos()

                    if i == 2:
                        pX.right(180)

                    

        if mystery_move == 3:
            print("You get to go back to start!")
            pX.goto(-175,-75)
            pX.setheading(0)
            pX_pos = pX.pos()

        if mystery_move == 4:
            print("You get to move to finish!")
            pX.goto(-125,-175)
            pX.setheading(180)
            pX_pos = pX.pos()
        
        time.sleep(1)

'''DRAWING BOARD'''
#Boxes 1-5
draw_box(-200,-100,"🚩","firebrick1")
draw_box(-150,-100,1,"LightGreen")
draw_box(-150,-50,2,"DodgerBlue1")
draw_box(-150,0,3,"gold")
draw_box(-150,50,"?","DeepPink")
draw_box(-150,100,5,"LightGreen")

#Boxes 6-11
draw_box(-100,100,6,"DodgerBlue1")
draw_box(-50,100,"?","DeepPink")
draw_box(0,100,8,"gold")
draw_box(50,100,9,"LightGreen")
draw_box(100,100,"?","DeepPink")
draw_box(150,100,11,"DodgerBlue1")

#Boxes 12-17
draw_box(150,50,12,"gold")
draw_box(150,0,"?","DeepPink")
draw_box(150,-50,14,"LightGreen")
draw_box(150,-100,15,"DodgerBlue1")
draw_box(150,-150,"?","DeepPink")
draw_box(150,-200,17,"gold")

#Boxes 18-22
draw_box(100,-200,18,"LightGreen")
draw_box(50,-200,19,"DodgerBlue1")
draw_box(0,-200,20,"gold")
draw_box(-50,-200,21,"LightGreen")
draw_box(-100,-200,22,"DodgerBlue1")
draw_box(-150,-200,"❌","firebrick1")

'''GAME LOOP'''
p1.goto(-175,-75)
p1_pos = p1.pos()

p2.goto(-175,-75)
p2_pos = p2.pos()

p3.goto(-175,-75)
p3_pos = p3.pos()

p4.goto(-175,-75)
p4_pos = p4.pos()

while p1_pos != (-125,-175) and p2_pos != (-125,-175) and p3_pos != (-125,-175) and p4_pos != (-125,-175):
    for i in range(1,5):
        if i == 1:
            print("Player 1's turn.")
            player_controller(p1,p1_pos)
            p1_pos = p1.pos()
            print(p1_pos)
            if p1_pos == (-125,-175):
                break #Stops other players from moving after a win
            
        if i == 2:
            print("Player 2's turn.")
            player_controller(p2,p2_pos)
            p2_pos = p2.pos()
            print(p2_pos)
            if p2_pos == (-125,-175):
                break #Stops other players from moving after a win
            
        if i == 3:
            print("Player 3's turn.")
            player_controller(p3,p3_pos)
            p3_pos = p3.pos()
            print(p3_pos)
            if p3_pos == (-125,-175):
                break #Stops other players from moving after a win
            
        if i == 4:
            print("Player 4's turn.")
            player_controller(p4,p4_pos)
            p4_pos = p4.pos()
            print(p4_pos)
            if p4_pos == (-125,-175):
                break #Stops other players from moving after a win
            
#Prints who won  
t.goto(50,250)     
if p1_pos == (-125,-175):   
    t.write("P1 Wins!", font=("Courier",30,"bold"))
if p2_pos == (-125,-175):
    t.write("P2 Wins!", font=("Courier",30,"bold"))
if p3_pos == (-125,-175):
    t.write("P3 Wins!", font=("Courier",30,"bold"))
if p4_pos == (-125,-175):
    t.write("P4 Wins!", font=("Courier",30,"bold"))

turtle.done()