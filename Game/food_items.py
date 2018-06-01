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
food_items = [['apfel','gemuese', 1, 2, 'Apfel.gif'],
              ['birne','gemuese', 1, 2, 'Birne.gif'],
              ['banane','gemuese', 1, 10,'Banane.gif'],
              ['mate','boost', 1, 1, 'energy', 'Mate.gif'],
              ['brokkoli','gemuese', 1, 1,  'Brokkoli.gif'],
              ['butter','gscheid', 1, 1, 10, 'Butter.gif'],
              ['booster','boost', 1, 1, 'energy', 'EnergyBooster.gif'],
              ['crazywolf','boost', 1, 1, 'energy', 'EnergyCrazyWolf.gif'],
              ['flyingpower','boost', 1, 1, 'energy', 'EneryFlyingPower.gif'],
              ['gurke','gemuese', 1, 1, 'Gurke.gif'],
              ['joint','boost', 1, 1, 'weed', 'Joint.gif'],
              ['lachgummi','gscheid', 1, 1, 20, 'LachgummiSauer.gif'],
              ['milchreis','gscheid', 1, 1, 20, 'Milchreis.gif'],
              ['salat','gemuese', 1, 1,  'Salat.gif'],
              ['schweinebauch','gscheid', 1, 1, 20, 'Schweinebauch.gif'],
              ['steak','gscheid', 1, 1, 20, 'Steak.gif'],
              ['tunfisch','gscheid', 1, 1, 20, 'Tunfisch.gif'],
              ['zucker','gscheid', 1, 1, 20, 'Zucker.gif']

              ]

              
# occurrences
occurence = np.array([fod_it[3] for fod_it in food_items])
occurence = occurence/occurence.sum()

def get_food_item():
    return food_items[np.random.choice(len(food_items), p=occurence)]
