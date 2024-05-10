import unittest
from app.src.experience import Experience

class TestExperience(unittest.TestCase):
  
  def test_worked_together_empty_input_array(self):
    experience = Experience('allari', 'developer', '2020-10-11', None)
    result = experience.worked_together([])
    self.assertFalse(result)

  def test_worked_together_none_as_input(self):
    experience = Experience('allari', 'developer', '2020-10-11', None)
    result = experience.worked_together(None)
    self.assertFalse(result)

  def test_worked_together_intersection_period_diferent_company(self):
    experience = Experience('allari', 'developer', '2020-10-11', None)
    result = experience.worked_together([
      Experience('ambush', 'developer', '2021-10-11', None)
    ])
    self.assertFalse(result)
  
  def test_worked_together_intersection_period_same_company(self):
    experience = Experience('allari', 'developer', '2020-10-11', None)
    result = experience.worked_together([
      Experience('allari', 'developer', '2021-10-11', None)
    ])
    self.assertTrue(result)

  def test_worked_together_same_company_no_intersection(self):
    experience = Experience('allari', 'developer', '2020-01-11', '2020-10-11')
    result = experience.worked_together([
      Experience('allari', 'developer', '2021-10-11', None)
    ])
    self.assertFalse(result)

  def test_worked_together_same_company_no_intersection_less_than_90_days(self):
    experience = Experience('allari', 'developer', '2020-01-11', '2020-10-11')
    result = experience.worked_together([
      Experience('allari', 'developer', '2020-09-11', '2020-10-11')
    ])
    self.assertFalse(result)

  def test_worked_together_same_company_no_intersection_less_than_1_days(self):
    experience = Experience('Allari', 'dev', '2022-01-01', '2023-01-01')
    result = experience.worked_together([
      Experience('Allari', 'dev', '2021-01-01', None),
    ])
    self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()