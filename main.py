from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Write your functions here. """
def shortest_names(countries):
  shortest_countries = []
  for country in countries:
    if len(country) == len(min(countries, key=len)):
      shortest_countries.append(country)
  print(shortest_countries)
  return shortest_countries



def most_vowels(countries):
  most_vowel_list = sorted(countries, key=lambda x: sum(1 for y in x if y in 'aeiouAEIOU'), reverse=True)

  print(most_vowel_list[0:3])
  return most_vowel_list[0:3]

def alphabet_set(countries):
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  for c in countries:
    return c

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()

    """ Write the calls to your functions here. """
    shortest_names(countries)
    most_vowels(countries)
    alphabet_set(countries)


""" TEST CODE """



""" Most vowels """
# South Georgia and the South Sandwich Islands (14)
# Micronesia, Federated States of (12)
# United States Minor Outlying Islands (12)
# The Democratic Republic of Congo (11)
# British Indian Ocean Territory (11)
# Equatorial Guinea (10)
# Saint Pierre and Miquelon (10)
# Saint Vincent and the Grenadines (10)
