from read_data import read_data


def find_all_users_name(data: dict) -> list:
    """
    This function will find all the users in the json file and return the list of users name.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    users_name = []
    for n in range(len(data['messages'])):
        if 'actor' in data['messages'][n]:
            users_name.append(data['messages'][n]['actor'])
        elif 'from' in data['messages'][n]:
            users_name.append(data['messages'][n]['from'])
    return users_name


data = read_data('data/result.json')
print(find_all_users_name(data))
