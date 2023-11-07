class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

if __name__ == "__main__":
    pet = Pet()

    name = input("Enter the pet's name: ")
    pet.set_name(name)

    animal_type = input("Enter the type of animal (e.g., Dog, Cat, Bird): ")
    pet.set_animal_type(animal_type)

    age = input("Enter the pet's age: ")
    pet.set_age(age)

    print("\nPet Details:")
    print("Name:", pet.get_name())
    print("Type:", pet.get_animal_type())
    print("Age:", pet.get_age())
