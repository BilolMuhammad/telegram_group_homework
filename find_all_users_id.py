from read_data import read_data


def find_all_users_id(data: dict) -> list:
    """ 
    This function will find all the users in the json file and return the list of users id

    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    users_id = []
    messages = data['messages']
    for n in range(len(messages)):
        if 'actor_id' in messages[n]:
            if messages[n]['actor_id'] not in users_id:
                users_id.append(messages[n]['actor_id'])
        elif 'from_id' in messages[n]:
            if messages[n]['from_id'] not in users_id:
                users_id.append(messages[n]['from_id'])
    return users_id


data = read_data('data/result.json')
print(find_all_users_id(data))
