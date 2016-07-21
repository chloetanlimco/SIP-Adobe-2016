import random

preceding = ["The", "Some ", "Incision ", "Uncommon ", "Floppy "]
adjectives = ["Amazing ", "Greatest ", "Random "]
objects = ["People", "Stones"]

preceding_length = len(preceding)
adjectives_length = len(adjectives)
objects_length = len(objects)

preceding_index = -1
adjectives_index = -1
objects_index = -1


    
#no repeats
for i in range(2):
    number_list = i + 1
    preceding_index = random.randint(0,preceding_length - number_list)
    adjectives_index = random.randint(0,adjectives_length - number_list)
    objects_index = random.randint(0,objects_length - number_list)
    print(str(number_list)+ ". " + places[places_index] + adjectives[adjectives_index] + foods[foods_index])
    preceding.remove(str(preceding[preceding_index]))
    adjectives.remove (str(adjectives[adjectives_index]))
    objects.remove(str(objects[objects_index]))
