#Siyu Chen
#11/11/17
#Simulate the data part of the plinko program

import time
import random
import math

random.seed()

#if these two values mutiplied together is "too big", it will take a long time to run the program
#both values have an effect on the result
balls = int(input("How many balls?"))
layer = int(input("How many layers?"))
print("Calculating...\n")
s1 = 0
s2 = 0
s3 = 0

#simulate the action of going down the plinko board.
def generate(trial, max):
  result = []

  #loop through every ball
  for i in range(0, trial):
      #the starting position of the ball
      instance = 0

      #loop through every layer of the board
      for j in range(1, max):

          #randomly determine whether the ball goes to the left or to the right
          x = random.randint(0,1)
          if x == 1:
              instance += 1

      #add up the result of the balls
      result.append(instance)
      
  return result

#create a list that shows how many balls are in each pit.
def total(list, max):
  countList = {}

  for i in range(0, max):

    countList[i] = list.count(i)

  return countList

#find the mean of the result 
def mean(list):

    total = 0
    for n in list:
        total += n

    mean = total/len(list)
    return mean

#find the standard deviation of the result
def standDev(list):

    sum = 0
    m = mean(list)
    for n in list:
        sum += (n-m)**2

    sx = math.sqrt(sum/(len(list)-1))

    return sx

#excute the simulation
r = generate(balls, layer)
l = total(r, layer)
m = mean(r)
sd = standDev(r)


for i in range(0, layer):

  #calculate the amount of balls within 1 standard deviation of the mean
  if i < (m + sd) and i > (m - sd):
    s1 += l[i]

  #calculate the amount of balls within 2 standard deviation of the mean
  if i < (m + sd*2) and i > (m - sd*2):
    s2 += l[i]

  #calculate the amount of balls within 3 standard deviation of the mean
  if i < (m + sd*3) and i > (m - sd*3):
    s3 += l[i]

#convert them into percentages 
p1 = (s1/balls)*100
p2 = (s2/balls)*100
p3 = (s3/balls)*100

#Using the 68-95-99.7 rule of the normal curve to compare the result to a true normal curve
print("result: ", l, "\n")
print("Ideal: 1σ    2σ    3σ")
print("     68%   95%   99.7%\n")
print("Actual: 1σ       2σ        3σ")
print("       ", p1, "%    ",p2, "%    " ,p3, "%")
