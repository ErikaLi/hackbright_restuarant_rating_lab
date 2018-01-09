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


def is_continue():
    user_continue = raw_input("Do you want to continue to add another rating? (Y/N) ")
    if user_continue.lower() == "n":
        return True
    elif user_continue.lower() != "y":
        print "Please enter either Y or N."
        is_continue()


def valid_rating():
    try:
        rating = int(raw_input("Please rate this restaurant (1 - 5) "))
        return rating
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        return valid_rating()


while True:
    user_restaurant = raw_input("What is the restaurant name? ")
    user_rating = valid_rating()
    #print user_rating
    if user_rating not in range(1, 6):
        print "This is not a valid number. Please enter a number between 1 and 5. "
        valid_rating()
    restaurant_ratings[user_restaurant] = user_rating
    if is_continue():
        break


for restaurant, rating in sorted(restaurant_ratings.items()):
    print "{} is rated at {}.".format(restaurant, rating)
