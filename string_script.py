#!/usr/bin/env python3

#importing necessary packages
import argparse
import pandas as pd
import sys 

#to run this script on command line type in python 3 string_script.py 

# function to calculate k and possible kmers given a string of characters [ATCG] 
def  poss_kmer(k, string):
    ''' 
    This is a function that will caluclate the k value and possible kmers when given a string of characters
    for exmaple: ATTGAG
    
    inputs:
    k: length of kmer of interest
    string: string of characters 
    
    return: possible number of character to the k or number of substrings that
    would fit in the string (integer)
     
    '''
    string_l = len(string) #calculating length of given string and assigning the numerical value as string_l
    poss_a = string_l + 1 - k #possible kmer is either length of given string + 1 - k (i.e. possible number of substrings that would fit within the string)
    poss_b = 4 ** k #or 4 to the k power (i.e. # of possible characters to the k power)
    if poss_a < poss_b: #poss_kmer is the smallest of these two calculations
        return poss_a #if poss_a is smaller than poss_b return poss_a
    else:
        return poss_b #if poss_a is greater than poss_b return poss_b



# function to calculate k and observed kmers given a string of characters [ATCG]        
def obs_kmer(k, string): 
    ''' 
    This is a function that will caluclate the k value and observed kmers given a string of characters
    for exmaple: ATTGAG
    
    inputs:
    k: length of kmer of interest
    string: string of characters 
    
    return: number of possible kmer combinations of length k (integer)
     
    '''
    full_list = [] # create empty data frame that will contain with duplicates
    unique_list = [] # create empty data frame for unique combinations only (i.e. no duplicates)
    count = 0 # create empty counter 
    string_l = len(string) #calculating length of given string and assigning the numerical value as string_l 
    for i in range(1,string_l+1): # indexing with i across all kmer values
        single_k = string[(i-1):(i-1+k)] # defining k value range [1:length(string)] 
        if len(single_k) == k: # only include kmers of the length k we're interested in
            full_list.append(single_k) # add all kmers to the full_list df 
    for item in full_list:
        if item not in unique_list: # select unique combinations
            count += 1 # add 1 to running count every time there is a new unique combination
            unique_list.append(item) #add the uniuqe combinations to the unique list to get list of observed kmers
    return(count) # this is the total number of unquie combinations of k (i.e. total observed kmers)




# function to create table of k, possible, and observed kmers given a string of characters [ATCG]        
def make_df(string): 
    ''' 
    This is a function to create table of possible and observed kmers given a string of characters
    for exmaple: ATTGAG
    
    input: string: string of characters 
    
    return: dataframe with totals of observed and possible kmers that can be used to calculate linguistic complexity (dataframe)
     
    '''
    df_empty = [] # create empty data frame
    string_l = len(string) #calculating length of given string and assigning the numerical value as string_l
    for k in range(1,string_l+1): #indexing with k in range of string lengths 1:string length+1
        df_empty.append([obs_kmer(k, string), poss_kmer(k, string)]) #using previously defined functions to calculate observed and possible kmers then adding to a dataframe
    df = pd.DataFrame(df_empty, index = range(1, string_l+1), columns = ["observed kmers", "possible kmers"]) #assigning index value (k) and column titles to df
    df.loc['Total'] = df.sum() #creating final row that includes totals of observed and possible columns
    df.to_csv(''+string+'_ling_complexity_.csv', index = True)
    print(df) #generating the new df 



#Generating functions to return lists of the observed and possible kmers so that I can continue to use "string" as my input for the linguistic complexity function
# function to generate list of observed kmers that can be totaled for linguistic complexity calculation

def obs_count_list(string):
    '''
    This is a function to generate the total observed kmer values
    
     input: string: string of characters
     
     return: list of observed kmer counts [1, n] (integers)

    '''
    obs_count_list = [] #make an empty list for observed kmer counts to be put in
    for k in range(1, len(string)+1): #for loop to loop thorugh all k values up to the string length 
        obs_count_list.append(obs_kmer(k, string)) #append the list with count of observed kmer each time through loop
    return obs_count_list

# function to generate list of possible kmers that can be totaled for linguistic complexity calculation

def poss_count_list(string):
    '''
 This is a function to generate the total observed kmer values
    
     input: string: string of characters
     
     return: list of possible kmer counts [1, n] (integers)
    '''
    poss_count_list = [] #make an empty list for possible kmer counts to be put in
    for k in range(1, len(string)+1): #for loop to loop thorugh all k values up to the string length 
        poss_count_list.append(poss_kmer(k, string)) #append the list with count of observed kmer each time through loop
    return poss_count_list


#function to caluclate linguistic complexity (i.e. ratio of the sum of observed kmers and sum of possible kmers)

def linguistic_complexity(string):

    ''' 
    This function calculates the linguistic complexity of a given string of characters (total obs/total poss) by calling on the previously defined obs_count_list and poss_count_list
    
    input:string: string of characters
    
    return: linguistic complexity value of the given string (integer)
    ''' 
    obs_poss_ratio =sum(obs_count_list(string)) / sum(poss_count_list(string)) #dividing the sum of observed kmers by the sum of possible kmers 
    print("The linguistic complexity of " +string+ " is", obs_poss_ratio)


# function to output file 
#def main(args): 
    ''' 
    This function reads in a file (.txt) of strings and outputs
    a new (.csv) file with the table of k, possible, and observed kmers and to prints out the calculated linguistic complexity value onto the command line. 
    
    input: .txt file containing string sequences
    
    returns:
    CSV file containing k values, observed and possible kmers
    Linguistic complexity value as a message on the command line
    
    '''

def main(args):
  for string in list: #using slist since list is a function
    make_df(string) # using predefined function make_df to output dataframe containing observed and possible kmers
    linguistic_complexity(string) #calculate linguistic complexity using predefined linguistic_complexity function and outputs it to command line

if __name__ == '__main__':
  parser = argparse.ArgumentParser() #place to put your arguments
  parser.add_argument('filename') #adding arguments
  args = parser.parse_args()
  with open(args.filename) as file: #reading in the txt file
    list = file.read().splitlines()
    main(args)




#On the terminal, type the following to:
#Run script: python3 string_script.py 'string'
#Make script executable: chmod +x string_script.py 
