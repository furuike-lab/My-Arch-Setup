class Animal():
    def __init__(self, name):
        self.name = name
        def cry(self):
            pass
        @classmethod
        def animal_sound(self, animal):
            print(animal.cry())

class Dog(Animal):
    def cry(self):
        return "bow-wow"

class Cat(Animal):
    def cry(self):
        print(self.name, end='')
        return "(cat) cries as meow."

def animal_sound(animal):
    print(animal.cry())

def main():
    inu = Dog("pochi")
    neko = Cat("mike")
    
    animal_sound(inu)
    animal_sound(neko)

if __name__ == '__main__':
    main()