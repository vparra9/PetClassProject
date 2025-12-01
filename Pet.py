class myPet:
   def  __innit__(self, name = None, age = None, hunger = 0)
        # Ask user for input
        self.name = name
        self.age = age
        self.hunger = 0 # pet starts full

    def feed(self):
        if self.hunger == 1:
            self.hunger == 0
            print(f"You fed {self.name}.") 
        else:
            print(f"{self.name} is full!")
    
    def play(self): 
        if self.hunger == 1:
            print(f"{self.name} is too hungry to play! Feeding them first...")
            self.feed()
        else
            self.hunger = 1 #pet becomes hungry after playing
            print(f"{self.name} played fetch and had a lot of fun!")

    def main():
        # Step 1: Create a pet
        name = input("Enter your pet's name: ")
        age = int(input("Enter your pets age: "))
        my_pet = Pet(name, age)

    
            


