# (c) Tony Yan 2017

# Declearing some global lists and dictionaries to store stuff.
# dictionary for number and a litst of its factors
dic_num_factor = {}
# dictionary  for number and the sum of its factors
dic_num_sum = {}
# list of all the friendly numbers found
list_friendly = []
# filtered repeated friendly numbers, friendly numbers can't be itself
dic_friendly_not_self = {}
# list of  dictionary keys for dic_friendly_not_self
dic_friendly_not_self_keys = []
dic_friendly_no_repeat = {}


# Find all the factors of a number, and find the sum, then put in a dictionary
def find_sum(num):
    list_factors_of_num = []  # temporary list
    if num in dic_num_sum:      # if alread calcuated
        return dic_num_sum[num]  # just return the previous result
    for i in range(1, num):    # if not, find all its factors
        if num % i == 0:        # is the number dividable by i
            if i in dic_num_factor:
                print(i)
                list_factors_of_num += dic_num_factor[i]
            else:
                list_factors_of_num.append(i)  # put the factors found in the list
    # put the list of factors in the global dictionary, for re-using the result
    print(list_factors_of_num)
    dic_num_factor[num] = list_factors_of_num
    # put the sum of factors in the global dictionary, for re-using the result
    dic_num_sum[num] = sum(list_factors_of_num)
    return dic_num_sum[num]


# test if the number has a friend
def search(num):
    if find_sum(find_sum(num)) == num:  # logic - if has any firend.
        # put the number that has a friend to the list.
        list_friendly.append(num)
        return True
    else:   # no friend
        return False


# scan and test the numbers
def find(num):
    # run though all the numbers
    print('                             ,press Ctrl C to intrrupt.', end="\r")
    for i in range(1, num + 1):
        print('Calculating:', i, end="\r")
        search(i)
    # clean up the double up friends, as they are paired.
def cleanup():
    for i in list_friendly:
        print('Cleaning Up cache      ', end="\r")
        if i != dic_num_sum[i]:
            dic_friendly_not_self[i] = dic_num_sum[i]
            dic_friendly_not_self_keys.append(i)
    list_mentioned = []  # a list to keep a record, so
    for i in dic_friendly_not_self_keys:  # using the list of friends
        # set up the variables for the two numbers
        i1 = dic_friendly_not_self[i]
        i2 = dic_friendly_not_self[i1]
        # a new pair, then print
        if i1 not in list_mentioned and i2 not in list_mentioned:
            list_mentioned.append(i2)
            list_mentioned.append(i1)
            dic_friendly_no_repeat[i1] = i2


# print out the results
def print_results(max_num=0):
    print('Results:                                                                                   ')
    if len(dic_friendly_not_self_keys) == 0:  # If there's no friends, then...
        print('None')
    else:  # there's some friends
        for i1 in dic_friendly_no_repeat:
            i2 = dic_friendly_no_repeat[i1]
            print(i1, ',', i2, 'are pairs')
            print('    Number =', i1, 'Factors:',
                  dic_num_factor[i1], 'Sum =', dic_num_sum[i1])
            print('    Number =', i2, 'Factors:',
                  dic_num_factor[i2], 'Sum =', dic_num_sum[i2])
            print('    Number =', i1, 'Sum =', dic_num_sum[i1])
            print('    Number =', i2, 'Sum =', dic_num_sum[i2])

def control():  # control centre...
    last_max = 0  # just to keep a record, so things don't get messy
    while True:
        try:
            i = int(input('\nmax limit: '))
            if i <= last_max:  # if a max limit larger has been used before
                print('calculated before')
            else:
                last_max = i
                try:
                    find(i)
                except:
                    pass
                cleanup()
                print_results()
        except:
            # if something went wrong...
            print('invalid input')
            break


control()
