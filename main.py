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
  most_vowel_list = []
  max_length = 0
  for country in countries:
      vowel_length = len([el for el in country.lower() if el in ['a', 'e', 'i', 'o', 'u']])

      # print(vowel_length, country)

      if vowel_length > max_length:
          max_length = vowel_length
          most_vowel_list.append(country)

  most_vowel_list.reverse()
  print(most_vowel_list[0:3])
  return most_vowel_list[0:3]

def alphabet_set(countries):
  for c in countries:
    return c

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()

    """ Write the calls to your functions here. """
    shortest_names(countries)
    most_vowels(countries)
    # alphabet_set(countries)


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
