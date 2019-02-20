#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # Loop through keys in recipe
    # Calculate ingredients[key] // recipe[key] and store result in a batch list
    # min(list) = max number of batches since max_batch dictated my limiting ingredient
    # runtime O(n); space O(n)
    batch = []
    for ingredient in recipe.keys():
        if ingredient in ingredients.keys():
            batch.append(ingredients[ingredient] // recipe[ingredient])
        else:
            return 0  # missing necessary ingredient
    return min(batch)


recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10},
               {'milk': 198, 'butter': 52, 'cheese': 10})


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
