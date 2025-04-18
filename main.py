from pet import Pet

# Creating Jim the pet
jim = Pet("Jim", "Dog")

print("🐶 Creating pet: Jim")
jim.eat()
jim.play()
jim.sleep()
jim.train("Roll Over")
jim.train("Play Dead")
jim.dance()  # Bonus action
jim.talk()   # Random responses
print("\n📢 Jim's current status:")
jim.get_status()
jim.show_tricks()
