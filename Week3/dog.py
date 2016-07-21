class Dog():

        #constructor function
        def __init__(self, furcolor, weight, eyecolor, name):
                self.furcolor = furcolor
                self.weight = weight
                self.eyecolor = eyecolor
                self.name = name

        #functions
        def bark(self):
            print("Woof")

        def wag(self):
            print("Wagging Tail")

        def run(self):
            print("Your dog is running away")

Toto = Dog("Brown", 25, "blue", "Toto")

Toto.run()
