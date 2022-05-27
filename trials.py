"""Python functions for JavaScript Trials 1."""

 
def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    evenNums = []

    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)
    return evenNums

def get_odd_indices(items):
    results = []
    results = items[::2]
    print(results)


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f'{i}. {item}')
        i += 1


def get_range(start, stop):
    nums = []
    i = start - 1
    while i < stop - 1:
        i += 1
        nums.append(i)
    return nums

def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)
    return chars


def snake_to_camel(string):
    camel_case = []
    words = string.split('_')
    for word in words:
        new_word = word[0].upper() + word[1:]
        camel_case.append(new_word)


    print(''.join(camel_case))


def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if longest < len(word):
            longest = len(word)
    return longest


def truncate(string):
    result = []
    for letter in string:
        if len(result) == 0 or letter != result[len(result) - 1]:
            result.append(letter)

    print(''.join(result))


def has_balanced_parens(string):
    parens = 0
    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

        if parens < 0:
            return False
    return parens == 0


def compress(string):
    compressed = []
    curr_char = ''
    count = 0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            if count > 1:
                compressed.append(str(count))

            curr_char = char
            count = 0
        count += 1
    compressed.append(curr_char)
    if count > 1:
        compressed.append(str(count))
    
    print(''.join(compressed))
