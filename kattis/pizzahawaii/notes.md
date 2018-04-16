A sets/dictionaries problem.

Build up a dictionary `d` of possible translations for each foreign word.

Whenever a new pizza is read in, the possible translations for each `w` in the foreign language should be the set intersection of the previous translations (`d[w]`) and the english ingredients in this pizza.

After this is done for all pizzas, you need to run through each `w` in `d` and remove all possible candidate translations that appear in other pizzas without `w`. ie. For every input pizza, if `w` is not in the foreign ingredients, then you should remove all the english ingredients for that pizza from `d[w]`. 

This runs in 0.02s in python3 (the fastest python3 submission on kattis!).
