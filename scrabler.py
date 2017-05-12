#Scrabler code for Oracle
#By Sampreet Kishan
#Date : 05/11/2017
#Contact: sampreet.kishan@colorado.edu

import sys
import os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--word",help="Please enter the scrambled set of characters")
parser.add_argument("--prefix",help="Please enter the prefix")
parser.add_argument("--suffix",help="Please enter the suffix")
args=parser.parse_args()
try:
    word=args.word
    print("The word is:"+ word)
except:
    print("No word")
try:
    prefix=args.prefix
    print("The prefix is:"+prefix)
except:
    print("No prefix")
try:
    suffix=args.suffix
    print("The suffix is:"+suffix)
except:
    print("No suffix")


def scrable(words):
    #Function to print out the right words from the list
    double_checker(word)
    word_arr=[]
    for i in range(len(word)):
        word_arr.append(word[i])

    words=words.splitlines()
    alpha={}
    for line in words:
        for i in range(97,123):
            alpha[chr(i)]=0
        check=1
        double_check=0

        for i in range(len(line)):
            try:
                if(line[i] not in word):
                    check=0
                key=line[i]
            #print(str(key))

                if(alpha[key]==1):
                    check=0
                elif(line[i] in word and alpha[line[i]]==0):
                    #print("Setting: "+line[i])
                    alpha[line[i]]=1
            except:
                check=0
        #print(alpha)

        if(check==1):
            print(line)
            #$print("\n")

def pref(words):
    print("The prefix is: "+str(prefix))
    double_checker(prefix)
    words=words.splitlines()
    pref_len=len(prefix)

    for line in words:
        check=1
        for i in range(pref_len):
            if(len(prefix)>len(line)):
                check=0
            elif(prefix[i]!=line[i]):
                check=0

        if(check==1):
            print(line)



def suff(words):
    print("The suffix is:"+str(suffix))
    double_checker(suffix)
    words=words.splitlines()
    suff_len=len(suffix)-1

    for line in words:
        check=1
        i=suff_len
        line_ind=len(line)-1
        while(i>=0 and line_ind>=0):
            if(len(suffix)>len(line)):
                check=0
            elif(suffix[i]!=line[line_ind]):
                check=0
            i=i-1
            line_ind=line_ind-1
        if(check==1):
            print(line)



def double_checker(text):
    #Function to check if the word is valid or not
    k=0
    while(k!=len(text)):
        if(text.count(text[k])>=2 or (text[k].islower()!=1)):
            print("Not a valid word")
            sys.exit()
        k=k+1


def main():
    print("\n\n")
    word_2=str(word)
    #double_checker(word_2)
    if(os.path.isfile("words.txt")==0):
        print("The file does not exist.\nThe program will be quitting now.")
        sys.exit()
    fh=open("words.txt",'r')
    f_read=fh.read(655360)
    if(word):
        scrable(f_read)
    print("\n\n")
    if(prefix):
        pref(f_read)
    print("\n\n")
    if(suffix):
        suff(f_read)
    print("------------------")
    fh.close()
    sys.exit()
main()