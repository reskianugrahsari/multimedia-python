import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import subprocess
import tempfile
import os

# Create the main window
root = tk.Tk()
root.title("Multimedia Application")

# Define the function to play music
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)

        # Create a temporary file with delete=False
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio_file:
            temp_file_path = temp_audio_file.name
            audio.export(temp_file_path, format="mp3")
        
        # Play the audio using ffplay
        subprocess.call(['ffplay', '-nodisp', '-autoexit', temp_file_path])

        # Remove the temporary file after playback is finished
        os.remove(temp_file_path)

# Create a button to play music
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Run the Tkinter event loop
root.mainloop()