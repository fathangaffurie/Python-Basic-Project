# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:55:06 2019

@author: acer
"""

#Temperature
def f_to_c(f_temp):
  c_temp = (f_temp-32) * 5/9
  return c_temp

f100_in_celcius = f_to_c(100)
print("100 Fahreinheit is equal to : " + str(f100_in_celcius) + " Celcius")

def c_to_f(c_temp):
  f_temp = (c_temp*9/5) + 32
  return f_temp

c0_in_fahreinheit = c_to_f(0)
print("0 Celcius is equal to : " + str(c0_in_fahreinheit) + " Fahreinheit")

print(""" 
""")
#Use The Force
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def get_force(mass,acceleration):
  force = mass*acceleration
  return(force)

train_force = get_force(train_mass,train_acceleration)

print ("The GE train supplies " + str(train_force) + " Newtons of force")

def get_energy(mass,c=3*(8**10)):
  energy = mass*(c**2)
  return (energy)

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

print(""" 
""")
#Do the Work
def get_work(mass, acceleration, distance):
  force = mass*acceleration
  work = force*distance
  return(work)
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")

