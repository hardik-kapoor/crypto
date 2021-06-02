## storing passwords and seeing if password matches using sha-256
from sha_256 import *

def passwordmatch():
    s=input()       ##password
    y=SHA2(s)
    storedAs=y.finalhashcal()
    print(storedAs)
    s2=input()
    y2=SHA2(s2)
    trying=y2.finalhashcal()
    if trying==storedAs:
        print("Same")
    else:
        print("Not same")
    
passwordmatch()
