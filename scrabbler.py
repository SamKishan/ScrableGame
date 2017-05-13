#Scrabler code for Oracle
#By Sampreet Kishan
#Date : 05/11/2017
#Contact: sampreet.kishan@colorado.edu
#To understand the code better, please refer to the readme file 'readme.txt'


import sys
import os
import argparse
from itertools import chain
from prettytable import PrettyTable
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
    a=double_checker(word,"combination")
    if(a==0):
        return -1
    word_arr=[]
    for i in range(len(word)):
        word_arr.append(word[i])

    words=words.splitlines()
    alpha={}
    total=0
    for line in words:
        concat=chain(range(97,123),range(65,91))
        for i in concat:
            alpha[chr(i)]=0
        check=1
        double_check=0

        for i in range(len(line)):
            try:
                if(line[i] not in word):
                    check=0
                key=line[i]

                if(alpha[key]==1):
                    check=0
                elif(line[i] in word and alpha[line[i]]==0):
                    alpha[line[i]]=1
            except:
                check=0

        if(check==1):
            print(line)
            total=total+1
    if(total==0):
        return 0
    else:
        return total


def pref(words):
    #Function to print out the words with the prefix entered as a system argument
    print("The prefix is: "+str(prefix))
    a=double_checker(prefix,"prefix")
    if(a==0):
        return -1
    words=words.splitlines()
    pref_len=len(prefix)
    total=0
    for line in words:
        check=1
        for i in range(pref_len):
            if(len(prefix)>len(line)):
                check=0
            elif(prefix[i]!=line[i]):
                check=0

        if(check==1):
            print(line)
            total=total+1
    if(total==0):
        return 0
    else:
        return total

def suff(words):
    #Function to print all the words that contain the suffix which was entered as a system argument
    print("The suffix is:"+str(suffix))
    a=double_checker(suffix,"suffix")
    if(a==0):
        return -1
    words=words.splitlines()
    suff_len=len(suffix)-1
    total=0
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
            total=total+1
    if(total==0):
        return 0
    else:
        return total

def double_checker(text,type):
    #Function to check if the word/prefix/suffix is valid or not.
    #Checks if it has a character that occurs more than once in the string, in which case it is invalid
    k=0
    check=1
    while(k!=len(text)):
        if(text.count(text[k])>=2):
            print("Not a valid "+str(type))
            check=0
            break
        k=k+1
    if(check==0):
        return 0
    else:
        return 1

def main():
    #Calls all the above functions. Prints out a table of the results.
    print("\n\n")
    word_2=str(word)
    if(os.path.isfile("words.txt")==0):
        print("The file does not exist.\nThe program will be quitting now.")
        sys.exit()
    fh=open("words.txt",'r')
    f_read=fh.read(655360)
    x = PrettyTable(["Type", "Number of occurences"])
    if(word):
        scrable_no=scrable(f_read)
        if(scrable_no==-1):
            print("Invalid Combination")
            #pass
        else:
            x.add_row(["Letter Combinations of \"" + str(word)+"\"", scrable_no])
    print("\n\n")
    if(prefix):
        pref_no=pref(f_read)
        if(pref_no==-1):
            print("Invalid prefix")
            #pass
        else:
            x.add_row(["Prefix \"" + str(prefix)+"\"", pref_no])
    print("\n\n")
    if(suffix):
        suff_no=suff(f_read)
        if(suff_no==-1):
            print("Invalid suffix")
            #pass
        else:
            x.add_row(["Suffix \"" + str(suffix)+"\"", suff_no])
    print("\n\n Statistics")
    print(x)
    print("*******The End********")
    fh.close()
main()