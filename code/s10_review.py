# for i in range "saad abdullah":
# print (letters) 


# count = 0
# for letter in 'mississippi':
#     if letter == 's':
#         count += 1
# print(count)

# ciynt = 0 
# for c in "babson college":
#     count += 1 
# print(count)

# print (len("babson college"))

# print(h(3))

# def k(x):
#     if x > 0:
#         print("Positive")
#         return x
#     print("Non-positive")

# print(k(5))

# def uses_any(word, letters):
#     for ch in word:
#         if ch in letters:
#             return True
#     return False

# print(uses_any("hello", "xyz"))
# print(uses_any("hello", "aeiou"))

# def test(word):
#     for ch in word:
#         if ch == "a":
#             print("Found")
#             return True
#     print("Done")
#     return False

# print(test("cat"))

# word = "Python"

# print(word[0])
# print(word[-1])
# print(word[1:4])

def has_double(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False

print(has_double("book"))
print(has_double("cat"))