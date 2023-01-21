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
    idx = []
    for n in range(len(data['messages'])):
        if 'actor_id' in data['messages'][n]:
            if not data['messages'][n]['actor_id'] in idx:
                if 'actor' in data['messages'][n]:
                    users_name.append(data['messages'][n]['actor'])
                    idx.append(data['messages'][n]['actor_id'])
        elif 'from_id' in data['messages'][n]:
            if not data['messages'][n]['from_id'] in idx:
                if 'from' in data['messages'][n]:
                    users_name.append(data['messages'][n]['from'])
                    idx.append(data['messages'][n]['from_id'])
    return users_name


data = read_data('data/result.json')
print(find_all_users_name(data))
