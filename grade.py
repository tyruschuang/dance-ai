def similarity(position_distance, velocity_distance, acceleration_distance):
    similarity_position = max(0, 100 - position_distance)
    similarity_velocity = max(0, 100 - velocity_distance)
    similarity_acceleration = max(0, 100 - acceleration_distance)

    similarity_global = (
        (similarity_position * 0.65) +
        (similarity_velocity * 0.20) +
        (similarity_acceleration * 0.15)
    )

    return similarity_position, similarity_velocity, similarity_acceleration, similarity_global