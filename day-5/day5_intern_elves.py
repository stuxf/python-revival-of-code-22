with open ('input.txt') as f:
    data = f.read().splitlines()

def contains_three_distinct_vowels(word):
    vowels = set('aeiou')
    return sum(1 for c in word if c in vowels) >= 3

def contains_double_letter(word):
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            return True
    return False
    
def contains_bad_strings(word):
    return 'ab' in word or 'cd' in word or 'pq' in word or 'xy' in word

def is_nice(word):
    return contains_three_distinct_vowels(word) and contains_double_letter(word) and not contains_bad_strings(word)

def repeat_with_between(word):
    for i in range(len(word) - 2):
        if word[i] == word[i+2]:
            return True
    return False

def contains_pair(word):
    for i in range(len(word) - 1):
        if word.count(word[i:i+2]) >= 2:
            return True
    return False

def is_nice_2(word):
    return repeat_with_between(word) and contains_pair(word)

good_data = [word for word in data if is_nice(word)]
print(f"{len(good_data)} words are nice")

good_data_2 = [word for word in data if is_nice_2(word)]
print(f"{len(good_data_2)} words are nice 2")