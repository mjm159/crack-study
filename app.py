# Standard Library
import csv

# 3rd Party Modules
import simplejson as json

# Files
DATA_FILE = 'data.csv'
JSON_FILE = 'data.json'


# Functions
def gen_dict_from_csv():
    """Creates usable dict from data file
    """
    res = {}
    with open(DATA_FILE, 'r') as dfile:
        reader = csv.DictReader(dfile)
        for row in reader:
            chap = row['Chapter']
            res.setdefault(
                chap,
                {'Topic': row['Topic'], 'Problems': []},
                )
            problem = {
                'Number': row['Problem'], 
                'Page': row['Page'],
                'Status': None,
                }
            res[chap]['Problems'].append(problem)
    return res


def load_history():
    """
    """
    pass


if __name__ == '__main__':
    prob_dict = gen_dict()

