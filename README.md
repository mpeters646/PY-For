# Instructions

Implement these functions in `main.py`:

1. `shortest_names`: takes a list of country names and returns a list of country names that have the shortest length. If there is only one country with the shortest name the list will contain only that country name, otherwise multiple countries should be in the list. Use a for-loop and `len`!

2. `most_vowels`: takes a list of country names and returns a list with the top three countries that have the most vowels in their name. The country with the most vowels should be on position `0` in the list, the country with the second-most on position 1, and so on. If there are multiple countries with the same number of vowels the order does not matter. To sidestep the y-issue: we count `aeiou` as vowels.

3. `alphabet_set`: takes a list of country names and returns a list of country names whose letters can be combined to form the complete alphabet. How short can you get your list to be?
   - Letter case is not relevant, so `'a'` is the same letter as `'A'` with regards to the alphabet.
   - Solutions with 14 or fewer countries are accepted as correct.

> You should write your functions before the if statement at the end of `main.py`. You can call these functions in the code block of that if statement.

## Wincpy Check

Use `wincpy check` for to see if you met all of the requirements for this exercise. Did you pass the test?
