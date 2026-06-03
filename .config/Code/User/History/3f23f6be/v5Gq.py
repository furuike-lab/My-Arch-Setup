from abc import ABC, abstractmethod

class Animal():
    def __init__(self, name):
        self.name = name
        @abstractmethod
        def cry(self):
            pass

class Dog(Animal):
    def cry(self):
        print(self.name, end='')
        print("(dog) cries as bow-wow.")

class Cat(Animal):
    def cry(self):
        print(self.name, end='')
        return "(cat) cries as meow."

def main():
    inu = Dog("pochi")
    neko = Cat("mike")
    
    inu.cry()
    neko.cry()

if __name__ == '__main__':
    main()