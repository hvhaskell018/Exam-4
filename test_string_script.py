# python3 string_script.py py.test
# to run the whole script type python3 string_script.py


#test multiple inputs (e.g. large k or small k)

from string_script import * #the file we are testing is string_script, we are testing these things after importing this script 

import pandas as pd 

# test obs_kmer function 1
def test_obs_kmer_1():
  k = 6
  string = 'ATTTGGATT'
  actual_result = obs_kmer(k, string)
  expected_result = 4
  assert actual_result == expected_result
  
  # test obs_kmer function 2
def test_obs_kmer_2():
  k = 6
  string = 'ACCGAT'
  actual_result = obs_kmer(k, string)
  expected_result = 1
  assert actual_result == expected_result


def test_obs_kmer_3():
  k = 20
  string = 'ACCTAT'
  actual_result = obs_kmer(k, string)
  expected_result = 0
  assert actual_result == expected_result

# test poss_kmer function 1
def test_poss_kmer_1():
  k = 1
  string = 'ATTTGGATT'
  actual_result = poss_kmer(k, string)
  expected_result = 4
  assert actual_result == expected_result


# test poss_kmer function 2
def test_poss_kmer_2():
  k = 3
  string = 'ATGGATT'
  actual_result = poss_kmer(k, string)
  expected_result = 5
  assert actual_result == expected_result
  
def test_poss_kmer_3():
  k = 4
  string = 'AGT'
  actual_result = poss_kmer(k, string)
  expected_result = 0
  assert actual_result == expected_result

#testing linguistic_complexity
def test_linguistic_complexity_1():
  string = 'ATTTGGATT'
  ling_actual = linguistic_complexity(string)
  ling_expected = print("The linguistic complexity of " "+ATTTGGATT+" " is", 0.875)
  assert ling_actual == ling_expected
  
def test_linguistic_complexity_2():
  string = 'ACTAA'
  ling_actual = linguistic_complexity(string)
  ling_expected = print("The linguistic complexity of " "+ACTAA+" " is", 0.9285714285714286)
  assert ling_actual == ling_expected


def test_linguistic_complexity_3():
  string = 'ACCC'
  ling_actual = linguistic_complexity(string)
  ling_expected = print("The linguistic complexity of " "+ACCC+" " is", 0.7)
  assert ling_actual == ling_expected


