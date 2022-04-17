from tkinter import *
import random
import os
import threading
import active
base_window = Tk()
import tasks
import windows
dir = os.getcwd()
#bgimg = Canvas(base_window, width = 400, height = 400)
#bgimg.grid(fill = "both", expand = True)
icon = PhotoImage(file = dir + "/Images/RealIcon.png")
base_window.iconphoto(False, icon)
base_window.title("Distraction Destroyer - The App you always wanted")
base_window['background'] = "#ffffff"

welcome_widget_frame = Frame(base_window)
welcome_widget_frame['background'] = '#ffffff'
current_frame = welcome_widget_frame
title = Label(welcome_widget_frame, text = "Distraction Destroyer", height = 2, fg="Red")
title.config(font=("TimesNewRoman", 20))
title['background'] = '#ffffff'
windows.startUpPopWindow()
#Images (made using Picsart)
lab = Label(welcome_widget_frame, borderwidth=0, highlightthickness=0)
img = PhotoImage(file = dir +"/Images/Study.png", width=150, height=150)
lab['image'] = img
lab.grid(row=6, column=0)

def loadMainMenu():
  #For the back button
  welcome_widget_frame.grid(row=0, column=0)
  title.grid(row = 0, column = 0, sticky="N")
  aboutButton.grid(row=4, column=0)
  scheduleButton.grid(row=2, column=0)
  creditsButton.grid(row=5, column=0)
  motivationButton.grid(row=3, column=0)
  tasksButton.grid(row=1, column=0)
  lab.grid(row=6, column=0)
  

#functions for buttons
def back():
  
  global current_frame
  current_frame.destroy()
  loadMainMenu()
  
def aboutPressed():
  global current_frame
  global img2
  about_frame = Frame(base_window)
  current_frame = about_frame
  for item in welcome_widget_frame.winfo_children():
    item.grid_forget()
  
  about = Label(about_frame, text = "About the program", font = "TimesNewRoman")
  info = Label(about_frame, text = "This program is an aggressive reminder program designed to keep you on track\n so that you can actually get all of your work done.\n You can schedule tasks using the schedule button and it will send you reminders to get your work done.\n If it senses you playing a game like Minecraft during your work, it will give you a warning to stop\n and if you don't stop within 5 minutes, \n it shuts down your game. \n It can also send nice motivational messages too\n\n")
  customer_reviews = Label(about_frame, text = "Customer Reviews\nThis app is so great, I will buy it for my company - Jeff Pezos\n Definitely 5 out of 5 stars, greatest app of all time - Bob McBob\n These are all totally real reviews - Guy who never lies\n Can't wait to use it on my siblings to 'help them study better' - Very Nice Guy")
  lab2 = Label(about_frame, borderwidth=0, highlightthickness=0)
  img2 = PhotoImage(file = dir + "/Images/discord.png",  width=150, height=150)
  lab2['image'] = img2
  lab2.grid(row=13, column=5)

  about.grid(row=5, column=5)
  info.grid(row=8, column=5)
  customer_reviews.grid(row = 9, column = 5)
  
  back_button = Button(about_frame, text = "Back", command = back)
  back_button.grid(row = 12, column = 5)
  about_frame.grid(row =0, column = 0)
  


new_task = None
task_time = None
task_end_time = None
task_list = []

enforcer_of_rules = threading.Thread(target = active.active_check_loop, args=(task_list,))
enforcer_of_rules.start()
def retrieveInfo():
  global task_list
  global current_frame
  for i in current_frame.winfo_children():
    if(i['fg']=='red' or i['fg'] == 'green'):
      i.destroy()
  
  data_name = new_task.get()
  data_start = task_time.get().strip()
  data_end = task_end_time.get().strip()
  success = False
  if(tasks.validate_time(data_start) and tasks.validate_time(data_end)):
    the_task = tasks.Tasks(data_name, data_start, data_end)
    task_list.append(the_task)
    task_list = tasks.start_time_sort(task_list)
    success = True  
  
  new_task.delete(0, 'end')
  task_time.delete(0, 'end')
  task_end_time.delete(0, 'end')
  if(success):
    for i in range(len(task_list)):
      print(task_list[i].description)
      print(task_list[i].startTime)
      print(task_list[i].endTime)
    print(" ")
    success_lab = Label(current_frame, text = "Success", fg = "green")
    success_lab.grid(row = 3, column = 1)
    success_lab.after(3000, lambda: success_lab.grid_forget())
    
    
    
  else:
    error_lab = Label(current_frame, text = "Data Format Error", fg = "red")
    error_lab.grid(row = 3, column = 1)
    error_lab.after(3000, lambda: error_lab.grid_forget())
    
    
  
