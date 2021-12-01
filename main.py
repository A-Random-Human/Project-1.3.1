#Importing Turtle and Random modules
import turtle as trtl
import random as rand


#Creating screen and background
wn = trtl.Screen()
wn.bgpic("background3.png")

#Creating Flappy Bird Object
flappy_bird = trtl.Turtle()
wn.addshape('stand-still_bird.gif')
#wn.addshape('flapping_bird')
flappy_bird.shape('stand-still_bird.gif')


#creating the clouds and stars
flappy_bird = []
clouds_and_stars = ['cloud_1', 'cloud_2', 'cloud_3', 'cloud_4']
wn.addshape('cloud_1.gif')


#functions:

flappybird = 0

# randomizes the candy being clicked
def ___:
  num2 = rand.randint(0,num)
  clouds2 = clouds[num2]
  wn.addshape(clouds2)
  flappy_bird.shape(clouds2)
  flappy_bird.score += 5
  print(flappy_bird.score)

#def flap():
#  flappy_bird.left(20)
  

#flappy_bird.onclick(flap)
#wn.onkeypress(flap,'a')


#Window
wn.mainloop()