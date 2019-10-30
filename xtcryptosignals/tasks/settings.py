__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from environs import Env


env = Env()
env.read_env(env('SETTINGS_APP'), recurse=False)

MONGODB_NAME = env.str('MONGODB_NAME')
MONGODB_HOST = env.str('MONGODB_HOST')
MONGODB_PORT = env.int('MONGODB_PORT')

TIMEOUT_PER_SYMBOL_REQUEST = 2.0  # in seconds
TIMEOUT_PER_SYMBOLS_REQUEST = 5.0  # in seconds
SYMBOL_FLOAT_PRECISION = 8
PRICES_CHANGE_CHART_SIZE = 6

from xtcryptosignals.settings import *  # noqa
from xtcryptosignals.tasks.settings_local import *  # noqa