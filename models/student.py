from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    home_address = Column(String)
    group_id = Column(Integer, ForeignKey("groups.id"))

    def __init__(self, name: str, surname: str, age: int,home_address: int ):
        self.name = name
        self.surname = surname
        self.age = age
        self.home_address = home_address


# id | name | surname | home_address | group_id |
# 1 | fff | fgfg | 15 | jh | 1 |


#groups
# id | name_of_group |