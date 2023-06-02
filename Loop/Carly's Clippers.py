"""
1.Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.

2.Loop through the prices list and add each price to the variable total_price.

3.To get the number of prices by using python function and print it.

4. Next, we find out the daily average revenue .

5.Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.
To do it we used list comprehension.

6.finally we find out the new list of prices by using list comprehension and print it.

"""
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]


total_price = 0

for x in prices:
  total_price += x 
  print(x)

average_price = total_price/len(prices)
print("average_price: ${}". format(average_price))

new_prices = [x-5 for x in prices]
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
 total_revenue += prices[i]* last_week[i]

print("total_revenue:${0}". format(total_revenue))

average_daily_revenue = total_revenue/7
print("average_daily_revenue:${0}".format(average_daily_revenue))


cuts_under_30 = [hairstyles [i]for i in range (len(hairstyles))if new_prices [i] < 30]
print(cuts_under_30)