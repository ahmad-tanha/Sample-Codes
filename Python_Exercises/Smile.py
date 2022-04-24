# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 23:19:36 2021

@author: Ahmad
"""
import numpy as np

def isInCircle(posX, posY, circleX, circleY, radius):
  distanceFromCircleCenter = np.sqrt((circleX-posX)**2+(circleY-posY)**2)
  return distanceFromCircleCenter <= radius

def isOnCircle(posX, posY, circleX, circleY, radius, thickness, squashY):
  distanceFromCircleCenter = np.sqrt((circleX-posX)**2+((circleY-posY)/squashY)**2)
  return distanceFromCircleCenter >= radius - thickness and distanceFromCircleCenter <= radius + thickness
  

result = ''
charCount = 0

# Canvas dimensions
width = 31
height = 31
halfWidth = np.floor(width * 0.5)
halfHeight = np.floor(height * 0.5)

# Style constants
strokeWidth = 0.6

# Smiley face configuration
headSize = 13;
headSquashY = 0.78
eyePositionX = 10
eyePositionY = 12
eyeSize = 1
mouthSize = 15
mouthPositionX = width / 2
mouthPositionY = 5
mouthOffsetY = 11

for y in range(height):
  for x in range(width):
    isHead = isOnCircle(x, y, halfWidth, halfHeight, headSize, strokeWidth, headSquashY)
    isLeftEye = isInCircle(x, y, eyePositionX, eyePositionY, eyeSize)
    isRightEye = isInCircle(x, y, width - eyePositionX - 1, eyePositionY, eyeSize)
    isMouth = isOnCircle(x, y, mouthPositionX, mouthPositionY, mouthSize, strokeWidth, 1) and y > mouthPositionY + mouthOffsetY

    if (isLeftEye or isRightEye or isMouth or isHead):
      result += "*"
    else:
      result += "."
      
    result += " "

    # Make sure the smiley face doesn't deform as the container changes width.
    charCount += 1
    if (charCount % width == 0):
      result += "\n"
    
print(result)    
