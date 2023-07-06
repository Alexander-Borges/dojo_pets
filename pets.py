#   For this assignment, you'll be asked to create a Ninja class and a Pet class. Your Ninjas will be able to have a pet - and you can even practice using inheritance by creating sub-classes of pets, if you're ready to stretch yourself!
class Pet:
    #implement __init__(name, type, tricks):
    def __init__(self,name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

# sleep() Increase the pet's energy by 25
    def sleep(self):
        self.energy += 25
        return self
# eat() Increase the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

# play() - Increase the pet's health by 5
    def play(self):
        self.health += 5
        self.energy -=15
        return self

# noise() - print out the pet's sound
    def noise(self):
        print(self.noise)



class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )        	
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self. treats = treats = treats 
        self.pet_food = pet_food
        self.pet = pet 

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
    
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print('We need more pet food.')
        return self

    def bathe(self):
        self.pet.noise()
    
dog_treats = ['Cheeze Whiz', 'Biscuits','Bones']
dog_food = ['salmon','lamb', 'rice']

biscuit = Pet('Biscuit','Dog', ['bites people', 'is tiny'], 'Ruff')

Alex = Ninja('Alex','Borges', dog_treats, dog_food, biscuit)

Alex.feed();
Alex.feed();
Alex.feed();
Alex.feed();


# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method


