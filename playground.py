# my_list = [1,2,3,4,5,6,7,8]
# for i in range(len(my_list)):
    # print(my_list[i])

#     bird = {
#         'feathers': "blue",
#         'wings': 2,
#         'name': "floppy",
#         'friends': ["Tom", "Tweety", "Woodie"]
# }
# for thing in bird:
    # print(thing, bird[thing])

#
# 2D Data Types
# canvas = [
#     [2,3,5,4,6],
#     [6,7,4,7,9],
#     [3,4,3,2,1],
#     [8,8,6,3,1]
# ]
# print(canvas[1][4])

# Objects w/ Lists
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# print(sports_directory['soccer'][1])

#loop through sports directory & print out all the bball and soccer players
# for sport in sports_directory:
    # print(sport)
    # print(sports_directory[sport])
    # for i in range(len(sports_directory[sport])):
    #     print(sports_directory[sport][i])

# List that contain objects

# students = [
#     {'first_name': 'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# print(students[1]['last_name']) # Prints Rosales

# import random
# print(random.random())
# print(random.random()*100)
# print(random.random()*30+20)

# import random
# print(random.random()*30+20)
# def randInt(min=0, max=100):
#     num = random.random() * (max - min) + min
#     return num
# print(randInt())
# print(randInt(max=50))
# print(randInt(min=50))
# print(randInt(min=50, max=500))

# import random
# print(random.random()*30+20)
# def randInt(min=0, max=100):
#     num = random.random() * (max - min) + min
#     return round (num)
# print(randInt())
# print(randInt(max=50))
# print(randInt(min=50))
# print(randInt(min=50, max=500))

# import random
# var takes in guess of heads or tails
# guess=""
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails')
#     guess = input()
# toss = random.randint(0,1) #0 is tails, 1 is heads
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again')
#     guess = input()
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')

