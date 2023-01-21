from read_data import read_data


def find_number_of_messages(data: dict) -> int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.

    """
    num_messag = 0
    for n in range(len(data['messages'])):
        if 'text' in data['messages'][n]:
            num_messag += 1
    return num_messag


data = read_data('data/result.json')
print(find_number_of_messages(data))
