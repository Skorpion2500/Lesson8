class Animals:
    def __init__(self, name, danger):
        self.name = name
        self.danger = danger
    
    def danger(self):
        if self.danger == 'dangerous' or self.danger == 'not dangerous':
            print('It is',self.danger)

class Mammals(Animals):
    def __init__(self, name, danger,tail):
        super().__init__(name, danger)
        self.tail = tail

    def say_tail(self):
        if self.tail == 'yes':
            print('I have tail')
        if self.tail == 'no':
            print('I have not tail')

class Human(Mammals):
    def __init__(self, name, gender, age):
        super().__init__(name, danger='not dangerous',tail='no')
        self.age = age
        self.gender = gender
    
    def say_age(self):
        print('I am', self.age)
    
    def make_sound(self):
        print('Hi')

class Cat(Mammals):
    def __init__(self, name):
        super().__init__(name,danger='not dangerous',tail='yes')
    
    def make_sound(self):
        print('Meow')

class Dog(Mammals):
    def __init__(self, name):
        super().__init__(name,danger='not dangerous',tail='yes')
    
    def make_sound(self):
        print('Woof')

class Student(Human):
    def __init__(self, name, gender, age, homework):
        super().__init__(name, gender, age)
        self.homework = homework
        
    def __gt__(self, other):
        return self.homework > other.homework
    def __lt__(self, other):
        return self.homework < other.homework
    def __ge__(self, other):
        return self.homework >= other.homework
    def __le__(self, other):
        return self.homework <= other.homework
    def __eq__(self, other):
        return self.homework == other.homework
    def __ne__(self, other):
        return self.homework != other.homework

Snejok = Cat('Snejok')
Ram = Dog('Ram')
Tom = Student('Tom', 'male', 19, 5)
Bob = Student('Bob', 'male', 20, 6)
for i in (Snejok,Ram, Tom, Bob):
    i.make_sound()
print(Tom > Bob)
print(Tom < Bob)
print(Tom >= Bob)
print(Tom <= Bob)
print(Tom == Bob)
print(Tom != Bob)