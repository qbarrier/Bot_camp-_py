bouffe = {
    "sandwich" : {
        "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
        "meal" : "lunch",
        "prep_time" : "10 minutes"
    },
    "cake" : {
        "ingredients" : ["flour", "sugar", "eggs"],
        "meal" : "dessert",
        "prep_time" : "60 minutes"
    },
    "salad" : {
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "lunch",
        "prep_time" : "10 minutes"
    }
}

def recipe_print(recipe):
    for x in bouffe:
        if x == recipe:
            print("Ingredients list :" , bouffe[recipe].get("ingredients"))
            print("To be eaten for the", bouffe[recipe].get("meal"))
            print("Takes",bouffe[recipe].get("prep_time") , "of cooking")
            break
    else:
        print("Please look the cookbook to find one recipe")
    x = 0

def cookbook():
    for x in bouffe:
        print("Recipe for " + str(x))
        print("Ingredients list :" , bouffe[x].get("ingredients"))
        print("To be eaten for the", bouffe[x].get("meal"))
        print("Takes",bouffe[x].get("prep_time") , "of cooking\n")
    x = 0

def delrecipe(recipe):
    for x in bouffe:
        if x == recipe:
            del bouffe[recipe]
            break
    else:
        print("Please look the cookbook to find one recipe")
    x = 0

def addrecipe(name, ing, time, meal):
    bouffe[name] = {'ingredients' : ing.split(), 'meal' : meal, 'prep_time' : time}
    print("You add a new recipe !!!" + name)
    recipe_print(name)



print("Please select an option by typing the corresponding number:")
print("1: Add a recipe")
print("2: Delete a recipe")
print("3: Print a recipe")
print("4: Print the cookbook")
print("5: Quit")

while True:
    choose = input("Select 5 if you want to quit\n")

    if choose == "5":
        print("Cookbook Close")
        quit()
    elif choose == "1":
        addrecipe(input("name :\n"), input("ingredients : separate by space\n"), input ("time for preparation\n"), input("meal: \n"))
    elif choose == "2":
        test = input("Please enter the recipe's name who want to delete:")
        delrecipe(test)
    elif choose == "3":
        test = input("Please enter the recipe's name to get its details:")
        recipe_print(test)
    elif choose == "4":
        cookbook()
