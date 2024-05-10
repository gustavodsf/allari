from dataclasses import dataclass
from typing import List, Dict
from .experience import Experience

@dataclass
class Phone:
  number: str
  type: str

  def __eq__(self, other): 
    if not isinstance(other, Phone):
        return False
    return self.number == other.number