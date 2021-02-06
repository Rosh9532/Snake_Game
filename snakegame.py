import turtle
import time
import random
delay=0.1
score = 0
high_score = 0

#S1 Setting the screen
r=turtle.Screen()
r.title("Snake Game by Roshni")
r.bgcolor("brown")
r.setup(width=600,height=600)
r.tracer(0) #turn off the screen updates


#S2 Making the snake head
h=turtle.Turtle()
h.speed(0)
h.shape("circle")
h.color("green")
h.penup()    #so tht it cannot draw anything
h.goto(0,0)  #positioning the start at center
h.direction="stop"

seg=[]
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "normal"))

#S5 function to change direction of head
def go_up():  
    if h.direction!="down": 
         h.direction="up"
def go_down(): 
    if h.direction!="up":  
         h.direction="down"  
def go_left():  
    if h.direction!="right": 
         h.direction="left"
def go_right(): 
    if h.direction!="left":  
         h.direction="right"    

#S7 food
f=turtle.Turtle()
f.speed(0)
f.shape("square")
f.color("red")
f.penup()    #so tht it cannot draw anything
f.goto(0,100)  #positioning the start at center              

#S4 function to move head
def move():
    if h.direction=="up":
        y=h.ycor()
        h.sety(y+20)

    if h.direction=="down":
        y=h.ycor()
        h.sety(y-20)

    if h.direction=="left":
        x=h.xcor()
        h.setx(x-20)


    if h.direction=="right":
        x=h.xcor()
        h.setx(x+20)

#S6 keyboaord     
r.listen()
r.onkeypress(go_up,"w")
r.onkeypress(go_down,"s")
r.onkeypress(go_left,"a")
r.onkeypress(go_right,"d")

#S3 main game loop
while True:
    r.update()
    # #check for border collision
    # if h.xcor()>340 or h.xcor()<-340 or h.ycor()<340 or h.ycor()<-340:
    #     time.sleep(1)
    #     h.goto(0,0)
    #     h.direction="stop"
    #     #hide segments
    #     for s in seg:
    #         s.goto(1000,1000)
    #     #clear segment list
    if h.xcor()>340 or h.xcor()<-340 or h.ycor()>340 or h.ycor()<-340:
        time.sleep(1)
        h.goto(0,0)
        h.direction = "stop"

        # Hide the segments
        for segment in seg:
            segment.goto(1000, 1000)

        # Clear the segments list
        seg.clear()
        #reset score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "normal")) 

       
# check for collision food
    if h.distance(f)<20:
        #S8 move the food to random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        f.goto(x,y)
    #increae by adding segment
        newseg=turtle.Turtle()
        newseg.speed(0)
        newseg.shape("circle")
        newseg.color("orange")
        newseg.penup()
        seg.append(newseg)

         # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "normal")) 

    # S8 move the segmrnt
    for index in range(len(seg)-1,0,-1):
        x=seg[index-1].xcor()
        y=seg[index-1].ycor()
        seg[index].goto(x,y)

    # S9move seg 0
    if len(seg)>0:
        x=h.xcor() 
        y=h.ycor()  
        seg[0].goto(x,y) 



    move()
    #S11 check for collision with own body
    for segment in seg:
        if segment.distance(h) < 20:
            time.sleep(1)
            h.goto(0,0)
            h.direction = "stop"

            # Hide the segments
            for segment in seg:
                segment.goto(1000, 1000)

            # Clear the segments list
            seg.clear() 
            # Reset the score
            
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "normal"))

    time.sleep(delay)

r.mainloop()