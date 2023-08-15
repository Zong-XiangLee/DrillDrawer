from drawer import window
from gui import GUI

if GUI.window_scale == 0:
    print("hello world")
else:
    window.init_window()
    window.turtle.delay(delay=None)
    window.outline()
    window.turtle.mainloop()
