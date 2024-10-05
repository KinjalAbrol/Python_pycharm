class user:
      pass

#1 object and second class and class needed ()
user_1 = user()
# cases:
#CamelCase: every letter of new word is capitalised and no space.
#camelCase: ist word letter is smaller and other are capitalised.
#snake_case: every letter is smaller and separated by _ .

# adding attributes by own:
class user:
    pass

user_1 = user()
user_1.id = "001"
user_1.username = "Angela"
print(user_1.id)
print(user_1.username)
# if we have more than 1 attribute
class user:
    pass

user_1 = user()
user_1.id = "001"
user_1.username = "Angela"
print(user_1.id)
print(user_1.username)
user_2 = user()
user_2.id = "002"
user_2.username = "jack"
print(user_2.id)
print(user_2.username)
# but if we have more and more attributes
# using special function init(it makes this init funcion call everytime with every object you made with class)
class user:
      def __init__(self):
          print("new user created")

user_1 = user()
user_1.id = "001"
user_1.username = "Angela"
print(user_1.id)
print(user_1.username)
user_2 = user()
user_2.id = "002"
user_2.username = "jack"
print(user_2.id)
print(user_2.username)
# init func with more parameters
# this make code smaller and convinient
class user:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name


user_1 = user("001", "Angela")
print(user_1.id)
print(user_1.username)
user_2 = user("002", "jack")
print(user_2.id)
print(user_2.username)

# init function if have defualt value give = 0
class user:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0

user_1 = user("001", "Angela")
print(user_1.id)
print(user_1.username)
print(user_1.followers)
user_2 = user("002", "jack")
print(user_2.id)
print(user_2.username)
print(user_2.followers)
# add methods
class user:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = user("001", "Angela")
print(user_1.id)
print(user_1.username)

user_2 = user("002", "jack")
print(user_2.id)
print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

