"""
#adding images of obstacles
def make_obstacle():
  if obstacle_down[index].xcor() > -400:
    obstacle_down[index].showturtle()
    # sky_objects[index].speed(50)
    obstacle_down[index].backward(25)
  else:
    obstacle_down[index].clear()
    wn.addshape(obstacle_list[index])
    obstacle_down[index].shape(cloud_or_star[index])
    obstacle_down[index].setx (rand.randint(400,600))
    obstacle_down[index].sety (rand.randint(400,600))

  wn.addshape('pipe_down.gif')
  wn.addshape('pipe_up.gif')
  flappy_bird.shape('pipe_down.gif')
  flappy_bird.shape('pipe_up.gif')
"""