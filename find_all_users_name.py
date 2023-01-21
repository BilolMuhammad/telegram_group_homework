from read_data import read_data
from find_all_users_id import find_all_users_id


def find_all_users_name(data: dict) -> list:
    """
    This function will find all the users in the json file and return the list of users name.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    users_name = []
    messages = data['messages']
    for n in range(len(messages)):
        if 'actor' in messages[n]:
            if not messages[n]['actor'] in users_name:
                users_name.append(messages[n]['actor'])
        if 'from' in messages[n]:
            if not messages[n]['from'] in users_name:
                users_name.append(messages[n]['from'])
    return users_name


data = read_data('data/result.json')
print(find_all_users_name(data))
