"""
Description:

Task:

This kata requires you to write an object that receives a file path and does operations on it. NOTE FOR PYTHON USERS: You cannot use modules os.path, glob, and re
The purpose of this kata is to use string parsing, so you're not supposed to import external libraries. I could only enforce this in python.

Testing:

Python:

>>> master = FileMaster('/Users/person1/Pictures/house.png')
>>> master.extension()
'png'
>>> master.filename()
'house'
>>> master.dirpath()
'/Users/person1/Pictures/'
"""


class FileMaster():
    def __init__(self, filepath):
        filepath = filepath.split('.')
        self._extension = filepath.pop()
        filepath = filepath[0].split('/')
        self._filename = filepath.pop()
        self._dirpath = '/'.join(filepath) + '/'

    def extension(self):
        return self._extension
    def filename(self):
        return self._filename
    def dirpath(self):
        return self._dirpath
