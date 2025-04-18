import random

class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type  # Dog, Cat, or Robot
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []  # List of tricks learned

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"🍖 {self.name} is eating! Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"💤 {self.name} is sleeping... Energy: {self.energy}")

    def play(self):
        if self.energy > 0:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"🎾 {self.name} is playing! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"😴 {self.name} is too tired to play!")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = max(0, self.happiness - 1)
        print(f"🎓 {self.name} learned '{trick}'! Happiness: {self.happiness}")

    def show_tricks(self):
        if self.tricks:
            print(f"🧠 {self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"🤔 {self.name} hasn't learned any tricks yet.")

    def dance(self):
        print(f"💃 {self.name} is dancing happily!")

    def talk(self):
        responses = ["Hello, human! 🐾", "I'm hungry... 🍽️", "Let's play! 🎾", "Time for a nap... 😴"]
        print(f"🗣️ {self.name} says: {random.choice(responses)}")

    def get_status(self):
        print(f"📊 {self.name}'s Status -> Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}, Tricks: {self.tricks}")
