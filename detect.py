import mediapipe as mp
import cv2
import csv
from mediapipe.python.solutions.pose import PoseLandmark

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

included_pose_landmarks = [
	PoseLandmark.NOSE,
	PoseLandmark.LEFT_ANKLE,
	PoseLandmark.LEFT_ELBOW,
	PoseLandmark.LEFT_EYE,
	PoseLandmark.LEFT_HIP,
	PoseLandmark.LEFT_KNEE,
	PoseLandmark.LEFT_SHOULDER,
	PoseLandmark.LEFT_WRIST,
	PoseLandmark.RIGHT_ANKLE,
	PoseLandmark.RIGHT_ELBOW,
	PoseLandmark.RIGHT_EYE,
	PoseLandmark.RIGHT_HIP,
	PoseLandmark.RIGHT_KNEE,
	PoseLandmark.RIGHT_SHOULDER,
	PoseLandmark.RIGHT_WRIST
]

def process_video(video_path, output_csv, annotate=False, frame_skip=2):
	# Load the MediaPipe Pose model
	pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

	# Open the video file
	cap = cv2.VideoCapture(video_path)

	# Open the output CSV file
	with open(output_csv, mode='w', newline='') as file:
		writer = csv.writer(file)

		# Write the header row to the CSV file
		header = []
		for pose_index in included_pose_landmarks:
			header += [pose_index.name + '_x', pose_index.name + '_y']

		writer.writerow(header)

		frame_count = 0

		# Process each frame in the video
		while cap.isOpened():
			# Read the next frame from the video
			ret, frame = cap.read()
			# If the frame cannot be read, then we have reached the end of the video
			if not ret:
				break

			frame_count += 1
			if frame_count % frame_skip == 0:
				continue

			frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

			# Process the frame to get pose landmarks
			results = pose.process(frame_rgb)
			landmarks = results.pose_landmarks

			body_landmarks = []

			# Save the landmarks to the CSV file
			if landmarks is None:
				continue
			for pose_index in included_pose_landmarks:
				body_landmarks += [landmarks.landmark[pose_index.value].x, landmarks.landmark[pose_index.value].y]

			writer.writerow(body_landmarks)

			if annotate:
				# Display the annotated frame
				annotated_frame = frame.copy()
				mp_drawing.draw_landmarks(annotated_frame, landmarks, mp_pose.POSE_CONNECTIONS)
				cv2.imshow('MediaPipe Pose', annotated_frame)

				# Wait for the user to press the 'q' key to stop the video
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break

	# Close objects
	cap.release()
	file.close()
	cv2.destroyAllWindows()
	pose.close()
