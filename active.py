import video_game_terminator
import datetime
import time
import windows
def getTime(tim):
  hour = tim.split(":")[0]
  min = tim.split(":")[1]
  try:
    hour = int(hour)
  except:
    hour = int(hour[1])
  
  try:
    min = int(min)
  except:
    min = int(min[1])
  return (hour, min)

def is_active(tsk):
  start = getTime(tsk.startTime)
  sh = start[0]
  sm = start[1]
  end = getTime(tsk.endTime)
  eh = end[0]
  em = end[1]
  currh = datetime.datetime.now().hour
  currm = datetime.datetime.now().minute
  if(sh<=currh<=eh):
    if(sh== currh):
      if(sm<=currm):
        return True
      else:
        return False
        
    elif(eh ==currh):
      if(currm<em):
        return True
        
      
    else:
      return True
  else:
    return False
      
def nearingEnd(tsk):
  end = getTime(tsk.endTime)
  
  eh = end[0]
  em = end[1]
  currh = datetime.datetime.now().hour
  currm = datetime.datetime.now().minute
  if(eh==currh):
    
    if((em-currm)<=10):
      return True
    else:
      return False
  elif((eh-1)%24==currh):
    if((60-currm)+em<=10):
      return True
    else:
      return False
  else:
    return False

def taskLate(tsk):
  end = getTime(tsk.endTime)
  eh = end[0]
  em = end[1]
  currh = datetime.datetime.now().hour
  currm = datetime.datetime.now().minute
  if(eh<currh):
    
    return True
  elif(eh==currh):
    
    if(currm>em):
      return True
    else:
      return False
  else:
    
    return False

def isStarting(task):
  start = getTime(task.startTime)
  currh = datetime.datetime.now().hour
  currm = datetime.datetime.now().minute
  sh = start[0]
  sm = start[1]
  if(sh==currh):
    if(currm>=sm):
      return True
    else:
      return False
  else:
    return False
def active_check_loop(tasks):
  chr_warning_sent = False
  dis_warning_sent = False
  while True:
    
    at_least_one_active = False
    for i in range(len(tasks)):
      
      if nearingEnd(tasks[i]) and (tasks[i].sent_check == False):
        tasks[i].sent_check = True
        windows.timeEndWarning()
      if is_active(tasks[i]):
        at_least_one_active = True
      
      if(taskLate(tasks[i]) and tasks[i].sent_late==False):
        windows.youreLate(tasks[i].description)
        tasks[i].sent_late = True
      if(isStarting(tasks[i]) and tasks[i].sent_start == False):
        tasks[i].sent_start = True
        windows.getToWork(tasks[i].description)
      
    if(at_least_one_active):
      result = video_game_terminator.eliminate_all_games(chr_warning_sent, dis_warning_sent)
      chr_warning_sent = result[0]
      dis_warning_sent = result[1]
          
    time.sleep(5)