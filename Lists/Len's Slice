"""
1.To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:

"pepperoni"
"pineapple"
"cheese"
"sausage"
"olives"
"anchovies"
"mushrooms"

2.To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:
2
6
1
3
2
7
2

3.
Your boss wants you to do some research on $2 slices.Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.

4.Find the length of the toppings list and store it in a variable called num_pizzas.

5.Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.

6.Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.Each sublist in pizza_and_prices should have one pizza topping and an associated price.

7. To show the pizzas are in the order of increasing price (ascending).Store the first element of pizza_and_prices in a variable called cheapest_pizza.

8. To get the most expensive pizzas and cheapst pizzas we used List methods.

Finally we got the most expensive pizza and cheapest pizza.
"""

toppings= ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
print(toppings)

prices =[2,6,1,3,2,7,2]

num_two_dollar_slices= prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print(num_pizzas)
print("\n")
print("We sell ", num_pizzas, " different kinds of pizza!")

pizza_and_prices =[[prices[0],toppings[0]],
[prices[1],toppings[1]],
[prices[2],toppings[2]],
[prices[3],toppings[3]],
[prices[4],toppings[4]],
[prices[5],toppings[5]],
[prices[6],toppings[6]]]


print (pizza_and_prices)

pizza_and_prices.sort()

cheapest_pizza =pizza_and_prices[0]
print(cheapest_pizza)
print("\n")
priciest_pizza =pizza_and_prices[6]
print(priciest_pizza)
print("\n")
pizza_and_prices.pop()
print(pizza_and_prices)
print("\n")
pizza_and_prices.insert(4,[2.5,"peppers"])
print(pizza_and_prices)

print("\n")
three_cheapest = pizza_and_prices[:4]
print(three_cheapest)