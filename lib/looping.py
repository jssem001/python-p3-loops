#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter=10
    while counter >0:
        print(counter)
        counter -=1
    print("Happy New Year!")
    

def square_integers(int_list):
    # code goes here!
    sq_list=[]
    for i in int_list:
        sq_list.append(i**2)
    return sq_list
    

def fizzbuzz():
    # code goes here!
    counter =1
    while counter <=100:
        if counter % 15 == 0:
            print("FizzBuzz")
        elif counter % 3 == 0:
            print("Fizz")
        elif counter % 5 == 0:
            print("Buzz")
        else:
            print(counter)
        counter +=1
    
