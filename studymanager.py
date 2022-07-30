from tkinter import *
import sys

sys.setrecursionlimit(10000)
to_do_list = []


def start_studying():
  global to_do_list
  to_do_list = [task1.get(), task2.get(), task3.get(), task4.get(), task5.get()]
  to_do_list = list(filter(None, to_do_list))
  
  if not to_do_list:
    emptylist = Label(window, text = "Error: Empty Task List", font = ('Times New Roman', 15), fg = 'black', bg = 'white')
    emptylist.pack(side = BOTTOM)
    window.after(4000, emptylist.pack_forget)
  else:
    for widget in window.winfo_children():
      widget.destroy()
    studying()


running = FALSE
seconds = 0
minutes = 0
hours = 0

def studying():
  stopwatch = Label(text = '00:00:00', font = ('Times New Roman', 55))
  stopwatch.pack()

  start_button = Button(text='start', font=('Times New Roman', 15), command= lambda: start(stopwatch))
  start_button.place(x = 235,y = 67)

  pause_button = Button(text='pause', font=('Times New Roman', 15), command= lambda: pause(stopwatch))
  pause_button.place(x=295, y=67)

  create_list()
                  
  
def start(stopwatch):
  global running
  if not running:
    running = TRUE
    update(stopwatch)


def pause(stopwatch):
  global running
  running = FALSE


def update(stopwatch):
  if running:
    global seconds, minutes, hours
    seconds += 1
    if seconds == 60:
          minutes += 1
          seconds = 0
    if minutes == 60:
          hours += 1
          minutes = 0
  
    string_seconds = str(seconds)
    string_minutes = str(minutes)
    string_hours = str(hours)
    
    if seconds < 10:
      string_seconds = '0' + str(seconds)
    if minutes < 10:
      string_minutes = '0' + str(minutes)
    if hours < 10:
      string_hours = '0' + str(hours)
    
   
    stopwatch.config(text = string_hours + ':' + string_minutes + ':' + string_seconds)  
  
    stopwatch.after(1000, lambda: update(stopwatch))

task_list = []
check_list = []


def create_list():
  size = len(to_do_list)
  if size == 0:
    finished()
    return
    
  taskY = 150
  checkY = 170

  x = IntVar()
  y = IntVar()
  z = IntVar()
  s = IntVar()
  l = IntVar()
  checked = [x, y, z, s, l]
    
  for pos in range(size):
    task = Label(window, text = "Task " + str(pos+1), font = ("Times New Roman", 10))
    task.place(x=40, y = taskY)
    task_list.append(task)

    check = Checkbutton(window, text = to_do_list[pos], variable = checked[pos], font = ('Times New Roman', 15), bg = 'white', fg = 'black',onvalue = 1, offvalue = 0, command = lambda: manage_list(checked), highlightthickness = 0, bd =0)
    check.place(x = 20, y = checkY)
    check_list.append(check)

    taskY += 60
    checkY += 60


def manage_list(checked):
  remove_pos = 0
  for check in checked:
    if check.get() == 1:
      break
    remove_pos += 1
  checked[remove_pos] = 0
  del to_do_list[remove_pos]
  destroy_list()
  create_list()
 

def destroy_list():
  for task in task_list:
    task.destroy()
  for check in check_list:
    check.destroy()


def finished():
  for widget in window.winfo_children():
    widget.destroy()

  finished_message = Label(window, text = "Congratulations on finishing your work!!!", font=('Times New Roman', 20), bg = 'white', fg = 'black')
  finished_message.pack(side = TOP, pady = 120)

  total_time = "You studied for " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds"
  timed_message = Label(window, text = total_time , font=('Times New Roman', 10), bg = 'white', fg = 'black')
  timed_message.pack(side = TOP)

  
  
window = Tk()
window.geometry("600x500")
window.title("Study Manager")
window.configure(background='white')

icon = PhotoImage(file='book.png')
window.iconphoto(True, icon)

instructions = Label(window, text = "Enter your tasks", font=('Times New Roman', 40))
instructions.pack()

label1 = Label(window, text = "Task 1", font = ("Times New Roman", 10))
label1.place(x=20, y = 70)
task1 = Entry(window, font = ("Times New Roman", 10), bg = 'white', fg = 'black', width = 39)
task1.place(x = 20, y = 90)

label2 = Label(window, text = "Task 2", font = ("Times New Roman", 10))
label2.place(x=20, y = 130)
task2 = Entry(window, font = ("Times New Roman", 10), bg = 'white', fg = 'black',width = 39)
task2.place(x = 20, y = 150)

label3 = Label(window, text = "Task 3", font = ("Times New Roman", 10))
label3.place(x=20, y = 190)
task3 = Entry(window, font = ("Times New Roman", 10), bg = 'white', fg = 'black',width = 39)
task3.place(x = 20, y = 210)

label4 = Label(window, text = "Task 4", font = ("Times New Roman", 10))
label4.place(x=20, y = 250)
task4 = Entry(window, font = ("Times New Roman", 10), bg = 'white', fg = 'black',width = 39)
task4.place(x = 20, y = 270)

label5 = Label(window, text = "Task 5", font = ("Times New Roman", 10))
label5.place(x=20, y = 310)
task5 = Entry(window, font = ("Times New Roman", 10), bg = 'white', fg = 'black',width = 39)
task5.place(x = 20, y = 330)

start_button = Button(window, text = "Start Studying", command = start_studying, font = ('Times New Roman', 15),compound = 'bottom' )
start_button.pack(side=BOTTOM, pady = 30)

window.mainloop()