import create2api
import time
import pygame

#Create a Create2 Bot
controller = None

pygame.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
controller.init()

axis_data = {}
button_data = {}

bot = create2api.Create2()

bot.start()
bot.full()

def room(bot):
  motor_toggle = False
  while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
          if event.axis == 1:
            axis_data["speed"] = -1*event.value
              
          elif event.axis == 2:
            axis_data["rotation"] = -1*event.value

        elif event.type == pygame.JOYBUTTONDOWN:
          pass
          #return
        elif event.type == pygame.JOYBUTTONUP:
          print(event.button)
          if event.button == 1:
            if motor_toggle:
              bot.motors_pwm(0, 0, 0)
            else:
              bot.motors_pwm(127, 127, 127)
            motor_toggle = not motor_toggle
          elif event.button == 2:
            return 
          elif event.button == 3:
            pass
          #return
    speed = 0
    rotation = 0
    if abs(axis_data["speed"]) > 0.4:
      speed = axis_data["speed"]
    if abs(axis_data["rotation"]) > 0.4:
      rotation = axis_data["rotation"]
    #print speed, rotation
    text = "    "
    if rotation < 0:
      text = "  ->"
    elif rotation > 0:
      text = "<-  "
    velocity = int(speed*499)
    radius = int(rotation*200)
    print velocity, radius
    #time.sleep(0.01)
    bot.drive(velocity, radius)
    bot.digit_led_ascii(text)
    time.sleep(0.05)
    
room(bot)

bot.motors_pwm(0, 0, 0)
bot.drive(0, 0)

time.sleep(1)


bot.destroy()