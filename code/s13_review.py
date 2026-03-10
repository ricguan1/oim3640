# stocks = 'AAPL, MSFT, GOOG, AMZN'

# print  = stocks[0]
# print  = stocks[-1]


def count_vowels(s):
    count = 0
    for c in s:
        if c in 'aeiou':
            count += 1
            
    return count

print(count_vowels('apple'))
print(count_vowels('sky'))
print(count_vowels('aeiou'))
print(count_vowels('dragon'))

'apple'.count('a')
'apple'.count('e')

# stocks = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
# stocks = stocks[0:2]
# print(stocks)
# s = input("Enter a list of stocks: ")

stocks = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
stocks = s.split(',')