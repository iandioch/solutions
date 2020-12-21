import sys
from collections import defaultdict
from functools import reduce

def parse_input():
    for line in sys.stdin.readlines():
        ingredients, allergens = line.strip().split('(contains')
        ingredients = ingredients.split()
        allergens = [a.strip() for a in allergens[:-1].split(',')]
        yield (ingredients, allergens)

def identify_allergens(foods):
    print(foods)
    food_ingredients = [set(food[0]) for food in foods]
    food_allergens = [set(food[1]) for food in foods] # map 0 to [dairy, fish]
    allergen_map = defaultdict(set) # map "dairy" to set(0, 1)
    ingredient_map = defaultdict(set) # map "mxmxvkd" to set(0, 1, 3)

    poss_allergens = defaultdict(set) # maps 'mxmxvkd' to set('dairy')

    for i, ingredients in enumerate(food_ingredients):
        for ing in ingredients:
            ingredient_map[ing].add(i)
    for i, allergens in enumerate(food_allergens):
        for al in allergens:
            allergen_map[al].add(i)

    print(ingredient_map)
    print(allergen_map)

    for a in allergen_map:
        intersection = reduce(lambda p, q: p.intersection(q), (food_ingredients[x] for x in allergen_map[a]))
        for ing in intersection:
            poss_allergens[ing].add(a)

    print(poss_allergens)
    no_allergen = set(ingredient_map) - set(poss_allergens)
    return sum(len(ingredient_map[a]) for a in no_allergen)


def main():
    foods = list(parse_input())
    print(identify_allergens(foods))



main()
