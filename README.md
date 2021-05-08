# Determining Linguistic Complexities (Exam 4)
Exam 4 - Python

Hannah Haskell

BIO539



## Python script: string_script.py 

This script can be used to calculate the linguistic complexity of a given string sequence provided in a given txt file. The output of the script is a CSV file containing a dataframe with k value, observed and possible kmers as well as a print out of the linguistic complexity value on the command line.

### Useage:
python3 string_script.py 'seq_test.txt'


## Python test script: test_string_script.py

This script tests various sequence strings on functions defined within string_script.py that were used to calculate linguistic complexity. 9 out of 9 tests passed.

### Useage:
py.test


## Example sequence data file (seq_test.txt)
Txt file containing the following 3 example sequence strings:

AGCTGAAA

GTTTC

ACCT

to run use this script input "python3 string_script.py 'seq_test.txt'" into the command line.
