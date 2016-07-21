import random

places = ["Italian ", "Fujian ", "Sichuan ", "French ", "Filipino-style ",
          "American ", "Mediterranean ", "Southwest ", "New York ",
          "Vietnamese ", "Indian "]
adjectives = ["spicy ", "sweet and sour ", "creamy ", "cheesy ", "crispy ", "juicy ",
              "gourmet ", "authentic ", "steamed ", "roasted ",
              "chopped ", "classic "]
foods = ["chicken", "beef", "spinach", "broccoli and beef", "pork",
         "greens", "seafood", "tofu", "mushrooms", "fried rice",
         "tuna", "salmon", "mystery meat", "Garden salad"]
places_used = []
adjectives_used = []
foods_used = []

foods_length = len(foods)
adjectives_length = len(adjectives)
places_length = len(places)

places_index = -1
adjectives_index = -1
foods_index = -1

once = False

#simple
for i in range(10):
    number_list = i + 1
    places_index = random.randint(0,places_length - 1)
    adjectives_index = random.randint(0,adjectives_length - 1)
    foods_index = random.randint(0,foods_length - 1)
    print(str(number_list)+ ". " + places[places_index] + adjectives[adjectives_index] + foods[foods_index])
    
#no repeats
for i in range(10):
    number_list = i + 1
    places_index = random.randint(0,places_length - number_list)
    adjectives_index = random.randint(0,adjectives_length - number_list)
    foods_index = random.randint(0,foods_length - number_list)
    print(str(number_list)+ ". " + places[places_index] + adjectives[adjectives_index] + foods[foods_index])
    places.remove(str(places[places_index]))
    adjectives.remove (str(adjectives[adjectives_index]))
    foods.remove(str(foods[foods_index]))

# menu generator - doesn't work
for i in range(10):
    once = True
    number_list = i+1
    while once == True:
        if((places[places_index] not in places_used)and(adjectives[adjectives_index] not in adjectives_used)and(foods[foods_index] not in foods_used)):
            places_index = random.randint(0,places_length - 1)
            places_used.append(str(places[places_index]))
            adjectives_index = random.randint(0,adjectives_length - 1)
            adjectives_used.append(str(adjectives[adjectives_index]))
            foods_index = random.randint(0,foods_length - 1)
            foods_used.append(str(foods[foods_index]))
            print(str(number_list)+ ". " + places[places_index] + adjectives[adjectives_index] + foods[foods_index])
            once = False
            places_index = -1
            adjectives_index = -1
            foods_index = -1
    


