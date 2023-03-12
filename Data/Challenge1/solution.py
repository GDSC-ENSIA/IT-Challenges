'''
A store owner wants to analyze the data of the cookies she sells.
The data can be found in start.py file.

1. In order to allow the owner to check the store's stock, write a function that returns a boolean value indicating if a certain brand exist.

2. The store wants now to calculate the area of the cookie of each brand. To do so, follow those steps:
    2.1. Write a function to calculate the area of a circle for a given radius (Do NOT take pi=3.14!).
    2.2. Write a function that converts float values into integer approximation.
    2.3. Using the previous functions, add an attribute to each dictionary in the data list indicating the cookie's surface area of each brand.

3. Print cookies with area between 1000mm² and 2000mm², inclusive.
'''

# Dataset
key_brand = 'Brand'
key_radius = 'Radius'
cookies = [
    {key_brand: 'Makla', key_radius: 23},
    {key_brand: 'Mibo', key_radius: 17},
    {key_brand: 'Cookio', key_radius: 19},
    {key_brand: 'Ji3ane', key_radius: 25},
    {key_brand: 'GDSCookies', key_radius: 27}
]

# Q1
def does_exist(brand):
    for cookie in cookies:
        if(cookie[key_brand] == brand):
            return True
    return False

# Q2.1
def calc_area(radius):
    from math import pi
    return pi * (radius ** 2)

# Q2.2
def to_int(x):
    return round(x)

# Q2.3
key_surface = 'Surface'
for cookie in cookies:
    cookie[key_surface] = to_int(calc_area(cookie[key_radius]))

# Q3
print([cookie[key_brand] for cookie in cookies if (cookie[key_surface] in range(1000, 2000))])
