# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 16:45:55 2018

@author: Yatri
"""
def matrix(arr):
    print(" ".center(6," ")+"|"+" ".center(6," ")+"|"+" ".center(6," "))
    print(arr[0].center(6," ")+"|"+arr[1].center(6," ")+"|"+arr[2].center(6," "))
    print(" ".center(6," ")+"|"+" ".center(6," ")+"|"+" ".center(6," "))
    print("-"*20)
    print(" ".center(6," ")+"|"+" ".center(6," ")+"|"+" ".center(6," "))
    print(arr[3].center(6," ")+"|"+arr[4].center(6," ")+"|"+arr[5].center(6," "))
    print(" ".center(6," ")+"|"+" ".center(6," ")+"|"+" ".center(6," "))
    print("-"*20)
    print(" ".center(6," ")+"|"+" ".center(6," ")+"|"+" ".center(6," "))
    print(arr[6].center(6," ")+"|"+arr[7].center(6," ")+"|"+arr[8].center(6," "))
    print(" ".center(6," ")+"|"+" ".center(6," ")+"|"+" ".center(6," "))

def win(arr,player_1,player_2):

    f=[['0','1','2'],['0','3','6'],['0','4','8'],['3','4','5'],['6','7','8'],['1','4','8'],['2','5','8'],['2','4','7']]
    for each in f:
        eac=each
        i=int(eac[0])
        j=int(eac[1])
        k=int(eac[2])
        if arr[i]==arr[j]==arr[k]=="X":
            print("%s won the game" %player_1)
            
        if arr[i]==arr[j]==arr[k]=="O":
            print("%s won the game" %player_2)
            
            


a=[ ]
condition=0
count=0
player_1=input("Enter name of player 1: ")
player_2=input("Enter name of player_2: ")
for i in range(10):
    a.append(" ")

for i in range(0,10):
    (location)= input("Please enter your location. Choose from digits 0-8 :  ")
    location=int(location)
    while (location not in range(0,9)) or a[location]!=" " :
        print("Please enter a valid input between 0-8 and make sure the place is empty")
        location=int(input())
    print("your chosen location is %d" % (location))
    a[location]="X"
    condition+=1
    matrix(a)
    win(a,player_1, player_2)

    
    if condition<9:
        (location)= input("Please enter your location. Choose from digits 0-8 :  ")
        location=int(location)
        while (location not in range(0,9)) or a[location]!=" ":
            print("Please enter a valid input between 0-8 and make sure the place is empty")
            location=int(input())
        print("your chosen location is %d" % (location))
        a[location]="O"
        condition+=1
        matrix(a)
        win(a,player_1, player_2)
        
    
    
