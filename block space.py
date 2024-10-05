# simple
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


if game_level < 5:
        new_enemy = enemies[0]
        print(new_enemy)
# block space
game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# block space
my_global_var = 1


def my_function():
    # Only accessible within my_function()
    my_local_var = 2


for _ in range(10):
    # Accessible anywhere
    my_block_var = 3


# prime number example
def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False

    # Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False

    # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return True