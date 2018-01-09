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

def get_rating():
    rating = raw_input("Please rate this restaurant (1 - 5) ")
    while not is_valid(rating):
        print "This is not a valid number. Please enter a number between 1 and 5. " 
        rating = raw_input("Please rate this restaurant (1 - 5) ")
    return int(rating)
    

def is_valid(score):
    try:
        score = int(score)
        return score in range(1, 6)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        return False


while True:
    user_restaurant = raw_input("What is the restaurant name? ")
    user_rating = get_rating()
    restaurant_ratings[user_restaurant] = user_rating
    if is_continue():
        break


for restaurant, rating in sorted(restaurant_ratings.items()):
    print "{} is rated at {}.".format(restaurant, rating)
