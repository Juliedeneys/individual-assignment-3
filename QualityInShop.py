#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:20:23 2018

@author: Julie
"""

#%%
class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
        
def recalculate_quality(product):
    if product.name == "potato":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
    else:
        if product.quality < 5:
            product.quality -= 3
            
            