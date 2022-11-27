import tkinter as tk
import tkinter.ttk as ttk
import random
import time

# CONSTANTS
DARK_RED = "#880808"
DB0 = "#0E293E"
DB1 = "#142635"
DB2 = "#0C2438"
DB3 = "#051726"
DB4 = "#0A1F31"
DB5 = "#213547"
DB6 = "#192B3B"
DB7 = "#04111C"
DB8 = "#0E1E2B"
TIME_STEP = 1
N_ROWS = 20
N_COLS = N_ROWS
SCREEN_TIME = 20*60 # 20 min
LOOP_COUNT = (24*60*60)/(SCREEN_TIME+5) # roughly 24 hours at 20
BREAK_TIME = 20 # seconds

def createCanvas(window):
  canvas = tk.Canvas(window)
  canvas.pack(fill=tk.BOTH, expand=True)
  return canvas

def backgroundAnimate(window,canvas):
  RECT_WIDTH = canvas.winfo_width()/N_COLS
  RECT_HEIGHT= canvas.winfo_height()/N_ROWS
  count = 0
  while count<BREAK_TIME:
    for row in range(N_ROWS):
      for col in range(N_COLS):
        x = col*RECT_WIDTH
        y = row*RECT_HEIGHT
        squareColor = random.choice([DB0,DB1,DB2,DB3,DB4,DB5,DB6,DB7,DB8])
        canvas.create_rectangle(x,y,x+RECT_WIDTH,y+RECT_HEIGHT,fill=squareColor, outline=squareColor)
    window.update()
    time.sleep(TIME_STEP)
    count+=1
  window.overrideredirect(False)
  window.iconify() # minimize to taskbar/dock

def main():
  window = tk.Tk() # create window
  window.title("20-20-20")
  WIDTH, HEIGHT = window.winfo_screenwidth(), window.winfo_screenheight()
  window.geometry("%dx%d+0+0" % (WIDTH, HEIGHT))
  window.update()

  myCanvas = createCanvas(window)
  window.update()

  # loop until quit or runs for 24 hours
  runCount=0
  while runCount<LOOP_COUNT: # roughly 24 hours
    runCount+=1
    window.attributes("-topmost", True)
    backgroundAnimate(window,myCanvas)
    time.sleep(SCREEN_TIME)
    window.deiconify()

  # end program
  window.destroy()
  window.mainloop()
if __name__ == "__main__":
    main()
