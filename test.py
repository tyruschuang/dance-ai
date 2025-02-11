from detect import process_video
from compare import compare
from grade import similarity
import pandas as pd

video_to_process = 'enter_video_name'
data_to_compare = 'enter_video_name'

process_video(f"video/{video_to_process}.mp4", f"out/{video_to_process}.csv")
print("Processing complete")
values = compare(pd.read_csv(f"out/{video_to_process}.csv"), pd.read_csv(f"out/{data_to_compare}.csv"))

similarity = similarity(values[0], values[1], values[2])

print(f'Grade given:')
print(f'Position Similarity: {similarity[0]}')
print(f'Velocity Similarity: {similarity[1]}')
print(f'Acceleration Similarity: {similarity[2]}')
print(f'Global Similarity: {similarity[3]}')