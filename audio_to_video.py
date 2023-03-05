import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from moviepy.editor import *
from tkinter.ttk import Progressbar

# Function to generate the video
def generate_video():
    # Get the input audio file path from the user
    audio_file = filedialog.askopenfilename(title="Select audio file",
                                             filetypes=[("Audio files", "*.mp3;*.wav")])
    if not audio_file:
        return
    # Get the input image file path from the user
    image_file = filedialog.askopenfilename(title="Select image file",
                                             filetypes=[("Image files", "*.jpg;*.png")])
    if not image_file:
        return
    # Get the output folder path from the user
    output_folder = filedialog.askdirectory(title="Select output folder")
    if not output_folder:
        return
    # Disable the "Generate Video" button while the video is being generated
    button.config(state=DISABLED)
    # Show a progress bar to indicate that the video is being generated
    progress_bar.start()
    # Load the audio file
    audio = AudioFileClip(audio_file)

    # Load the image
    image = ImageClip(image_file)

    # Set the duration of the video to be the same as the audio
    duration = audio.duration

    # Create a video with the image as the only frame
    video = image.set_duration(duration)

    # Set the size of the video to match the size of the image
    video = video.resize(width=image.w, height=image.h)

    # Set the audio of the video to be the same as the loaded audio
    video = video.set_audio(audio)

    # Set the output video file name to be the same as the input audio file name
    output_file = os.path.splitext(os.path.basename(audio_file))[0] + ".mp4"

    # Concatenate the output folder path and the output file name to get the full output file path
    output_path = os.path.join(output_folder, output_file)

    # Write the video to the output file
    video.write_videofile(output_path, fps=24)

    # Stop the progress bar and re-enable the "Generate Video" button
    progress_bar.stop()
    button.config(state=NORMAL)

    # Show a message box to inform the user that the video has been generated
    messagebox.showinfo("Video Generation", "Video has been generated successfully.")

# Create the main window
root = Tk()
root.title("Audio 2 Video Generator By LKN")

# Set the window size and background color
root.geometry("400x200")
root.configure(bg="#F5F5F5")

# Create the title label
title_label = Label(root, text="Audio 2 Video Generator By LKN", font=("Arial", 20), bg="#F5F5F5")
title_label.pack(pady=10)

# Create the description label
description_label = Label(root, text="Select an audio file and an image file to generate a video.", bg="#F5F5F5")
description_label.pack(pady=5)

# Create the "Generate Video" button
button = Button(root, text="Generate Video", command=generate_video, bg="#4CAF50", fg="white", activebackground="#60B044")
button.pack(pady=10)

# Create the progress bar
progress_bar = Progressbar(root, orient=HORIZONTAL, length=200, mode="indeterminate")
progress_bar.pack(pady=10)

# Run the main loop
root.mainloop()
