STR_MIN_VAL = 2
TOKEN_LIFETIME = 3600
PASSWORD_LEN = 8
NOTE_TITLE_LEN = 50
SPELLER_URL = 'https://speller.yandex.net/services/spellservice.json/checkText'
SPELLER_SETTINGS = {
    'lang': 'ru,en',
    'options': 6,
}
SPELLER_TEXT_LIM = 1000
NOTE_MAX_LEN = SPELLER_TEXT_LIM
LOGGING_FILE = 'app.log'
LOGGING_FILE_MODE = 'a'
LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'