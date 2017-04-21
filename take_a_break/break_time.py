import webbrowser

import time

url = "https://youtu.be/JWUVJTnuOds"

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())

while(break_count < total_breaks):
    # delay for 10 seconds
    time.sleep(3)
    # Open URL in a new tab, if a browser window is already open
    webbrowser.open_new_tab(url)
    break_count += 1