#This is a palindrome checker.
#The user will give us text, and we will determine whether or not it is a
#palindrome.

#accept text

import re
text = input("Feed me text: ")

def pal():
    lower = (text).lower()
    print (lower)
    stripped = re.sub(r'[^A-Za-z]',"", lower)
    print (stripped)
    rev = (stripped[::-1])
    print (rev)
    if rev == stripped:
        return "You have a palindrome!"
    else:
        return "This is not a palindrome."

pal()    
#lower case text
#strip text off all but letters
#reverse text
#compare strings
#print steps



#how is this recursive?
