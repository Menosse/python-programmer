# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Wed Oct 16 15:33:03 2019

# @author: Fernando
# """

# # 1 Ask the user for the radius of a circle and then print the area
user_radius = int(input('Please type the radius of a circle\n >>> '))
pi = 3.14159265359
area = user_radius**2 * pi
print("The Circle area is %f",area)


# # 2 Convert fahrenheit to celsius (You will have to find the formula)
user_fah = int(input('Please type the Farenheit value\n >>> '))
celcius = (user_fah - 32) * 5/9

# print("The Celcius value is %f",celcius)

# # 3 Obtain the sum of two integers
user_int1 = int(input('Please type the Farenheit value\n >>> '))
user_int2 = int(input('Please type the Farenheit value\n >>> '))
print("The sum is",user_int1 + user_int2)

# # 4 Obtain the product of two integers
user_int1 = int(input('Please type the Farenheit value\n >>> '))
user_int2 = int(input('Please type the Farenheit value\n >>> '))
print("The product is",user_int1 * user_int2)

# # 5 Bob, Ann, Jane and Ashwin want to order pizza - they know they will each eat
# # 4 slices of pizza. The local pizza shop sells pizzas of only 6 slices
# # What is the minimum number of pizzas needed - Use floor division

ppl = 4
ppl_slices = 4
pizza_size = 6
total_slices = ppl * ppl_slices
min_pizza = total_slices // pizza_size + 1
print("Minimun number of pizzas is",min_pizza)


min_pizza_prof = (total_slices+5) // 6
slices_left = min_pizza_prof * 6 - total_slices
print("Minimun number of pizzas is",min_pizza_prof )
print("slices left",slices_left )