
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 06:05:48 2015

@author: Alex
"""




import pandas as pd
import random
import string

words = ['Gnar','Rad','Kook','Barney','Finner','Tube','Froth','Cutback','Shred','Sexwax','Kelly','Taj','Kerrzy','Parko']
symbols = ['#','@','?']
pass_dict = pd.DataFrame.from_csv('pass_strings.csv')

def twelverandomwords():
    pass_string = ''.join(random.choice(words) for _ in range(3))
    pass_string = pass_string+random.choice(symbols)
    pass_string = pass_string+str(random.randint(10,99))
    return pass_string

new_or_old = raw_input("new or old? \n ")



## if new password is needed
if new_or_old=='new':
    place = raw_input("Somewhere new, where ya at? \n  ")
    pass_string = twelverandomwords()
    name = raw_input("What's your username? \n  ")
    print "Ok, your username is "+name+", your pass_string is "+pass_string+". \n"
    pass_dict=pass_dict.append(pd.DataFrame({'place':place,'name':name,'pass_string':pass_string},index=[place]))

if new_or_old=='old':
    place = raw_input("Forgot again? where ya at? \n ")
    name = pass_dict.ix[place]['name']
    pass_string = pass_dict.ix[place]['pass_string']
    print "Ok, for "+place+" try username "+name+" + "+pass_string+". \n"

 
pass_dict = pass_dict.drop_duplicates('place',take_last=True)
pass_dict[['place','name','pass_string']].to_csv('pass_strings.csv')  
## ^^ only for 'new' password??