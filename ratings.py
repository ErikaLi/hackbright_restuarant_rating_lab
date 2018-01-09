"""Restaurant rating lister."""


# put your code here
import sys


# file closes automatically
with open(sys.argv[1]) as score_file:

    restaurant_ratings = {}

    for line in score_file:
        line = line.rstrip()
        restaurant_rating = line.split(":")
        restaurant = restaurant_rating[0]
        rating = restaurant_rating[1]
        restaurant_ratings[restaurant] = rating
        

user_restaurant = raw_input("What is the restaurant name? ")
user_rating = int(raw_input("Please rate this restaurant (1 - 5) "))
restaurant_ratings[user_restaurant] = user_rating

for restaurant, rating in sorted(restaurant_ratings.items()):
    print "{} is rated at {}.".format(restaurant, rating)
