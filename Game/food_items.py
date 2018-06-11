# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:31:00 2018

@author: Weissenbäck
"""


''''
    dict of food items 'name':(lists of [type, speed, chance_of_occurrence(weight), image_name])
    wenn typ gscheid: + nutritional_vale int
    wenn typ boost: + boost function
'''

import numpy as np
food_items = [['apfel','gemuese', 1, 6, 'Apfel.gif'],
              ['birne','gemuese', 1, 8, 'Birne.gif'],
              ['banane','gemuese', 1, 5,'Banane.gif'],
              ['mate','boost', 1, 6, 'energy', 'Mate.gif'],
              ['brokkoli','gemuese', 1, 6,  'Brokkoli.gif'],
              ['butter','boost', 1, 3, 'multi', 'Butter.gif'],
              ['booster','boost', 1, 3, 'energy', 'EnergyBooster.gif'],
              ['crazywolf','boost', 1, 3, 'energy', 'EnergyCrazyWolf.gif'],
              ['flyingpower','boost', 1, 3, 'energy', 'EnergyFlyingPower.gif'],
              ['gurke','gemuese', 1, 8, 'Gurke.gif'],
              ['joint','boost', 1, 2, 'weed', 'Joint.gif'],
              ['lachgummi','gscheid', 1, 10, 200, 'LachgummiSauer.gif'],
              ['milchreis','gscheid', 1, 10, 100, 'Milchreis.gif'],
              ['salat','gemuese', 1, 8,  'Salat.gif'],
              ['schweinebauch','gscheid', 1, 5, 200, 'Schweinebauch.gif'],
              ['chips','gscheid', 1, 10, 250, 'chips.gif'],
              ['steak','gscheid', 1, 5, 200, 'Steak.gif'],
              ['bucket','gscheid', 1, 6, 500, 'bucket.gif'],
              ['fleischwurst','gscheid', 1, 3, 1000, 'Fleischwurst.gif'],
              ['burger','gscheid', 1, 5, 500, 'Burger.gif'],
              ['tunfisch','gscheid', 1, 11, 200, 'Tunfisch.gif'],
              ['zucker','boost', 1, 3, 'multi', 'Zucker.gif']
              ]

              
# occurrences
occurence = np.array([fod_it[3] for fod_it in food_items])
occurence = occurence/occurence.sum()

def get_food_item():
    return food_items[np.random.choice(len(food_items), p=occurence)]
