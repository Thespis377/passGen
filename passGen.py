#! /usr/bin/python
#
# Passphrase generator
#

import sys
import re
import random
import string
import argparse


class myPassword ():

    @classmethod
    def __init__(self, length=12, wordlist='./wordlist'):
        #/usr/share/dict/linux.words

        self.length = length
        self.wordlist = wordlist 
        with open(self.wordlist) as f:
            self.allwords = f.readlines()
        #Remove all but 5 character words
        self.words = []
        for w in self.allwords:
            if len(w.strip()) > 5:
                w = w.strip()
                self.words.append(w.capitalize()) #Make them all capitalized

        #Generate a string of characters to pull from to generate the passwords
        self.passwdChars = string.punctuation + string.digits
        for i in range(0,3):
            #Add 3 iterations of ascii letters to be letter heavy.
            self.passwdChars += string.ascii_letters

    def genphrase(self, num=3):
        #Generate a passphrase with a default of 3 words.
        self.phrase = ""
        for p in range(0,num):
            self.phrase = self.phrase + random.choice(self.words)
        return self.phrase
    
    def genpass(self, num=None):
        #Generate a random password
        #num is character length
        if num is None:
            num = self.length
        
        self.password = ""
        for p in range(0,num):
            self.password = self.password + random.choice(self.passwdChars)

        return self.password



if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Password and Passphrase generator', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("total", nargs='?', default=3, type=int, help="Number of total passwords and pass phrases to generate")
    parser.add_argument("-l", "--length", default=12, type=int, help="Password length.")
    args = parser.parse_args()

    if args.length:
        myPass = myPassword(args.length)
    else:
        myPass = myPassword()

    for t in range(0,args.total):
        print("Random Passphrase: ", myPass.genphrase())
        print("Random Password: ", myPass.genpass())

