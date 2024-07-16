# Review 1

def add_to_list(value, my_list=None):

    '''
    problem:
    If add_to_list is called multiple times without providing the my_list argument, 
    the same list will be used each time, which is likely not the intended behavior.
    solution:
    Create a new list when my_list is None 
    instead of using a default mutable argument.
    '''

    if my_list is None:

        my_list = []

    my_list.append(value)

    return my_list



# Review 2

def format_greeting(name, age):

    '''
    problem:
    The function returns a greeting message with the name and age parameters
    but the string is not formatted correctly.
    solution:
    use f-string or format function to format the string
    '''

    return f"Hello, my name is {name} and I am {age} years old."
    # return "Hello, my name is {} and I am {} years old.".format(name, age)



# Review 3

class Counter:

    count = 0

    '''
    problem:
    The  __init__ method increases the count attribute of the instance, not 
    the class.Therefore, the class variable count remains unchanged.
    solution:
    Use type(self).count to access the class variable count.
    '''


    def __init__(self):

        type(self).count += 1



    def get_count(self):

        return self.count



# Review 4

import threading

'''
problem:
1.The increment method in the SafeCounter class is not thread-safe, 
meaning multiple threads might concurrently modify the count attribute,
leading to race conditions.
solution:
Use a threading lock to ensure that only one thread can increment 
the counter at a time.
'''

class SafeCounter:

    def __init__(self):

        self.count = 0
        self.lock = threading.Lock()



    def increment(self):

        with self.lock: 
            self.count += 1



def worker(counter):

    for _ in range(1000):

        counter.increment()



counter = SafeCounter()

threads = []

for _ in range(10):

    t = threading.Thread(target=worker, args=(counter,))

    t.start()

    threads.append(t)



for t in threads:

    t.join()



# Review 5
'''
problem:
1.The =+ operator is interpreted as an assignment (=) followed by a unary plus (+), 
which may get unexpect count result.
2.if item in counts: if item is a dictionary, it will raise an error.
soulution:
1. Use += operator to increment the value of the count.
2. Use json.dumps to convert the item to a string if item is a dictionary before 
checking if it is in the dictionary.
'''
def count_occurrences(lst):
    import json
    counts = {}

    for item in lst:

        if isinstance(item,dict):
            item = json.dumps(item)

        if item in counts:

            counts[item] += 1

        else:

            counts[item] = 1

    return counts