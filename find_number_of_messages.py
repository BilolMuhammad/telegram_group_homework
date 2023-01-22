from read_data import read_data


def find_number_of_messages(data: dict) -> int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.

    """
    sum_messages = 0
    messages = data['messages']
    for n in range(len(messages)):
        if messages[n]['type'] == 'message':
            sum_messages += 1

    return sum_messages


data = read_data('data/result.json')
print(find_number_of_messages(data))
