import cv2
import imageio
import os
from pathlib import Path


# with open(os.path.join("./result2.0/DF", filename), 'r') as f:
#     text = f.read()
# for filename in os.listdir("./result2.0/FB"):
#     print(filename)

# def read_video(path):
# frame_list = read_video('./result2.0/rlof_d1.mp4')
# 		frame_to_gif(frame_list)

for filename in os.listdir("./result2.0/DF"):
	# print(filename)
	if(filename != 'gif'):
		path = "./result2.0/DF/"+filename
		print(path)
		video_cap = cv2.VideoCapture(path)
		frame_count = 0
		all_frames = []
		while True:
			ret, frame = video_cap.read()
			if ret is False:
				break
			frame = frame[..., ::-1]   # opencv读取BGR，转成RGB
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
		gif = imageio.mimsave(("./result2.0/DF/gif/%s.gif" %file_name), all_frames, 'GIF', duration=0.00085)  
	# duration 表示图片间隔


# if __name__ == "__main__":
	# frame_list = read_video('./result2.0/rlof_d1.mp4')
	# frame_to_gif(frame_list)
