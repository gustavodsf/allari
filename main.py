from typing import Tuple, List
from src.person import Person
from src.contact import Contact
from src.input_file import InputFile
from src.relationship import Relationship
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--person', help='=used inform the person id')

def get_input_files() -> Tuple[List[Person], List[Contact]]:
  input_file = InputFile();
  people = input_file.get_people()
  contacts = input_file.get_contacts()
  return (people, contacts)


def get_people_relation(personId: int) -> List[Person]:
  (people, contacts) =  get_input_files()
  relationship = Relationship();
  return relationship.get_colleges(2, people, contacts)

def print_people(people: List[Person]) -> None:
  for person in people:
    print(f"{person.id}: {person.first} {person.last}")

def print_connected_people(personId: int) -> None:
  connected = get_people_relation(personId)
  print_people(connected)

if __name__ == '__main__':
    args = parser.parse_args()
    if args.person:
      personId = args.person
      print(f"find the colleges of the person with id {personId}")
      print_connected_people(personId)
    else:
      print(f"we need that you inform the perso id thought the parameter --person")
