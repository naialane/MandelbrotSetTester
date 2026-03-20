#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:30:47 2026

@author: naialane
"""

def testc(re, im, its):
    c = complex(re, im)
    
    z_0 = complex(0, 0)
    listz = [z_0]
    
    for z in listz:
        while len(listz) < its:
            listz.append(listz[-1]**2 + c)
            if ((listz[-1].real)**(2) + (listz[-1].imag)**(2))**0.5 > 4:
                return False
    return True
    
    
    
    