"""Restaurant rating lister."""


# put your code here
import sys

score_file = open(sys.argv[1])

restaurant_ratings = {}

for line in score_file:
    line = line.rstrip()
    info = line.split(":")
    restaurant = info[0]
    rating = info[1]
    restaurant_ratings[restaurant] = rating


for restaurant, rating in sorted(restaurant_ratings.items()):
    print "{} is rated at {}.".format(restaurant, rating)