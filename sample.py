""" Example of use of Interface metaclass """

from typing import Callable
from interface import Interface


# Interface definition
class IAnimal(metaclass=Interface):
    sound:   Callable
    eat:     Callable
    excrete: Callable
    name:    property


# Definition of human
class Human(IAnimal):

    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    @property
    def name(self):
        return self._name + " " + self._surname

    def sound(self):
        return "Halo, halo, co se stalo?"

    def eat(self, food):
        print('<--', food)
        self._food = food

    def excrete(self):
        try:
            print('waste of', self._food, '-->')
            return self._food
        except AttributeError:
            print(f"[{self.name}] I'am Starving :(")
            return None


# Definition of dog
class Dog(IAnimal):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def sound(self):
        return "Haf haf haf"

    def eat(self, food):
        print('<--', food)
        self._food = food

    def excrete(self):
        try:
            print('waste of', self._food, '-->')
            return self._food
        except AttributeError:
            print(f"[{self.name}] Haf haf haf :'(")
            return None


# Definition of fish
class Fish(IAnimal):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def sound(self):
        return "Glo glo glo"

    def eat(self, food):
        print('<--', food)
        self._food = food

    def excrete(self):
        try:
            print('waste of', self._food, '-->')
            return self._food
        except AttributeError:
            print(f"[{self.name}] Haf haf haf :'(")
            return None


# Fish class not satisfying IAnimal interface requirements
# no sound() method defined
class FishA(IAnimal):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def eat(self, food):
        print('<--', food)
        self._food = food

    def excrete(self):
        try:
            print('waste of', self._food, '-->')
            return self._food
        except AttributeError:
            print(f"[{self.name}] Haf haf haf :'(")
            return None

"""ERROR MESSAGE: NotDefinedInterfaceError
Traceback (most recent call last):
  File "sample.py", line 86, in <module>
    kaprik = Fish("Kapřík")
  File "/home/mgrunwal/Desktop/meta/interface.py", line 58, in __call__
    mcs.__interface_check__()
  File "/home/mgrunwal/Desktop/meta/interface.py", line 48, in __interface_check__
    raise NotDefinedInterfaceError(undefined_items)
interface.NotDefinedInterfaceError: Required attributes [sound:typing.Callable] are not defined.
"""


# Fish class not satisfying IAnimal interface requirements
# Attribute name() has to be property not callable
class FishB(IAnimal):

    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def sound(self):
        return "Glo glo glo"

    def eat(self, food):
        print('<--', food)
        self._food = food

    def excrete(self):
        try:
            print('waste of', self._food, '-->')
            return self._food
        except AttributeError:
            print(f"[{self.name}] Haf haf haf :'(")
            return None

"""ERROR MESSAGE: InvalidTypeInterfaceError
Traceback (most recent call last):
  File "sample.py", line 120, in <module>
    kaprik = FishB("Kapřík")
  File "/home/mgrunwal/Desktop/meta/interface.py", line 58, in __call__
    mcs.__interface_check__()
  File "/home/mgrunwal/Desktop/meta/interface.py", line 51, in __interface_check__
    raise InvalidTypeInterfaceError(invalid_items)
interface.InvalidTypeInterfaceError: Invalid attributes "attribute [name] is type <class 'property'> not <function FishB.name at 0x7f5e8b380280>".
"""


pepa = Human("Pepa", "Novak")
alik = Dog("Alik")
kaprik = Fish("Kapřík")

for z in [pepa, alik, kaprik]:
    print("---------------------------------")
    print(z.name, f"({z.__class__.__name__})", f'"{z.sound()}"')
    f'"{z.sound()}"'
    z.eat('some delicious food')
    z.excrete()


"""CONSOLE OUTPUT:
Pepa Novak (Human) "Halo, halo, co se stalo?"
<-- some delicious food
waste of some delicious food -->
---------------------------------
Alik (Dog) "Haf haf haf"
<-- some delicious food
waste of some delicious food -->
---------------------------------
Kapřík (Fish) "Glo glo glo"
<-- some delicious food
waste of some delicious food -->
"""
