from datetime import datetime
import os
import sys


class Person():
    def __init__(self, id, name, email):
        self.id = id
        self.name=name
        self.email=email

class Freelancer(Person):
    def __init__(self,id,name,email):
        super().__init__(id,name,email)
        self.email=email