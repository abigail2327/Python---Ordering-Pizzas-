import topping
import pizza0
#done by Mohamed Abdullah Najumudeen, Abigail Da Costa, Farheen Haniyah

cheeses = {'f': "fresh mozzarella (f)", 's': "Shredded cheese (s)", 'c': "cheddar (c)"}
meats = {'p': 'pepperoni (p)', 's': 'sausage (s)', 'b': 'bacon (b)', 'm': 'meatball (m)','n': 'none(n)'}
veggies = {'m': 'mushrooms (m)', 'b': 'bell peppers (b)', 'n': 'none (n)', 'p': 'pineapple (p)', 'j': 'jalapenos peppers (j)',}

def create_cheeses():
    cheeses = []
    cheeses.append(topping.Topping("fresh mozzarella", "f", "cheese", 1.00))
    cheeses.append(topping.Topping("cheddar", "c", "cheese", 0.50))
    cheeses.append(topping.Topping("Shredded cheese", "s", "cheese", 0.00))
    
    
    cheeses_dict = {}
    for i in range(len(cheeses)):
        cheeses_dict[cheeses[i].code] = cheeses[i]
    return cheeses_dict
    

def create_meats():
    meats = []
    meats.append(topping.Topping("pepperoni", "p", "meat", 1.5))
    meats.append(topping.Topping("sausage", "s", "meat", 1.50))
    meats.append(topping.Topping("bacon", "b", "meat", 1.00))
    meats.append(topping.Topping("meatball", "m", "meat", 2.00))
    meats.append(topping.Topping("none", "n", "meat", 0.00))
    meats_dict = {}
    for i in range(len(meats)):
        meats_dict[meats[i].code] = meats[i]
    return meats_dict


def create_veggies():
    veggies = []
    veggies.append(topping.Topping("mushrooms", "m", "veggie", 1.00))
    veggies.append(topping.Topping("bell peppers", "b", "veggie", 1.00))
    veggies.append(topping.Topping("none", "n", "veggie", 0.00))
    veggies.append(topping.Topping("pineapple", "p", "veggie", 1.00))
    veggies.append(topping.Topping("jalapenos peppers", "j", "veggie", 1.00))
   
    veggies_dict = {}
    for i in range(len(veggies)):
        veggies_dict[veggies[i].code] = veggies[i]
    return veggies_dict


def cheese_options(cheeses):
    print("cheese options: ")
    for key in cheeses:
        print(cheeses[key])

def meat_options(meats):
    print("meat options: ")
    for key in meats:
        print(meats[key])

def veggies_options(veggies):
    print("veggie options: ")
    for key in veggies:
        print(veggies[key])
def cheese_prompt(cheeses):
    print("What cheese would you like on your pizza?")
    for key in cheeses:
        print(cheeses[key])

    cheese_list = []
    cheese_i = input("Enter the 1-letter codes for your choice (with spaces)): ")
    if cheese_i == "all":
        for key in cheeses:
            cheese_list.append(cheeses[key])
    else:
        split_cheese = cheese_i.split(' ')
        for i in range(len(split_cheese)):
            cheese_list.append(cheeses[split_cheese[i]])
    return cheese_list

def meat_prompt(meats):
    print("What meats would you like on your pizza?")
    for key in meats:
        print(meats[key])
    
    meat_i = input("Enter the 1-letter codes for your choice (with spaces)): ")
    if meat_i == "all":
        meat_list = []
        for key in meats:
            meat_list.append(meats[key])
    else:
        split_meat = meat_i.split(' ')

        meat_list = []
        for i in range(len(split_meat)):
            meat_list.append(meats[split_meat[i]])
    return meat_list

def veggie_prompt(veggies):
    print("What veggies would you like on your pizza?")
    for key in veggies:
        print(veggies[key])
    
    veggie_i = input("Enter the 1-letter codes for your choice (with spaces)): ")
    if veggie_i == "all":
        veggie_list = []
        for key in veggies:
            veggie_list.append(veggies[key])
    else:
        split_veggie = veggie_i.split(' ')

        veggie_list = []
        for i in range(len(split_veggie)):
            veggie_list.append(veggies[split_veggie[i]])
    return veggie_list

def manual():
    print("press 'all' to add all toppings of that type")
    print("press 1 to see cheese options")
    print("press 2 to see meat options")
    print("press 3 to see veggie options")
    print("press 4 to choose your cheese")
    print("press 5 to choose your meats")
    print("press 6 to choose your veggies") 
    print("press 7 to see your pizza")
    print("press 8 to create your pizza")
    print("press 9 to quit")

def print_pizza(cheeses, meats, veggies):
    print("Your pizza has: ")
    for i in range(len(cheeses)):
        print(cheeses[i])
    for i in range(len(meats)):
        print(meats[i])
    for i in range(len(veggies)):
        print(veggies[i])

def main():
    cheeses = create_cheeses()
    meats = create_meats()
    veggies = create_veggies()
    pizzas = []
    
    input("Welcome to the pizza factory,where all orders include two pizzas. \n Press enter to continue.")
    while len(pizzas) < 2:
        inp = int(input("input 0 to open manual.."))
        if inp == 0:
            manual()
        if inp == 1:
            cheese_options(cheeses)
        if inp == 2:
            meat_options(meats)
        if inp == 3:
            veggies_options(veggies)
        if inp == 4:
            cheeses_chosen = cheese_prompt(cheeses)
        if inp == 5:
            meats_chosen = meat_prompt(meats)
        if inp == 6:
            veggies_chosen = veggie_prompt(veggies)
        if inp == 7:
            print_pizza(cheeses_chosen, meats_chosen, veggies_chosen)
        if inp == 8:
            pizza_1 = pizza0.Pizza(cheeses_chosen, meats_chosen, veggies_chosen, 5.00)
            print(pizza_1)
            pizzas.append(pizza_1)

            cheeses_chosen = []
            meats_chosen = []
            veggies_chosen = []

        if inp == 9:
            break
    
    print("Your 2 pizzas are: ")
    for i in range(len(pizzas)):
        print(pizzas[i])
        
    print("Your total is: ")
    total = 0
    for i in range(len(pizzas)):
        total += pizzas[i].get_price()
    print(total)
main()