#Test code for scrabbler.py
#By Sampreet Kishan
#Date : 05/11/2017
#Contact: sampreet.kishan@colorado.edu

#To understand the code better, please refer to the readme file 'readme.txt'
#Makes use of the 'pytest' Python framework
#To run the script, run the command "pytest" on the command line.
#Also, make sure this file is in the same directory (project) as the scrabbler.py Python file.

import scrabbler

fh = open("words.txt", 'r')
fh_read = fh.read(655360)

def test_pref():
    scrabbler.prefix="girl"
    pref_total=scrabbler.pref(fh_read)
    assert pref_total == 8

def test_suff():
    scrabbler.suffix="uck"
    suff_total=scrabbler.suff(fh_read)
    assert suff_total == 27

def test_comb():
    scrabbler.word="dB"
    word_total=scrabbler.scrable(fh_read)
    assert word_total == 1

def test_incor_suff():
    scrabbler.suffix="ishh"
    output=scrabbler.suff(fh_read)
    print(output)
    if(output==-1):
       assert True
    else:
       assert False


def test_incor_pref():
    scrabbler.prefix="libb"
    output=scrabbler.pref(fh_read)
    print(output)
    if(output==-1):
       assert True
    else:
       assert False







