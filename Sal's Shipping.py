# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 18:02:51 2019

@author: acer
"""

#Ground Pricing
def ground_shipping(weight):
  if (weight < 2):
    price = 1.50
  elif (weight >= 2) and (weight <= 6):
    price = 3.00
  elif (weight >= 6) and (weight <= 10):
    price = 4.00
  else:
    price = 4.75
  return (price * weight) + 20

print(ground_shipping(8.4))

#Drone Pricing
def drone_shipping(weight):
  if (weight < 2):
    price = 4.50
  elif (weight >= 2) and (weight <= 6):
    price = 9.00
  elif (weight >= 6) and (weight <= 10):
    price = 12.00
  else:
    price = 14.25
  return (price * weight)

print(drone_shipping(1.5))

#Premium Pricing
premium_shipping  = 125
  
def cheapest_shipping (weight):
  
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_shipping
  
  if ground < drone and ground < premium:
    shipping = "Ground Shipping"
    cost = ground
  elif drone < ground and drone < premium:
    shipping = "Drone Shipping"
    cost = drone
  else:
    shipping = "Premium Shipping"
    cost = premium
  print ("The cheapest shipping is $%2.f via %s"
        %(cost, shipping))
  
cheapest_shipping(4.8)
cheapest_shipping(41.5)