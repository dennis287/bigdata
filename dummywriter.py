import sys
import random

countries = ['usa', 'canada', 'netherlands']

file = open("input5milj.txt", "w")
for _ in range(5000000):
    file.write(random.choice(countries) + " " + str(random.randint(10,35)) + "\n")
file.close()
