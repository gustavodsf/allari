from dataclasses import dataclass
from typing import List
from .experience import Experience

@dataclass
class Person:
  """Class to store a person metadata and create a link with the experiences"""
  id: int
  first: str
  last: str
  phone: str
  experience: List[Experience]
