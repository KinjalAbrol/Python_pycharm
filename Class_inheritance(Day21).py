# simple example:
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#     def breathe(self):
#         print("Inhale, Exhale.")
#
# class Fish:
#     def swim(self):
#         print("moving in water.")
#
# nemo = Fish()
# nemo.swim()
# using class inheritance:-
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#     def breathe(self):
#         print("Inhale, Exhale.")
#
# class Fish(Animal):#it allows anything in fish class to inherit from super class animal.
#     def __init__(self):
#         super().__init__()
#
#     def swim(self):
#         print("moving in water.")
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)
#inherit a method  and add something new to it.
class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale, Exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()# everything breathe method from superclass.
        print("doing this underwater")#adding some extra.

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)