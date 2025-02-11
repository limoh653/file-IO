# cars= input("what is the model of your car?")

# file= open('cars.txt','a')
# file.write(f'{cars}\n')
# file.close()

# with open("cars.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print(f"My car is a, {line.rstrip()}")

# with open("cars.txt", "r") as file:
#     for line in file:
#         print(f"My car is a, {line.rstrip()}")

cars = []

with open("cars.txt", "r") as file:
    for line in file:
        cars.append(line.rstrip())

for car in sorted(cars):
    print(f"My car is a, {car}")tou