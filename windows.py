from tkinter import *
import simpleaudio
import os

dir2 = os.getcwd()

def startUpPopWindow():
  start_up = Toplevel()
  start_up.title("Start")
  msg = Label(start_up, text = "In order for this app to actually work, it needs you to eliminate physical distractions.\n Put away your phone somewhere where you can't see it and won't be tempted to get it.\n Next, take any distracting things off your desk and put them away.\n Then, organize your desk so everything on it is nice and neat.\n Finally, collect all the things you need to work and start WORKING NOW.\n You can close this window. Remember, Big Brother could be watching you(jk).\n Also, you better not be in your pajamas! Dress up properly", font = "TimesNewRoman")
  msg.grid(row = 0, column = 0)
  start_up.attributes('-topmost', 1)

def video_game_terminated():
  win = Toplevel()
  win.title("Game ended successfully")
  msg = Label(win, text = "Terminator destroyed your game. Stop playing games, get back to work now.\n No work -> bad grades -> not first choice university -> very sad :(\n If you get this message three times please watch this video https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  msg.grid(row = 0, column = 0)
  win.attributes('-topmost', 1)
  
def chromeWarning():
  chr = Toplevel()
  msg = Label(chr, text= "I hope you are using google for work purposes and not anything else.\n If you use gmail or any chat application remember to be professional and speak politely.\n No swearing.\n Also absolutely NO WORDLE")
  msg.grid(row = 0, column = 0)
  chr.attributes('-topmost', 1)

def getToWork(task):
  work = Toplevel()
  msg = Label(work, text = "Time to start your task: " + task + ". All your games are not disabled until you complete your tasks. And don't even think about rushing :)")
  msg.grid(row=0, column=0)
  work.attributes('-topmost', 1)
  
def discordWarning():
  dis = Toplevel()
  dismsg = Label(dis, text = "I hope you are using discord for work purposes and not anything else. Don't lie to yourself")
  dismsg.grid(row=0, column=0)
  dis.attributes('-topmost', 1)

def youreLate(task):
  late = Toplevel()
  late.title("YOU'RE LATE")
  latemsg = Label(late, text = "You're LATE on completing this task: " +task+ ".\n Big Brother is not impressed... \nNo video games for you until you finish your work.\n Don't rush, you don't want to submit work that looks like garbage.")
  latemsg.grid(row=0, column=0)
  #https://realpython.com/lessons/simpleaudio/ - Credit
  music = simpleaudio.WaveObject.from_wave_file(dir2+"\Audio\Sad.wav")
  sing = music.play()
  sing.wait_done()
  late.attributes('-topmost', True)

def timeEndWarning():
  warn = Toplevel()
  warnmsg = Label(warn, text = "Time's running up. Make sure to double check your work")
  warnmsg.grid()
  warn.attributes('-topmost', 1)