def cookbook(*args):
    cuisine_dict = {}
    recipe_dict = {}
    for name, cuisine, my_list in args:
        recipe_dict[name] = my_list
        if cuisine not in cuisine_dict:
            cuisine_dict[cuisine] = [name]
        else:
            cuisine_dict[cuisine].append(name)
    message = ""
    for cuisines in sorted(cuisine_dict.items(), key = lambda x: (-len(x[1]), x[0])):
        message+=f"{cuisines[0]} cuisine contains {len(cuisines[1])} recipes:\n"
        for cuisine in sorted(cuisines[1]):
            message+=f"  * {cuisine} -> Ingredients: {', '.join(recipe_dict[cuisine])}\n"

    return message

print(cookbook(("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
                      ("Chicken Curry", "Indian", ["chicken", "curry paste", "coconut milk", "rice"]),
                      ("Caesar Salad", "American", ["romaine lettuce", "croutons", "parmesan", "caesar dressing"]),
                      ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
                      ("Mushroom Risotto", "Italian", ["arborio rice", "mushrooms", "onion", "parmesan", "broth"]),
                      ("Tacos", "Mexican", ["tortillas", "ground beef", "lettuce", "tomato", "cheese"]),
                      ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"]),
                      ("Chicken Alfredo", "Italian", ["fettuccine", "chicken", "alfredo sauce", "broccoli"])))

