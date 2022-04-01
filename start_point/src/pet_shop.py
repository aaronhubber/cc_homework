# WRITE YOUR FUNCTIONS HERE
#to get the name of the petshop, return the name
#1
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
def get_pets_by_breed (number_of_breed, breed):
    
    for breed in 






