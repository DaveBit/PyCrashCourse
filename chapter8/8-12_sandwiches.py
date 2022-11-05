def ordered_sandwich(*ingredients):
    """This functions prints the ingredients of the sandwich which has been ordered"""
    print("\nIngredients: ")
    for ingredient in ingredients:
        print("- " + ingredient)


ordered_sandwich('lechuga', 'potato', 'egg', 'tomato', 'ketchup')
ordered_sandwich('lettuce', 'cheese', 'bacon')

