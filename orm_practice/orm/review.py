import uuid
from logger import logger


class Review:
    def __init__(self, header, text, mark, author, status='Moderation'):
        self._id = uuid.uuid4()
        self._header = header
        self._text = text
        self._mark = mark
        self._author = author
        self._status = status

    def __str__(self):
        return f"{self._header} ( {self._mark} ) - {self._status}"

    def __repr__(self):
        return f"{self._id} : {self._header} ( {self._mark} ) - {self._status}"

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        if value > 5:
            self._mark = 5
        elif value < 1:
            self._mark = 1
        else:
            self._mark = value

    @property
    def author(self):
        return self._author

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
