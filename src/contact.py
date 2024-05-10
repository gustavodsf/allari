from dataclasses import dataclass
from typing import List
from .phone import Phone

@dataclass
class Contact:
  id: int
  owner_id: int
  contact_nickname: str
  phone: List[Phone]
