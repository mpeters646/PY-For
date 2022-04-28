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
  # print(shortest_countries)
  return shortest_countries



def most_vowels(countries):
  most_vowel_list = sorted(countries, key=lambda x: sum(1 for y in x if y in 'aeiouAEIOU'), reverse=True)

  # print(most_vowel_list[0:3])
  return most_vowel_list[0:3]

def alphabet_set(countries):
  '''
    * Maak een lege lijst Alphabeth, hier kunnen we opslaan welke letters we al hebben gevonden.
    * Maak een lege lijst Countries_in_alphabeth, hier kunnen we de landen opslaan die we gebruikt hebben voor ons alfabet.
    * Per land, per letter van dat land, kijken we of die letter al in onze lege lijst Alphabeth zit, zo niet, voeg die letter dan toe aan onze lijst Alphabeth, en voeg het land toe aan lijst Countries_in_alphabeth, ga verder voor de rest van de letters van het land, en voeg ze eventueel toe aan lijst Alphabeth.
    * Wanneer onze lijst Alphabeth de lengte van het alfabet heeft, dan zijn we klaar.
  '''

  alphabet = []
  countries_in_alphabet = []

  for country in countries:
      for char in country:
          if char.lower() not in alphabet and char.isalpha():
              alphabet.append(char.lower())
      if country not in countries_in_alphabet:
          countries_in_alphabet.append(country)
      if len(alphabet) == 26:
          break
  print(alphabet.sort())
  print(countries_in_alphabet)
  return countries_in_alphabet


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()

    """ Write the calls to your functions here. """
    shortest_names(countries)
    most_vowels(countries)
    alphabet_set(countries)
