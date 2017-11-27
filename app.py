# Standard Library
import csv
import os
import random


# 3rd Party Modules
import simplejson as json

# Config
DATA_FILE = 'data.csv'
JSON_FILE = 'data.json'

MAX_RETRIES = 200


# Functions
def store_problem_data(data):
    """Store problem data out to file

    :param data: problems dataset dictionary
    :type data: dict
    """
    with open(JSON_FILE, 'w') as jfile:
        jfile.write(json.dumps(data))


def retrieve_problem_data():
    """Retrieve problem data from file
    """
    if not os.path.exists(JSON_FILE):
        prob_dict = gen_dict_from_csv()
        store_problem_data(prob_dict)
    else:
        prob_dict = load_json_data()
    return prob_dict


def gen_dict_from_csv():
    """Creates usable dict from data file
    """
    res = {}
    with open(DATA_FILE, 'r') as dfile:
        reader = csv.DictReader(dfile)
        for row in reader:
            chap = row['Chapter']
            prob_num = row['Problem']
            default_dict = {
                'Topic': row['Topic'],
                'Problems': {},
                'Size': 0,
                'Attempts': 0,
                'Completed': 0,
                }
            res.setdefault(chap, default_dict)
            res[chap]['Size'] += 1
            problem = {
                'Page': row['Page'],
                'Status': None,
                }
            res[chap]['Problems'][prob_num] = problem
    return res


def load_json_data():
    """Loads data from JSON_FILE
    """
    with open(JSON_FILE, 'r') as jfile:
        return json.loads(jfile.read())


def get_problem(data, chaps=[], status=[None]):
    """Returns problem to try
    
    Based on the parameters provided, a random problem from Cracking the Coding
    Interview 6th edition is selected and returned.

    :param data: problems dataset dictionary
    :param chaps: chapters to use ex. [2, 5, 11]
    ;param status: problem status' allowed
    :type data: dict
    :type chaps: list
    :type status: list
    :return: problem and page number
    :rtype: dict
    """
    def pick_chap():
        """Selects random chapter
        """
        if len(chaps) > 0:
            chap = str(random.choice(chaps))
        else:
            chap = random.choice(data.keys())
        return chap
    for attempt in range(MAX_RETRIES):
        chap = pick_chap()
        prob = random.choice(list(data[chap]['Problems'].keys()))
        choice = data[chap]['Problems'][prob]
        if choice['Status'] in status:
            results = {
                'Problem': '{}.{}'.format(chap, prob),
                'Page': choice['Page'],
                }
            return results
    return None


def update_problem_status(data, prob, status):
    """Update status for problem

    :param data: problems dataset dictionary
    :param prob: problem number in format [chapter].[number] ex. 7.11
    :param status: status of problem of [None, 'pass', 'fail']
    :type data: dict
    :type prob: str
    :type status: str
    """
    chap, prob_num = prob.split('.')
    data[chap]['Problems'][prob_num]['Status'] = status 
    store_problem_data(data)
    

if __name__ == '__main__':
    # Setup data dict
    prob_dict = retrieve_problem_data()

