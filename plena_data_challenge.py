# function to use as a key in sort method returning the second element of the parameter
def sort_list(elem):
    return elem[1]


def plena_data_challenge():
    string = input("Please enter a string: ").lower()
    string_list = []
    new_string = ""
    # for loop going over each element in the string and counting the number of occurrences in them and then appending
    # the letter and count as a tuple into the ordered list
    for i in string:
        letter_count = string.count(i)
        string_list.append((i, letter_count))
    # take the list of tuples and sort them using our function above (utilizes the second element, or the letter count)
    string_list.sort(key=sort_list)
    # loop over the newly sorted/organized list of tuples to concatenate each letter onto the new string
    for letter in string_list:
        new_string += letter[0]
    return new_string
