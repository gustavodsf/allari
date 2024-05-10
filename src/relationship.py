from typing import List
from src.person import Person
from src.experience import Experience
from src.contact import Contact

class Relationship:

  def get_colleges(self, personId: int, people: List[Person], contacts: List[Contact]) -> List[Person]:
    [personInterest] = list(filter(lambda p: p.id == personId, people))
    colleges = []
    for person in people:
      if person.id == personId :
        continue
      if(self.connected_by_work(personInterest, person) or self.connected_by_contact(personInterest, person, contacts)):
        colleges.append(person)
    return colleges

  def connected_by_work(self, person: Person, other: Person) -> bool:
      matched = list(filter(lambda e: e.worked_together(person.experience), other.experience))
      if(len(matched) >= 1):
        return True
      return False

  def connected_by_contact(self, person: Person, other: Person, contacts: List[Contact]) -> bool:
    interest_contacts = list(filter(lambda c: c.owner_id == person.id, contacts))
    other_contacts = list(filter(lambda c: c.owner_id == other.id, contacts))

    if(self._is_connect_by_phone(person, other_contacts) and self._is_connect_by_phone(other, interest_contacts)):
      return True
    return False
  
  def _is_connect_by_phone(self, person: Person, contacts: List[Contact]) -> bool:
    for contact in contacts:
      for phone in contact.phone:
        if phone.number == person.phone:
          return True
    return False

  def get_id_of_colleges(self, people: List[Person], personId: int) -> List[int]:
    matched = self.get_colleges(people, personId)
    return list(map(lambda m: m.id, matched))

