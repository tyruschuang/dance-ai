import pandas as pd
import numpy as np
from dtaidistance import dtw_ndim

def compare(reference_data, input_data):
	# TODO: Implement data normalization

	reference_velocity = np.diff(reference_data.values, axis=0)
	reference_velocity = np.vstack([np.zeros((1, reference_velocity.shape[1])), reference_velocity])  # Add zero row to match original length
	
	# Calculate acceleration (second derivative)
	reference_acceleration = np.diff(reference_velocity, axis=0)
	reference_acceleration = np.vstack([np.zeros((1, reference_acceleration.shape[1])), reference_acceleration])  # Add zero row to match original length
	
	input_velocity = np.diff(input_data.values, axis=0)
	input_velocity = np.vstack([np.zeros((1, input_velocity.shape[1])), input_velocity])  # Add zero row to match original length

	# Calculate acceleration (second derivative)
	input_acceleration = np.diff(input_velocity, axis=0)
	input_acceleration = np.vstack([np.zeros((1, input_acceleration.shape[1])), input_acceleration])  # Add zero row to match original length
	
	position_distance = dtw_ndim.distance(reference_data.values, input_data.values)
	velocity_distance = dtw_ndim.distance(reference_velocity, input_velocity)
	acceleration_distance = dtw_ndim.distance(reference_acceleration, input_acceleration)
	
	print(f'Position Distance: {position_distance}')
	print(f'Velocity Distance: {velocity_distance}')
	print(f'Acceleration Distance: {acceleration_distance}')
	
	# Calculate velocity (first derivative)
	return position_distance, velocity_distance, acceleration_distance