def schedulePressed():
  global current_frame
  global new_task
  global task_end_time
  global task_time
  global dir
  global img3
  schedule_frame = Frame(base_window)
  current_frame = schedule_frame
  for item in welcome_widget_frame.winfo_children():
    item.grid_forget()

  note = Label(schedule_frame, text = "Enter your time using 24hr time", font = 'TimesNewRoman')
  note.grid(row=5, column = 1)
  question = Label(schedule_frame, text = "Enter the task ", font = "TimesNewRoman")
  question.grid(row=0, column=0)
  txt_box = Entry(schedule_frame, width = 30)
  time_start_prompt = Label(schedule_frame, text = "Start Time", font = 'TimesNewRoman')
  time_start = Entry(schedule_frame, width = 30)
  time_end_prompt = Label(schedule_frame, text = "End Time", font = 'TimesNewRoman')
  time_end = Entry(schedule_frame, width = 30)
  schedule_frame.grid(row=0, column=0)
  txt_box.grid(row=1, column=0)
  time_start_prompt.grid(row = 0, column = 1)
  time_end_prompt.grid(row = 0, column = 2)
  time_start.grid(row = 1, column = 1)
  time_end.grid(row = 1, column = 2)
  
  new_task = txt_box
  task_time = time_start
  task_end_time = time_end
  submit_task_button = Button(schedule_frame, text = "Submit", command = retrieveInfo)
  submit_task_button.grid(row = 2 , column = 1)
  
  back_button = Button(current_frame, text = "Back", command = back)
  back_button.grid(row = 4, column = 1)
  
  lab3 = Label(current_frame, borderwidth=0, highlightthickness=0)
  img3 = PhotoImage(file = dir + "/Images/LOL.png", width=150, height=150)
  lab3['image'] = img3
  lab3.grid(row=8, column=1)  
  
def creditsPressed():
  credit_frame = Frame(base_window)
  global current_frame
  global img2
  global dir
  current_frame = credit_frame

  for item in welcome_widget_frame.winfo_children():
    item.grid_forget()
  
  credits = Label(credit_frame, text = "This application was created by Jason W, Nathan H, and Kelvin F ", font = "TimesNewRoman")
  credits.grid(row=5, column=5)
  credit_frame.grid(row =0, column = 0)

  lab4 = Label(current_frame, borderwidth=0, highlightthickness=0)
  img4 = PhotoImage(file = dir + "/Images/Steam.png", width=150, height=150)
  lab4['image'] = img2
  lab4.grid(row=9, column=5) 
  
  back_button = Button(credit_frame, text = "Back", command = back)
  back_button.grid(row = 8, column = 5)


def motivationPressed():
  global current_frame
  global img3
  global dir
  motivation_frame = Frame(base_window)
  current_frame = motivation_frame
  
  for item in welcome_widget_frame.winfo_children():
    item.grid_forget()

  #Quotes from https://meratas.com/blog/quotes-for-college-students/ written by Anna Klawitter
  quotes = ['“A little progress each day adds up to big results.” – Satya Nani', '“It’s not about having time. It’s about making time.” – unknown', '“Losers quit when they’re tired. Winners quit when they’ve won.”', '“Skill is only developed by hours and hours of work.” – Usain Bolt', '“Wake up with determination. Go to bed with satisfaction.” – unknown', '“You will never always be motivated. You have to learn to be disciplined.” – unknown', '“Self-discipline is the magic power that makes you virtually unstoppable.” – Dan Kennedy', '“The way to get started is to quit talking and begin doing.” – Walt Disney', '“Focus on doing the right things instead of a bunch of things.” – Mike Krieger', '“The successful warrior is the average man, with laser-like focus.” – Bruce Lee', '“Discipline is just choosing between what you want now and what you want most.” – Abraham Lincoln', '“It’s not about perfect. It’s about effort.” – Jillian Michaels', '“Excellence is not a skill. It is an attitude.”– Ralph Marston', '“Focus on your goal. Don’t look in any direction but ahead.” -unknown', '“You don’t get what you wish for. You get what you work for.” – Daniel Milstein', '“Do something now; your future self will thank you for later.” – unknown', '“Don’t try to be perfect. Just try to be better than you were yesterday.” – unknown', '“Keep going. Everything you need will come to you at the perfect time.” – unknown', '“Even the greatest were beginners. Don’t be afraid to take that first step.” – unknown', '“Everything you’ve ever wanted is on the other side of fear.” – George Addair', '“Your time is limited, so don’t waste it living someone else’s life.”– Steve Jobs', '“You can’t use up creativity. The more you use, the more you have.”– Maya Angelou', '"The best way to gain self-confidence is to do what you are afraid to do.” – Swati Sharma', '“If you hear a voice within you say ‘you cannot paint,’ then by all means paint, and that voice will be silenced.” – Vincent Van Gogh', '“Courage doesn’t always roar. Sometimes courage is the quiet voice at the end of the day saying ‘I will try again tomorrow’.”– Mary Anne Radmacher', '“Wake up with determination. Go to bed with satisfaction.” – unknown', '“It never gets easier. You just get better.” – Jordan Hoechlin', '“Fall seven times, stand up eight.” – Japanese Proverb', '“The pain you feel today will be the strength you feel tomorrow.” – Nicole', '“You don’t want to look back and know you could have done better.” – unknown', '“Successful people are not gifted; they just work hard, then succeed on purpose.” – G.K. Nielson', '“Determination is doing what needs to be done even when you don’t feel like doing it.” –  unknown', '“If you are not willing to risk the usual, you will have to settle for the ordinary.” – Jim Rohn', '“Perseverance is the hard work you do after you get tired of doing the hard work you already did.” – Newt Gingrich']
  '''
  num = random.randint(0, len(quotes)-1)
  while num == last_num:
    num = random.randint(0, len(quotes)-1)
  last_num = num'''
  motivation = Label(current_frame, text = quotes[random.randint(0, len(quotes)-1)], font = "TimesNewRoman")
  motivation.grid(row=5, column=5)
  motivation_frame.grid(row=0, column=0)

  lab3 = Label(current_frame, borderwidth=0, highlightthickness=0)
  img3 = PhotoImage(file = dir + "/Images/Minecraft.png", width=150, height=150)
  lab3['image'] = img3
  lab3.grid(row=9, column=5)
  
  back_button = Button(motivation_frame, text = "Back", command = back)
  back_button.grid(row = 8, column = 5)

