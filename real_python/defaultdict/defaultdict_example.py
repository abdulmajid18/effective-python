import collections

my_dict = {"fruits": ["apple", "banana"]}
# my_dict["vegetables"].append("carrot") # KeyError
if "vegetables" not in my_dict:
    my_dict["vegetables"] = []
my_dict["vegetables"].append("carrot")

new_dict = collections.defaultdict(list, fruits=["apple", "banana"])

new_dict["vegetables"].append("carrot")
print(new_dict["vegetables"])

my_dict = {"fruits": ["apple", "banana"]}
my_dict.setdefault("vegetables", []).append("carrot")
print(my_dict["vegetables"])

#  more intuitive
