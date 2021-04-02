import numpy
import random
import json

min_num = input("Please enter the minimum size of the number.")
max_num = input("Please enter the maximum size of the number.")

min_num = int(min_num)
max_num = int(max_num)

random_number = random.randrange(min_num, max_num)

with open('json/number.json', 'r') as f:
    number_to_input = json.load(f)
number_to_input["number"] = random_number
with open('json/number.json', 'w') as f:
    json.dump(number_to_input, f, indent=4)
    print(random_number)
