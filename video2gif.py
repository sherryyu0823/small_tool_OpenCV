import cv2
import imageio
import os
from pathlib import Path

# Convert the videos to gif in a folder
for filename in os.listdir("Your Folder"):
	# print(filename)
	if(filename != 'gif'):
		path = "your folder/"+filename
		print(path)
		video_cap = cv2.VideoCapture(path)
		frame_count = 0
		all_frames = []
		while True:
			ret, frame = video_cap.read()
			if ret is False:
				break
			frame = frame[..., ::-1]   # opencv BGR to RGB
			all_frames.append(frame)
			# cv2.imshow('frame', frame)
			cv2.waitKey(1)
			frame_count += 1
			# print(frame_count)
		video_cap.release()
		cv2.destroyAllWindows()
		print('===>', len(all_frames))

		# all_frames

		# print(filename)
		file_name = Path(filename).stem
		print(file_name)
	# def frame_to_gif(frame_list):
		gif = imageio.mimsave(("your folder/%s.gif" %file_name), all_frames, 'GIF', duration=0.00085)  
