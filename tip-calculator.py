#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Tip calculator")
bill = int(input("What is your bill?"))
tip = int(input("What percent of tip would you tip?"))
split = int(input("How many people split the bill?"))

tip_perc = (int(tip)/100) + 1
split_perc = bill/split
result = round(split_perc * tip_perc)
print(result)