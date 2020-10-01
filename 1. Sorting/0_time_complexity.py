from binary_search_tree import BSTNode
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


# Linear time
def print_animals(animal_list): # O(n)
    for i in range(len(animal_list)): # O(n)
        print(animal_list[i]) # O(1) + O(k) where k is the len of the string for our purposes we are ignoring k


"""
Getting the time complexity of an iterative solution
1. Compute the Big-O for each line in isolation.
2. If something is in a loop, multiply it's Big-O by the loop for the total.
3. If two things happen sequentially, add the Big-Os.
4. Drop leading multiplicative constants from each Big-O.
5. From all the Big-Os that are added, drop all but the biggest, dominating one.
"""

# lets figure out the time complexity of this code
def print_animals_a(animal_list): # O(n) Linear
    for i in range(len(animals)): # O(n)
        print(animal_list[i]) # O(1) * n (1 * n)
        my_number = 0  # O(1) (1 * n)
        # O(2 * n)
        for _ in range(100000): # O(100000) (100000 * n)
            my_number += 1  # O(1) (1 * 100000) O(100000)

    # O(100003 * n) => O(n)
    # O(100000 * 1) => O(1)

    # O(n)

# Polynomial Time
"""
Key Points
- This gets bad quickly, but a computer can normally handle an n of a few hundred
- It's easy to confuse this with exponential time. The difference is that here, the number grows, but the exponent stays the same. It's opposite for exponential, where the number stays the same, but the exponent grows.
- The keywords for polynomial are pairs, triplets, etc. Sometimes you have to think to get this - finding a match on two names of lists is a pair
- One point of algorithms and data structures is to improve solutions that have this runtime or worse
"""

# Print a list of all possible animal pairs
def print_animal_pairs(): # O(n ^ 2)
    for animal_1 in animals: # O(n)
        for animal_2 in animals: # O(n)
            print(f"{animal_1} - {animal_2}") # O(1)

# Print a list of all possible animal triples
def print_animal_triples(): # O(n^3)
    for animal_1 in animals: # O(n)
        for animal_2 in animals: # O(n)
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")


# Print a list of all possible animal triples
def print_animal_triples_a():
        # O(n)
        for animal in animals:
            print(animal)
        # O(n^3)
        for animal_1 in animals:
            for animal_2 in animals:
                for animal_3 in animals:
                    print(f"{animal_1} - {animal_2} - {animal_3}")

def insert_array(n): # O(n^2) -> O(n * n)
    arr = []
    for i in range(n): # O(n) beacuse of loop
        arr.insert(0, i) # linear operation because you are inserting at the front
        # arr.append(0, i) # if we were adding to the end this will be constant, then the function would be linear

def time_insert():
    for in in [10, 100, 1000, 10000]:
        start = time.time()
        insert_array(n)
        end = time.time()
        print(f"{n}: \t {end-start}")

time_insert()
# when tested the increase in time was multiplied so not linear but quadratic
# 10 -> ~ 000005960464475390625
# 100 -> ~ 000030040748966706875
# 1000 -> ~ 0.000408495330810547
# 10000 -> ~ 0.05913805961608887
# 100000 -> ~ 0.472319641111328125
# 1000000 -> ~ 4.838762998580933
# runtimes are not increasing by a factor of 10, then it would be linear


# Exponential Time
"""
Key Points
- This gets bad extremely quickly. Between 30 and 40, even simple processes break down
- It's easy to confuse this with exponential time. The difference is that here, the exponent grows, but the number stays the same. It's opposite for polynomial, where the exponent stays the same, but the base number grows.
- The keywords for exponential are 'all', 'combinations', 'groups', etc.
- Combination locks have a bad name - they're really permutation locks!
"""

# Given a list,
# Return a list of all possible combination of animals
def get_animal_combos(l):
    list_length = len(l)
    if list_length == 0:
        return [[]]
    else:
        animal_combos = []
        previous_combos = get_animal_combos(l[1:])
        for combo in previous_combos:
            animal_combos.append(combo)
            animal_combos.append(combo + [l[0]])
        return animal_combos

counter = 0
def get_animal_combos(l):
    global counter
    list_length = len(l)
    if list_length == 0:
        return [ [] ]
    else:
        animal_combos = []
        previous_combos = get_animal_combos( l[1:] )

        for combo in previous_combos:
            animal_combos.append( combo )
            animal_combos.append( combo + [l[0]] )
            counter += 1
        return animal_combos


get_animal_combos(animals)
print(counter)


# Factorial Time

"""
Key Points
- Factorial time is the worse time complexity that we have deal with on a normal basis
- The keywords for exponential are 'all', 'permutations', 'orders', 'arrangements', etc.
- Combination locks have a bad name - they're really permutation locks!
"""

# Given a list,
# Return a list of all possible arrangements of list items
def get_all_arrangements(l):
    list_length = len(l)
    if list_length <= 1:
        return [l]
    else:
        arrangements = []
        previous_arrangements = get_all_arrangements( l[1:] )
        for previous_arrangement in previous_arrangements:
            for i in range(len(previous_arrangement) + 1):
                arrangements.append( previous_arrangement[i:] + [l[0]] + previous_arrangement[:i] )
        return arrangements


# Logarithmic Time

"""
Key Points
- Look for division that dramatically reduces the remaining data for hints that this might be logn
- Often, this means dividing the data in each step
- Key words are 'sorted list', 'binary', 'tree'
"""

# free all the animals, half at a time
# (remove them from the array)
def free_animals(animals):
    while len(animals) > 0:
        animals = animals[0:len(animals) // 2]


def bst_random(random_nums, target):
    bst = BSTNode(random_nums[0]) # O(1)
    # overall: n log n
    for num in random_nums[1:]: # iteration ->O(n)
        bst.insert(num) # insert is O(log n)

    bst.contains(target) # O(log n) -> with each iteration you can throw out each item you are looking at
    # in whole: n log n + log n --> n log n  --> Linearithmic time

bst_random([8, 4, 16, 1, 3, 12, 6, 5, 7, 2, 15, 13, 14, 10, 9, 11], 13)