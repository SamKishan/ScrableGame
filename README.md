Source code: scrabbler.py
Test code: test_test.py
Author: Sampreet Kishan
Start date: 05/11/2017
End date: 05/12/2017
Python test framework: pytest
Contact information: saki8093@colorado.edu


YOU CAN USE THESE SCRIPTS WITHOUT ANY RESTRICTION. 


********************************************************************************************************************************

INSTRUCTIONS TO RUN THE SCRIPTS:

    (i) Source code:
        On the command line please run the following command in the directory where the source code "scrabbler.py" resides.
            $ scrabbler.py --word="abcd" --prefix="lib" --suffix="ish"
            or
            $ python scrabbler.py --word="abcd" --prefix="lib" --suffix="ish"

    (ii) Test code:
        To run the test script (test_test.py) please run "pytest" on the command line in the same directory as the source code.
        Also make sure the pytest python module is installed. To do so, run "pip install pytest" on the command line.

********************************************************************************************************************************
SOURCE CODE DESCRIPTION:

The source code is a Python script that lets the user enter a combination of letters and parses a text file that contains several words
and prints out the words who letters can are in the combination of letters entered by the user.

The source code has 5 functions. They are
        1)scrable: This function takes the combination of letters entered by the user and parses the text file to find
                    and print words that can be formed using those letters.

        2)pref: This function takes the prefix entered by the user and parses the text file to find
                 and print words that can be formed using those letters (prefix entered by the user).

        3)suff: This function takes the suffix entered by the user and parses the text file to find
                 and print words that can be formed using those letters (suffix entered by the user).

        4)double_checker: This function checks if the user input is valid or not. This is determined by checking if the entered
                        input has character(s) that have more than 1 occurence.

        4)main: This function calls the above functions and prints out a PrettyTable of the number of occurences of all the
                types (combination of letters, prefix, and suffix).

        Notes: (i) Python modules needed for this source code to work are a)PrettyTable b) itertools.
                    Prettytable can be installed by running "pip install prettytable" on the command prompt.
               (ii) The source code accepts system arguments by using the module argparse. So the module argparse has
                    to be present in the local repository ,if not it has to be installed.
                    To run the Python script, run the following command on the command line:
                    $ scrabbler.py --word="abcd" --prefix="lib" --suffix="ish"

                    or

                    $ python scrabbler.py --word="abcd" --prefix="lib" --suffix="ish"


********************************************************************************************************************************

TEST CODE DESCRIPTION

    The automated test script imports the source code (scrabbler.py) and it is run using the "pytest" Python automated
    testing framework.
    The script contains 5 methods:
        a)test_pref: checks the number of words in the file "words.txt" with the prefix "girl". It has to be 8.
        b)test_suff: checks the number of words in the file "words.txt" with the suffix "uck". It has to be 27.
        c)test_comb: checks the number of words in the file "words.txt" which can be formed using the letters "dB".
                    It has to be 1.
        d)test_incor_suff: checks the output of the script when the suffix entered is "ishh". It needs to result the original
                            source code printing out "Invalid suffix"/"Not a valid suffix" and return -1 to the called function.
                            This is the condition for success.
        e)test_incorr_pref: similar to "test_incor_suff" except this function checks the output of the script when the prefix
                              entered is "libb"
    Notes:
            (i) The "pytest" module has to be installed. You can run "pip install pytest" on the command line to do so.
            (ii) To run the test script, make sure
                    -->the test script is in  the same directory as the source code
                    -->it has to be named with prefix "test_"
                    -->you run the command "pytest" only on the command line.

    Result:
        The result should show that there were 5 test conditions and all of them passed.

***************************************************************************************************************************