def remove_tasks():
  for i in range(len(task_list)-1, -1, -1):
    if task_list[i].completed.get() == True:
      task_list.pop(i)
  back()
  viewPressed()

def viewToSchedule():
  back()
  schedulePressed()
    
def viewPressed():
  global current_frame
  global task_list
  #global check_button_list
  #check_button_list = []
  view_frame = Frame(base_window)
  current_frame = view_frame
  view_frame.grid(row=0, column=0)

  for item in welcome_widget_frame.winfo_children():
    item.grid_forget()

  if len(task_list) == 0:
    no_tasks = Label(view_frame, text="There are no scheduled tasks.")
    no_tasks.grid(row = 8, column = 1)
    schedule_button = Button(view_frame, text="Schedule new tasks", command=viewToSchedule)
    schedule_button.grid(row = 9, column = 1)
  else:
  #Adapted from Geeks for geeks https://www.geeksforgeeks.org/create-table-using-tkinter/
    task_name = Entry(view_frame, width = 20, font = "TimesNewRoman")
    task_name.grid(row = 0, column = 0)
    task_name.insert('end', "Task Name")
    task_name.config(state = 'readonly')
    task_start = Entry(view_frame, width = 20, font = "TimesNewRoman")
    task_start.grid(row = 0, column = 1)
    task_start.insert('end', "Task Start")
    task_start.config(state = 'readonly')
    task_end = Entry(view_frame, width = 20, font = "TimesNewRoman")
    task_end.grid(row = 0, column = 2)
    task_end.insert('end', "Task End")
    task_end.config(state = 'readonly')
    for task in range(len(task_list)):
      for property in range(3):
        cell = Entry(view_frame, width = 20, font = "TimesNewRoman")
        cell.grid(row = task+1, column = property)
        if(property == 0):
          cell.insert('end', task_list[task].description)
          cell.config(state = 'readonly')
        elif(property == 1):
          cell.insert('end', task_list[task].startTime)
          cell.config(state = 'readonly')
        else:
          cell.insert('end', task_list[task].endTime)
          cell.config(state = 'readonly')
      
      check = Checkbutton(view_frame, text="Completed?", onvalue = True, offvalue = False, variable=task_list[task].completed)
      check.grid(row = task+1, column = 4)
    
    remove_tasks_button = Button(view_frame, text="Remove completed tasks", command=remove_tasks)
    remove_tasks_button.grid(row = 8, column = 1)
  
  back_button = Button(view_frame, text = "Back", command = back)
  back_button.grid(row = 10, column = 1)


#Buttons
aboutButton = Button(welcome_widget_frame, text = "About", bg="Yellow", activebackground = "#f7dd14", command=aboutPressed)

scheduleButton = Button(welcome_widget_frame, text = "Schedule New Tasks", bg="lightGreen", activebackground = "#2bf070", command=schedulePressed)

tasksButton = Button(welcome_widget_frame, text = "View Tasks", bg = "lightBlue", activebackground = "skyBlue", height = 2, command=viewPressed)

creditsButton = Button(welcome_widget_frame, text = "Credits", bg = "#ffbe63", activebackground = "orange", command=creditsPressed)

motivationButton = Button(welcome_widget_frame, text = "Motivational Quote", bg = "#ff6666", activebackground = "#f54040", command=motivationPressed)

loadMainMenu()
welcome_widget_frame.grid_rowconfigure(0, weight = 1)
welcome_widget_frame.grid_columnconfigure(0, weight = 1)
base_window.grid_rowconfigure(0, weight = 1)
base_window.grid_columnconfigure(0, weight = 1)

base_window.mainloop()