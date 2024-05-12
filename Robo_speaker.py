import pyttsx3
import tkinter as tk

# Initialize the speech engine
voice = pyttsx3.init()


# Function to speak the entered text
def speak():
    text = entry.get()
    if text.lower() == "q":
        voice.say("Bye Bye brother....!")
        voice.runAndWait()
        root.destroy()  # Close the window and end the program
    else:
        voice.say(text)
        voice.runAndWait()


# Create the main application window
root = tk.Tk()
root.title("Robo Speaker")

# Create widgets
label = tk.Label(root, text="Enter what you want me to speak and 'q' to quit:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Speak", command=speak)
button.pack()

# Run the application
root.mainloop()
