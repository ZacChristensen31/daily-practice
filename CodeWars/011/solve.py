# Problem comes from CodeWars https://www.codewars.com/kata/525c65e51bf619685c000059/python
# Solved on Friday May 20th, 2022

from typing import Dict

"""
    Given a recipe (a list of ingredients and their quantities) and a list of available ingredients,
    what is the maximum number of recipes that can be created?
"""
def solve(recipe: Dict[str, int], available: Dict[str, int]) -> int:
    output = 2 ** 32
    for key in recipe.keys():
        new_output = available.get(key, 0) // recipe.get(key, 0)
        if new_output < output:
            output = new_output

    return output

if __name__ == '__main__':
    assert solve(
        {'flour': 500, 'sugar': 200, 'eggs': 1},
        {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}
    ) == 2

    assert solve(
        {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100},
        {'sugar': 500, 'flour': 2000, 'milk': 2000}
    ) == 0

    assert solve(
        {'flour': 20, 'sugar': 20, 'eggs': 20, 'milk': 20},
        {'flour': 200, 'sugar': 200, 'eggs': 200, 'milk': 200}
    ) == 10