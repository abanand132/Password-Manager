import json

def advanced_search_func(website_data):
    # website_data = keyword we enter in website input box
    with open("data_files.json", 'r') as data_file:
        data = json.load(data_file)

    x = 0
    key_name = []
    key_matched_number = []
    index_list = []
    result_list = []
    """
    Logic : First calculate how many characters of website data matched with passwords keys. Then according to that
    , we saved that no. of characters matched in a list. Then we check for a maximum value present in the list.
    After getting the maximum value, we are checking that count of that number. If that number is present once it
    means there is only one key that is matched most nearly with the website data. But if the max number count is
    more than 1 then it means there are more than one key in password database that is matched with website data.
    In this case, we need to return a list of these keys that will be displayed in separate window.
    """
    for key in data.keys():
        for i in range(len(website_data)):
            if website_data[i] == key[i]:
                x += 1
            else:
                key_name.append(key)
                key_matched_number.append(x)
                x = 0
                break

        if len(website_data) == x and x != 0:
            key_name.append(key)
            key_matched_number.append(x)
            x = 0

    maximum_number = max(key_matched_number)  # it tells that it is the length of nearly matched string
    max_number_count = key_matched_number.count(maximum_number)  # checking how many times it is present

    if maximum_number == 0:
        return None

    elif max_number_count == 1:
        nearly_matched_String = key_name[key_matched_number.index(maximum_number)]
        return nearly_matched_String

    else:
        for i in range(len(key_matched_number)):
            if key_matched_number[i] == maximum_number:
                index_list.append(i)

        for i in index_list:
            result_list.append(key_name[i])

        return result_list
