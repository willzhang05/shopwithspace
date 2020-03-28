import sys
import populartimes
from pprint import pprint


API_KEY = sys.argv[1]

data = populartimes.get_id(API_KEY, "ChIJSYuuSx9awokRyrrOFTGg0GY")
pprint(data)
data = populartimes.get(API_KEY, ["grocery_or_supermarket"], (48.132986, 11.566126), (48.142199, 11.580047))
pprint(data)
