from datetime import datetime
import os
import sys


class Person():
    def __init__(self, id, name, email, adate):
        self.id = id
        self.name=name
        self.email=email
        self.adate=datetime.now()

class Freelancer(Person):
    def __init__(self,id,name,email,adate):
        super().__init__(id,name,email,adate)
        self.email=email