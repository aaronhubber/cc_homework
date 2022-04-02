# WRITE YOUR FUNCTIONS HERE
#to get the name of the petshop, return the name
#1
from os import remove
from time import perf_counter


def get_pet_shop_name (shop):
    return shop["name"]

#2 get total cash in shop
def get_total_cash(amount):
    return amount ["admin"]["total_cash"]

#3 add 10 to the total in shop cash
def add_or_remove_cash (shop_total, cash):
    shop_total["admin"]["total_cash"] += cash 
    return shop_total

#4 same as above as using cash variable from testshop file

#5 find total number of pets sold
def get_pets_sold (number_of_pets):
    return number_of_pets ["admin"]["pets_sold"]

#6 increase the number of pets sold by 2
def increase_pets_sold (total_pets, sold):
    total_pets["admin"]["pets_sold"] += sold
    return total_pets

#7 count number of pets as stock
def get_stock_count(pets):
    return len(pets["pets"])

#8 find the number of britih shorthairs
def get_pets_by_breed (pet_shop, breed):
    num_breed = []
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["breed"] == breed:
            num_breed.append(pet)
    return (num_breed)

#9 same as number 8

#10 same as above but looking for name rather than breed

def find_pet_by_name(pet_shop, pet_name):
    for pets_select in pet_shop["pets"]:
        if pet_name == pets_select["name"]:
            return pets_select

# def find_pet_by_name (pet_shop, name):
#     pets = pet_shop["pets"]
#     for pet in pets:
#         if pet["name"] == name:
#             return pet["name"]


# def find_pet_by_name (pet_shop, names):
#     pet_names = pet_shop["pets"]
#     for banana in pet_shop:
#         if banana["name"] == names:
#             return (pet_names)

    # pet = []
    # names = pet_shop["name"]
    # for petz in names:
    #     if petz["pet"]["name"] == [p_names]:
    #         pet.append(p_names)
    # return pet

# def find_pet_by_name (pet_shop, pet_names):
#     pet_names = []
#     for names in pet_names:
#         for name in names ["pets"]["names"]:
#             pet_names.append(name)
#     return pet_names

#q11 same as 10

# q12 remove arthur from list

def remove_pet_by_name (pet_shop, pet_name):
    for pets_select in pet_shop["pets"]:
        if pet_name == pets_select["name"]:
            return pet_name

#q13 

def remove_pet_by_name(pet_shop, pet_name):
    #pets = pet_shop["pets"]

    for pet in pet_shop["pets"] :
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

#q14 get total number of pets after adding a pet
def add_pet_to_stock (pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    return len(pet_shop["pets"])

#q15

def get_customer_cash (total):
    return total["cash"]

#q16

def remove_customer_cash (customer, cash):
    customer["cash"] -= cash

#q17

def get_customer_pet_count (total):
    return len(total["pets"])

#q18
def add_pet_to_customer (customer, new_pet):
    customer["pets"].append(new_pet)
    return len(customer["pets"])





#q19
# def customer_can_afford_pet (customer, new_pet);






