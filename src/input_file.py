import json
from src.person import Person
from src.contact import Contact
from src.phone import Phone
from src.experience import Experience
from typing import List

class InputFile:

  def get_people(self, file_name="persons.json") -> List[Person]:
    newPeopleList = []
    people = self._read_json(file_name)
    for person in people:
      experience =  list(map(lambda e: Experience(**e), person.get('experience')))
      person['experience']= experience
      newPeopleList.append(Person(**person))
    return newPeopleList

  def get_contacts(self, file_name="contacts.json") -> List[Contact]:
    newContactList = []
    contacts = self._read_json(file_name)
    for contact  in contacts:
      phones = list(map(lambda c: Phone(**c), contact.get('phone')))
      contact['phone'] = phones
      newContactList.append(Contact(**contact))
    return newContactList

  def _read_json(self, file_name) -> List:
    with open("./data/{}".format(file_name)) as f:
      return json.load(f)
 