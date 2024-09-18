import random
import string
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Parameters for player movement
walk_speed = 4.317
sprint_speed = 5.612
sprint_jump_speed = 7.127
speed_2_modifier = 1.4
tick_interval = 0.05
max_sprint_jump_speed_with_potion = sprint_jump_speed * speed_2_modifier

# Function to add noise
def add_noise(value, noise_level=0.05):
    """Adds noise to the given value. The noise level defines the max percentage of variation."""
    noise = value * noise_level * (random.uniform(-1, 1))  # Add noise as a percentage of the value
    return value + noise

def generate_player_logs(start_time, num_ticks, is_cheater):
    player_name = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    log_data = []
    x, y, z = -34.612, 65.621, -12.345
    pitch, yaw = 25.7, 3.2
    
    for tick in range(num_ticks):
        time = start_time + timedelta(seconds=tick * tick_interval)
        has_speed_potion = random.random() < 0.1  # Random potion application

        if is_cheater and random.random() < 0.1:
            # Simulate cheating behavior
            current_cheat_type = random.choice(['speed', 'teleport', 'fly', 'aim_assist'])

            if current_cheat_type == 'speed':
                distance = random.uniform(sprint_speed * 2, sprint_jump_speed * 3 * tick_interval)
            elif current_cheat_type == 'teleport':
                distance = random.uniform(30, 50)
            elif current_cheat_type == 'fly':
                distance = random.uniform(0.5, 2.0)
                y += random.uniform(5, 10)
            elif current_cheat_type == 'aim_assist':
                distance = random.uniform(0.5, 2.0)
                yaw += random.uniform(45, 90)
        else:
            # Legitimate movement with added noise
            movement_type = random.choices(
                ['walking', 'sprinting', 'sprint_jumping'], weights=[0.3, 0.4, 0.3], k=1)[0]

            if movement_type == 'walking':
                distance = add_noise(random.uniform(0.1, walk_speed * tick_interval), noise_level=0.1)
            elif movement_type == 'sprinting':
                distance = add_noise(random.uniform(sprint_speed * tick_interval, sprint_speed * tick_interval), noise_level=0.1)
            elif movement_type == 'sprint_jumping':
                distance = add_noise(random.uniform(sprint_jump_speed * tick_interval, sprint_jump_speed * tick_interval), noise_level=0.1)

            yaw_change = add_noise(random.uniform(-5, 5), noise_level=0.1)
            yaw += yaw_change

        # Add noise to position
        x += add_noise(distance * np.cos(np.radians(yaw)), noise_level=0.05)
        z += add_noise(distance * np.sin(np.radians(yaw)), noise_level=0.05)
        y += add_noise(0, noise_level=0.01)  # Adding very small noise to vertical movement

        log_data.append({
            'timestamp': time,
            'player': player_name,
            'x1': x - distance, 'y1': y, 'z1': z - distance,
            'pitch1': pitch, 'yaw1': yaw - yaw_change if not is_cheater else yaw,
            'x2': x, 'y2': y, 'z2': z,
            'pitch2': pitch, 'yaw2': yaw,
            'has_speed_potion': int(has_speed_potion),  # Boolean encoded as 1/0
            'cheating': 1 if is_cheater else 0  # Cheating encoded as 1/0
        })

    return pd.DataFrame(log_data)
