# A small python program that will run in the ISS (International space station) made by me and my daughter. This is a part of Astro Pi Missions.
# https://astro-pi.org/mission-space-lab/

# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image

c = (0, 0, 0) # Black
m = (34, 139, 34) # ForestGreen
q = (255, 255, 0) # Yellow
t = (255, 140, 0) # DarkOrange
y = (255, 20, 147) # DeepPink

for i in range(5):
  rgb = sense.color # get the colour from the sensor
  c = (rgb.red, rgb.green, rgb.blue)

  image = [
    c, c, y, y, y, y, c, c,
    c, y, y, t, t, y, y, c,
    y, y, t, q, q, t, y, y,
    c, y, y, t, t, y, y, c,
    c, c, y, y, y, y, c, c,
    m, c, c, m, m, c, c, m,
    c, m, m, m, m, m, m, c,
    c, c, c, m, m, c, c, c]

  # Display the image

  sense.set_pixels(image)
  sleep(1)

x = (178, 34, 25)  # choose your own red, green, blue values between 0 - 255
sense.clear(x)