from tkinter import *
class Tasks:
  description = ""
  startTime = None
  endTime = None
  sent_late = False
  sent_start = False
  completed = BooleanVar()
  sent_check = False
  def __init__(self, d, s, e):
    self.description = d
    self.startTime = s
    self.endTime = e
    self.sent_start = False
    self.sent_late = False
    self.sent_check = False
    
    self.completed = BooleanVar(value = False)

def start_time_sort(all_tasks):
  #get the starting time hour and minute
  newest_task = all_tasks[len(all_tasks)-1]
  new_task_start = newest_task.startTime
  #get the starting hour and make sure the first digit is not 0
  new_task_hour = new_task_start.split(":")[0]
  if new_task_hour[0] == "0":
    new_task_hour == new_task_hour[1]
  new_task_hour = int(new_task_hour)
  #get the starting minute and make sure the first digit is not 0
  new_task_min = new_task_start.split(":")[1]
  if new_task_min[0] == "0":
    new_task_min == new_task_min[1]
  new_task_min = int(new_task_min)
  for i in range(len(all_tasks)-1):
    #get the starting hour and minute of a task to compare it to
    task_start = all_tasks[i].startTime
    task_hour_min = task_start.split(":")
    hour = task_hour_min[0]
    if hour[0] == "0":
      hour = hour[1]
    hour = int(hour)
    min = task_hour_min[1]
    if min[0] == "0":
      min = min[1]
    min = int(min)
      
    if new_task_hour < hour:
      all_tasks.insert(i, newest_task)
      all_tasks.pop(len(all_tasks)-1)
      return all_tasks
    elif new_task_hour == hour:
      if new_task_min < min:
        all_tasks.insert(i, newest_task)
        all_tasks.pop(len(all_tasks)-1)
        return all_tasks
  return all_tasks




def validate_min(m):
  if(len(m)==2):
    if(m[0]==0):
      try:
        int(m[1])
      except:
        return False
      else:
        if(0<=int(m[1])<60):
          return True
        else:
          return False
    else:
      try:
        int(m)
      except:
        return False
      else:
        if(0<=int(m)<60):
          return True
        else:
          return False
  else:
    return False


def validate_time(time):
  hour_min = time.split(":")
  if(len(hour_min)!=2):
    return False
  hour = hour_min[0]
  min = hour_min[1]
  if(len(hour)==1):
    try:
      int(hour)
    except:
      return False
    else:
        if(0<=int(hour)<=24):
            return validate_min(min)
        else:
            return False
  elif(len(hour)==2):
    if(hour[0]==0):
      try:
        int(hour[1])
      except:
        return False
      else:
        if(0<=int(hour[1])<24):
            return validate_min(min)
        else:
            return False
    else:
        try:
            int(hour)
        except:
            return False
        else:
            if(0<=int(hour)<24):
                return validate_min(min)
            else:
                return False
  else:
      return False
        
def validate_start_end(start, end):
  start_hour_min = start.split(":")
  end_hour_min = end.split(":")
  startH = start_hour_min[0]
  if len(startH) == 2 and startH[0] == "0":
    startH = startH[1]
  startM = start_hour_min[1]
  if startM[0] == "0":
    startM = startM[1]
  startH = int(startH)
  startM = int(startM)
  
  endH = end_hour_min[0]
  if len(endH) == 2 and endH[0] == "0":
    endH = endH[1]
  endM = end_hour_min[1]
  if endM[0] == "0":
    endM = endM[1]
  endH = int(endH)
  endM = int(endM)
  if endH < startH:
    return False
  elif endH == startH:
    if endM < startM:
      return False
    else:
      return True
  else:
    return True