import time
from IPython.display import clear_output  # Import clear_output for Jupyter Notebook

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        clear_output(wait=True)  # Clears previous output in Jupyter Notebook
        print(timer)  # Prints the updated timer
        time.sleep(1)
        t -= 1

    clear_output(wait=True)
    print("Timer completed!")

t = int(input("Enter the time in seconds: "))  # Convert input to int
countdown(t)
