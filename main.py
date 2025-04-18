from pet import Pet

def main():
    print("Creating pet: Max 🐶")
    max_pet = Pet("Max")

    print("Max is eating...")
    max_pet.eat()

    print("Max is playing...")
    max_pet.play()

    print("Max is sleeping...")
    max_pet.sleep()

    print("Teaching Max new tricks...")
    max_pet.train("roll over")
    max_pet.train("play dead")

    print("\nMax's current status:")
    max_pet.get_status()

    print("\nTricks:")
    max_pet.show_tricks()

if __name__ == "__main__":
    main()
