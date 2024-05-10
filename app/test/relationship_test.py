import unittest
from app.src.relationship import Relationship 
from app.src.person import Person 
from app.src.experience import Experience 
from app.src.contact import Contact 
from app.src.phone import Phone 

class TestRelationship(unittest.TestCase):

  def test_relationship_person_contact_empty_array(self):
    relationship = Relationship()
    result = relationship.get_colleges(1, [], [])
    self.assertEqual(len(result), 0)

  def test_relationship_person_array_full_of_data(self):
    relationship = Relationship()
    result = relationship.get_colleges(1,[
      Person(0, "Gustavo", 'Daniel', "+5521964925227", [Experience('Allari', 'dev', '2021-01-01', None)] ),
      Person(1, "Doe", 'Daniel', "+552196492537", [Experience('Allari', 'dev', '2022-01-01', '2023-01-01')] ),
      Person(2, "Victor", 'Daniel', "+5521964925237", [Experience('Ole', 'dev', '2022-01-01', None)] ),
    ], [])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0].first,'Gustavo')

  def test_relationship_person_array_full_of_data(self):
    relationship = Relationship()
    result = relationship.get_colleges(1,[
      Person(0, "Gustavo", 'Daniel', "+5521964925227", [Experience('Allari', 'dev', '2021-01-01', None)] ),
      Person(1, "Doe", 'Daniel', "+552196492537", [Experience('Allari', 'dev', '2022-01-01', '2023-01-01')] ),
      Person(2, "Victor", 'Daniel', "+5521964925237", [Experience('Allari', 'dev', '2022-01-01', None)] ),
    ], [])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0].first,'Gustavo')
    self.assertEqual(result[1].first,'Victor')


  def test_relationship_person_contact_full_of_data_but_seach_user_without_connection(self):
    relationship = Relationship()
    result = relationship.get_colleges(1,[
      Person(0, "Gustavo", 'Daniel', "+5521964925227", [Experience('Allari', 'dev', '2021-01-01', None)] ),
      Person(1, "Doe", 'Daniel', "+552196492537", [Experience('Ambush', 'dev', '2022-01-01', '2023-01-01')] ),
      Person(2, "Victor", 'Daniel', "+5521964925237", [Experience('Navalia', 'dev', '2022-01-01', None)] ),
    ], [
      Contact(1,0,'dad',[Phone("+5521964925237", 'cell')]),
      Contact(2,0,'mom',[Phone("+5521964925238", 'cell')]),
      Contact(2,1,'test',[Phone("+552196492599", 'cell')]),
      Contact(2,2,'friend',[Phone("+5521964925227", 'cell')])
    ])
    self.assertEqual(len(result), 0)

  def test_relationship_person_contact_full_of_data_but_seach_user_with_phone_connection(self):
    relationship = Relationship()
    result = relationship.get_colleges(0,[
      Person(0, "Gustavo", 'Daniel', "+5521964925227", [Experience('Allari', 'dev', '2021-01-01', None)] ),
      Person(1, "Doe", 'Daniel', "+552196492537", [Experience('Ambush', 'dev', '2022-01-01', '2023-01-01')] ),
      Person(2, "Victor", 'Daniel', "+5521964925237", [Experience('Navalia', 'dev', '2022-01-01', None)] ),
    ], [
      Contact(1,0,'dad',[Phone("+5521964925237", 'cell')]),
      Contact(2,0,'mom',[Phone("+5521964925238", 'cell')]),
      Contact(2,1,'test',[Phone("+552196492599", 'cell')]),
      Contact(2,2,'friend',[Phone("+5521964925227", 'cell')])
    ])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0].first, "Victor")

  def test_relationship_person_contact_full_of_data_but_seach_user_with_phone_and_work_connection(self):
    relationship = Relationship()
    result = relationship.get_colleges(0,[
      Person(0, "Gustavo", 'Daniel', "+5521964925227", [Experience('Allari', 'dev', '2021-01-01', None)] ),
      Person(1, "Doe", 'Daniel', "+552196492537", [Experience('Allari', 'dev', '2022-01-01', '2023-01-01')] ),
      Person(2, "Victor", 'Daniel', "+5521964925237", [Experience('Navalia', 'dev', '2022-01-01', None)] ),
    ], [
      Contact(1,0,'dad',[Phone("+5521964925237", 'cell')]),
      Contact(2,0,'mom',[Phone("+5521964925238", 'cell')]),
      Contact(2,1,'test',[Phone("+552196492599", 'cell')]),
      Contact(2,2,'friend',[Phone("+5521964925227", 'cell')])
    ])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0].first, "Doe")
    self.assertEqual(result[1].first, "Victor")