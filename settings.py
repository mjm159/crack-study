# Standard Library
import os

# 3rd Party Modules
import simplejson as json

# Local Modules
import config


# Functions
def load_settings():
    """Load JSON data from settings file

    :return: dictionary with settings details
    :rtype: dict
    """
    if os.path.exists(config.SETTINGS_FILE):
        with open(config.SETTINGS_FILE, 'r') as sfile:
            settings = json.loads(sfile.read())
    else:
        settings = {
            'Chapters': [],
            'Status': [],
            }
    return settings


def store_settings(settings):
    """Store settings in settings.json

    :param settings: settings for app
    :type settings: dict
    """
    with open(config.SETTINGS_FILE, 'w') as sfile:
        sfile.write(json.dumps(settings))

