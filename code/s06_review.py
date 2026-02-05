# for i in range(4):
#     print("Iteration:",i)
#     print("Square:", i*i)
#     print()


# a = 5
# b = a
# a = 10
# print(b), print (a)


# def double(x):
#     return x * 2

# print(double(5))
# print(double("Hi"))


# a = [1, 2, 3]   # square bracket becomes a list
# b = a
# a.append(4)     # they are pointint to the same list
# print(b)
# print(a)


# x = 10

# def f():
#     message = "hello"
#     x = 5
#     return x
# print(f())
# print(x)
# print(message)  # message does not exist on the exist frame because it is only local, once its done, it is gone


# def draw_square(size):
#     for i in range (size):
#         # print ("brick" * size)
#         for j in range(size)



# create a function to draw a triangle


# in row i, how many bricks are there? = i+1

# def draw_triangle(rows):
#     for i in range(rows):
#         print("@" * (i+1))

# draw_triangle(4)


# REVIEW THIS QUESTION
# Draw a triangle like this (size = 5)

#     @     4 spaces + 1 # = 5  5 - 0 -1 = 4
#    @@     3 spaces + 2 # = 5  5 - 1 -1 = 3
#   @@@
#  @@@@
# @@@@@

# for i in range (size):
#     in row i, how many spaces are in there? size - i = 1

def draw_triangle(size):
    for i in range(size):
        print(" " * (size - i - 1) + "#" * (i + 1))

draw_triangle(5)


# create a function to draw a pyramid

    #
   ###
  #####
 #######

def draw_pyramid(size):
    for i in range(size):
        print(" " * )
 