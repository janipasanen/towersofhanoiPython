#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 6 juli 2017
© 2017 Jani Pasanen

@author: Jani Pasanen
Python script to display a recursive algorithm for solving the 
"Towers of Hanoi" puzzle for arbitrary n

'''


# Print when reach base case (n == 1)
def printmove(a, b):#
    print('Move from ' + str(a) + ' to ' + str(b))

# The algorithm    
def move(n, a, b, c):
    if n == 1:
        printmove(a, b)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, c, b, a)
 
 
# enables this module to be run as a script. To run as script python3 towersofhanoi.py n A B C
# Make sure to supply the arguments; Number of n, name of first stack, name of second stack and
# name of third stack.       
if __name__ == '__main__':
    from sys import argv
    move(int(argv[1]),argv[2],argv[3],argv[4])  
        
