from dataclasses import field
from functools import wraps
from http import HTTPStatus
import logging
from typing import Optional

import httpx
from pydantic.dataclasses import dataclass

from app.core.constants import SPELLER_SETTINGS, SPELLER_URL

logger = logging.getLogger(__name__)


@dataclass
class SpellerResult:
    code: Optional[int]
    pos: Optional[int]
    row: Optional[int]
    col: Optional[int]
    word: Optional[str]
    s: Optional[list[str]] = field(default_factory=lambda: [0])

    def __eq__(self, other: object) -> bool:
        '''
        SpellerResult instances are considered to be equal
        if their word fields are equal.

        '''
        if isinstance(other, SpellerResult):
            return self.word == other.word
        return False

    def __hash__(self):
        return hash(self.word)


class YandexSpellerAPI:
    """Base class for requests to YandexSpeller."""
    URL = SPELLER_URL
    SETTINGS = SPELLER_SETTINGS

    def __do_req(text: str, url: str = URL) -> list[SpellerResult]:
        """Base request method."""
        params = {'text': text}
        params.update(SPELLER_SETTINGS)
        try:
            with httpx.Client() as client:
                response = client.post(url, data=params, timeout=5.0)
                response.encoding = 'utf-8'

                if response.status_code != HTTPStatus.OK:
                    raise Exception(
                        "Error during executing request. {}: {}".format(
                            response.status_code, response.reason_phrase
                        )
                    )
                json_data = response.json()

                result: list[SpellerResult] = [
                     SpellerResult(**obj) for obj in json_data
                ]
                logger.info(f'{result}')
            return result

        except Exception as err:
            logger.error(f'{type(err)}: {err}')

    @staticmethod
    def get_spell_check(text: str):
        ''''''
        return YandexSpellerAPI.__do_req(text=text)


def correct_typos(func):
    '''
    Decorator for finding and correcting typos
    with the help of Яндекс.Спеллер service.

    Time Complexity: O(m*n)
    Space Complexity: O(m*n)

    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        text_to_correct: str = func(*args, **kwargs)

        speller_results: list[SpellerResult] = YandexSpellerAPI.get_spell_check(
            text=text_to_correct
        )

        if speller_results is not None:
            for result in set(speller_results):
                misspelled_word = result.word
                # get the first suggested option as it's the closest
                suggested_correction = result.s[0]
                text_to_correct = text_to_correct.replace(
                    misspelled_word, suggested_correction
                )
        return text_to_correct
    return wrapper
