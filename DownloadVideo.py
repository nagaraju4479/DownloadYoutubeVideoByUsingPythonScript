import pytube

# Ask for the video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object
youtube = pytube.YouTube(url)

# Get the highest quality stream with both audio and video
stream = youtube.streams.get_highest_resolution()

# Get the video title for the output file name
title = youtube.title

# Download the video
print(f"Downloading '{title}' in {stream.resolution}...")
stream.download()
print("Download complete!")
