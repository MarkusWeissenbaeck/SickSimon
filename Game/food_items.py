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
              ['braten','gscheid', 1, 10, 20, 'Banane.gif']
              ]

# occurrences
occurence = np.array([fod_it[3] for fod_it in food_items])
occurence = occurence/occurence.sum()

def get_food_item():
    return food_items[np.random.choice(len(food_items), p=occurence)]