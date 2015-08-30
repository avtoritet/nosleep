# This short script will keep mouse-clicking every 60 sec
# for n amount of minutes to not let computer fall asleep
import win32api, win32con, time

# Total time
MINUTES = 60

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

for i in range (0, MINUTES):
    click(55, 0)
    time.sleep(30)
    click(85, 0)
    time.sleep(30)
