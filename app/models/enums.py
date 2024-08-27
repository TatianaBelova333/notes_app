from enum import Enum


class PriorityEnum(str, Enum):
    '''Enum class for the priority levels of notes.'''
    HIGH = 'Важное'
    MEDIUM = 'Среднее'
    LOW = 'Неважное'


class TagEnum(str, Enum):
    '''Enum Class for note tags.'''
    WORK = 'Работа'
    SPORT = 'Спорт'
    STUDY = 'Учеба'
    SHOPPING = 'Покупки'
    PLEASURE = 'Развлечение'
    MISCELLANEOUS = 'Разное'
