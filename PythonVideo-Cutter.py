import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def divide_and_arrange_videos(input_file):
    # Duration of each subclip in seconds (5 minutes = 300 seconds)
    subclip_duration = 300

    # Create a folder to store the subclips
    folder_name = "subclips"
    os.makedirs(folder_name, exist_ok=True)

    # Load the input video file
    video = VideoFileClip(input_file)

    # Get the total duration of the input video in seconds
    total_duration = video.duration

    # Calculate the number of subclips needed
    num_subclips = min(max(int(total_duration / subclip_duration), 2), 5)

    # Divide the input video into subclips
    subclips = []
    for i in range(num_subclips):
        start_time = i * subclip_duration
        end_time = min((i + 1) * subclip_duration, total_duration)
        subclip = video.subclip(start_time, end_time)
        subclip_path = os.path.join(folder_name, f"subclip{i+1}.mp4")
        subclip.write_videofile(subclip_path, codec="libx264", audio_codec="aac")
        subclips.append(subclip_path)

    # Concatenate the subclips in the desired order (1-2-3)
    arranged_clip = concatenate_videoclips([VideoFileClip(subclip) for subclip in subclips[:3]])

    # Save the final arranged video
    arranged_clip.write_videofile("arranged_video.mp4", codec="libx264", audio_codec="aac")

    # Print success message
    print("Video processing completed successfully!")

# Prompt for the path to the input video file
input_file_path = input("Enter the path to the input MP4 file: ")
divide_and_arrange_videos(input_file_path)
