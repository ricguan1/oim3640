# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)
# print(a is b)

# a = [1, 2, 3]
# b = a[:]
# b.append(4)
# print(a)
# print(a is b)

# eng2esp = {"one": "uno", "two": "dos", "three": "tres"}
# print(eng2esp["one"])

# # Start empty, add entries
# prices = {}
# prices['AAPL'] = 178.50
# prices['GOOG'] = 141.80
# prices['MSFT'] = 415.20

# # Update an existing key
# prices['AAPL'] = 182.30

# # Delete a key
# del prices['GOOG']

# print(prices)   # {'AAPL': 182.30, 'MSFT': 415.20}

# prices = {'AAPL': 182.30, 'MSFT': 415.20, 'GOOG': 141.80}
# for key in prices:                # loop over keys
#     print(key, prices[key])

# for value in prices.values():     # loop over values
#     print(value)

# for key, value in prices.items(): # loop over both
#     print(f'{key}: ${value}')

def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d