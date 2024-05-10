from dataclasses import dataclass
from datetime import datetime,timedelta
from typing import List

DAYS_WORKING_TOGETHER = 90

@dataclass
class Experience:
  """ Class that represents a expience that a person has """
  company: str
  title: str
  start: datetime
  end: datetime #should be null if is the current experience

  def worked_together(self, experiences: List = []) -> bool:
    now = datetime.now()
    if experiences is None:
      return False

    for experience in experiences:
      if experience.company == self.company:
        other_start = datetime.strptime(experience.start, '%Y-%m-%d')
        other_end = now if experience.end == None else datetime.strptime(experience.end, '%Y-%m-%d')
        my_start = datetime.strptime(self.start,  '%Y-%m-%d')
        my_end = now if self.end == None else datetime.strptime(self.end, '%Y-%m-%d')

        if(
          (other_start <= my_start and (other_end - my_start).days > DAYS_WORKING_TOGETHER) or
          (my_start <= other_start and (my_end - other_start).days > DAYS_WORKING_TOGETHER) 
        ):  
          return True
    return False

