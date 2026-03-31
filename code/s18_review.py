
# words = 'the cat sat on the mat'.split()
# print(len(words))
# print(len(set(words)))

# def mystery(s):
#     return len(set(s)) == len(s)

# print(mystery('hello'))
# print(mystery('world'))


# freq = {'a': 3, 'b': 1, 'c': 2}
# result = sorted(freq.items(), key=lambda x: x[1])
# print(result)


# num = 100
# try:
#     a = float(input('Enter a number to divide by: '))
#     print(num / a)
# except ZeroDivisionError:
#     print('Error: Division by zero is not allowed.')
# except ValueError:
#     print('Error:Please enter a valid number.')
# finally:
#     print("We still want to print this")

# print('Lets move on to the next part of the code...')


# import requests

# # response = requests.get('https://oim.108122.xyz/words/random')
# # print(response.json())   # a random word!


# response = requests.get('https://oim.108122.xyz/mass')
# data = response.json()

# # print(data['name'])       # 'Massachusetts'
# # print(data['governor'])   # 'Maura Healey'

# # for town in data['data'][:5]:
# #     print(f"{town['name']}: pop {town['population']:,}")

# print (len(data))
# print(data.keys())
# print(type(data['data']))

# towns = data['data']
# print(type(towns))

import requests

response = requests.get(
    'https://oim.108122.xyz/words/random',
    headers={'X-Token': 'ricric'},  # your first name x2
)
print(response.json())