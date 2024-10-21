"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluates to the number of entries
print(len(ice_cream))  # print 3

# add key-value entry by directly assigning to a key
ice_cream["mint"] = 3

# access entries by their key
print(ice_cream["chocolate"])  # prints 12

# test if "pbj" is a key in ice_cream
has_pdj: bool = "pbj" in ice_cream

# remove items by key using pop method
ice_cream.pop("strawberry")

# loop through iten using for-in loops
total_orders: int = 0
# the variable (e.g. flavor) iterates over each key one-by-one in the dict
for flavor in ice_cream:
    print(f"{flavor}: {ice_cream[flavor]}")
    total_orders += ice_cream[flavor]

print(f"Total orders: {total_orders}")
