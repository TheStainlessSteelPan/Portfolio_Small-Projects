""" Generates a master tally of votes using the random module. The Pandas Module help in organizing the master_tally dictionary
into a table for data visualization and such. """
import random as rand
import pandas as pd

## Resimulate a school elections for President, Vice President, Councilors
## Convert the generated votes into a dictionary to structure data

#ROSTERS
roster_pres = ['Patroclus', 'Buddha', 'Odysseus', 'Granma']
roster_vpres = ['Girl', 'Boy', 'Gintama', 'Frieren']
roster_council = ['Rose', 'Pumpkin', 'Lily', 'Daisy', 'Oakwood', 'Rubber', 'Sunflower']

#Vote Results Master Sheet and individual sheets
master_tally = {'V_Pres':'' , 'V_VPres': '', 'V_Councilors': [],}
vote_preslist = []
vote_vpreslist = []
vote_council = []
# # len - counts from 1
# # rand.randint - counts from start N to end B+1, to include last digit
# # lists - index starts from 0

x = input("How many students will vote?: ")
stud_votes = int(x)

council_mem = input("How many council members?: ")
member = int(council_mem)

def generatevote(position):
    '''Generates a random integer from the given range'''
    return rand.randrange(0, (len(position)))

def votesim_pres():
    '''Returns a candidate from the given list'''
    return(roster_pres[generatevote(roster_pres)])

def votesim_vpres():
    '''Returns a candidate from the given list'''
    return(roster_vpres[generatevote(roster_vpres)])

def votesim_council():
    '''Returns k number of candidates from list'''
    return(rand.sample(roster_council, member))
    

for i in range(1,stud_votes+1):
    i = votesim_pres()
    vote_preslist.append(i)

for y in range(1, stud_votes+1):
    y = votesim_vpres()
    vote_vpreslist.append(y)
    
for k in range(1, stud_votes + 1):
    k = votesim_council()
    vote_council.append(k)
    
master_tally.update({'V_Pres':vote_preslist, 'V_VPres':vote_vpreslist, 'V_Councilors':vote_council}) 

df = master_tally
converted_df = pd.DataFrame(df)

print(converted_df)
