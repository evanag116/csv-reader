animal = input("Enter an animal: ")
if animal[-1] != "s":
    animal = animal + "s"

try:
    with open(f"data/{animal}.csv") as animals:
        for line in animals.readlines()[1:]:
            pet = line.strip().split(", ")
            print(f"{pet[0].title()} is a {pet[1].title()} year old {pet[2]}.")


except Exception as e:
    print(f"We apologize, {animal} are not available at this time.")
