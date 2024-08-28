STR_MIN_VAL = 2
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

PASSWORD_LEN = 8
PASS_LEN_ERR_MSG = f'Password must be at least {PASSWORD_LEN} characters long.'
PASS_CONTAINS_EMAIL_ERR_MSG = 'Password must not contain {user_email}'
USER_SUCCESS_REG_MSG = 'User {user_email} has been successfully registered.'

TOKEN_URL = 'auth/jwt/login'
TOKEN_LIFETIME = 3600

NOTE_NOT_FOUND_ERR = 'The note has not been found.'
