'''
Created on 6 juli 2017

@author: Jani Pasanen
2017 Jani Pasanen
Python script to display a recursive algorithm for solving the 
"Towers of Hanoi" puzzle for arbitrary n

'''


# Print when reach basecase (n == 1)
def printmove(frm, to):#
    print('Move from ' + str(frm) + ' to ' + str(to))

# The algorithm    
def move(n, frm, to, spare):
    if n == 1:
        printmove(frm, to)
    else:
        move(n-1, frm, spare, to)
        move(1, frm, to, spare)
        move(n-1, spare, to, frm)
 
 
# enables this module to be run as a script. To run as script python3 towersofhanoi.py n A B C
# Make sure to supply the arguments; Number of n, name of first stack, name of second stack and
# name of third stack.       
if __name__ == '__main__':
    from sys import argv
    move(int(argv[1]),argv[2],argv[3],argv[4])  
        