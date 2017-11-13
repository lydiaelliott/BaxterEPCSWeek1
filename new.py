breed = ["Huskey","Corgi","Lab","Boston Terrior","Poodle"]
name = ["Izzy","Gus","Chloe","Chilli","Angel"]
toy = ["tennis ball", "squeaky duck","frizbee","plastic bone","bouncy ball"]
food = ["tase of the wild","purina","natural balance","pedigree","blue buffalo"]
bedcolor = ["purple","blue","green","red","pink"]

def selection(getUserSelection)
    if selection == 5: print self.randomName and self.randomBreed
    if selection == 6: print self.RandomToy and self.RandomFood and self.RandomBedcolor

    class Puppy:
        def __init__(self):
            self.assignRandomName()
            self.assignRandomBreed()
            self.assignRandomFood()
            self.assignRandomToy()
            self.assignRandomColorbed()

        def assignRandomName(self):
                self.name = random.choice(names)
        def assignRandombreed(self):
                self.breed = random.choice(breed)
        def assignRandomfood(self):
                self.food = random.choice(food)
        def assignRandomtoy(self):
                self.favoritetoy = random.choice(toy)
        def assignRandomcolorbed(self):
                self.colorbed = random.choice(bedcolor)

inputQuestions = [
        "For PUPPIES BY NAME AND BREED, type 5",
        "For PUPPIES BY FOOD TOY AND BEDCOLOR, type 6",
]

puppies = [Puppy(), Puppy()]

def getUserSelection():
    for inputQuestion in inputQuestions:
        print (inputQuestion)
    return int(input("Enter input here:" ))


def printHEADER():
    print ("Puppy facts")
def printSortByName(puppyvariables):

    main()
