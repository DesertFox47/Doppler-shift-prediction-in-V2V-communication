import math
import csv
import random




def doppler_shift_and_gain(V1, V2, angle_degrees, frequency):
    # Convert angle to radians
    angle_radians = math.radians(angle_degrees)
    
    # Calculate the relative velocity between the vehicles
    relative_velocity = math.sqrt(V1**2 + V2**2 - 2 * V1 * V2 * math.cos(angle_radians))
    
    # Calculate the observed frequency using the Doppler shift formula
    observed_frequency = calculate_doppler_shift(frequency, V1, V2)
    
    # Calculate the gain based on the ratio of observed frequency to emitted frequency
    gain = observed_frequency / frequency
    
    return observed_frequency, gain

def calculate_doppler_shift(f, vr, vs):
    c = 3  # Speed of light in meters per second

    # Calculate the Doppler-shifted frequency
    f_prime = f * (c + vr) / (c + vs)

    return f_prime

def calculate_acceleration(x_acc, y_acc, z_acc):
    # Calculate the total acceleration magnitude
    total_acceleration = math.sqrt(x_acc**2 + y_acc**2 + z_acc**2)
    
    return total_acceleration



def random_take_data():
    # Input velocities and angle in degrees
    V1 = float(random.uniform(0, 10000))
    V2 = float(random.uniform(0, 10000))
    angle_degrees = float(random.uniform(0, 360))
    frequency = float(5.9) # 5.9 G Hz
    time = 5  # Time in seconds (you can change this value as needed)

    
    # Calculate Doppler shift and gain at 0 second
    observed_frequency, gain = doppler_shift_and_gain(V1, V2, angle_degrees, frequency)

    x_acc = float(random.uniform(0, 1000))
    y_acc = float(random.uniform(0, 1000))
    z_acc = float(random.uniform(0, 1000))

    # Calculate acceleration, change in direction, and yaw angle
    total_acceleration = calculate_acceleration(x_acc, y_acc, z_acc)
    #roll_angle_deg, pitch_angle_deg, yaw_angle_deg = calculate_change_in_direction(x_acc, y_acc, z_acc)
    
    # parameters after 5 second 
    V1_t5 = V1 + (total_acceleration * time)
    angle_radians_t5 = math.acos((V1**2 + V2**2 - (total_acceleration * time)**2) / (2 * V1 * V2))
    angle_degrees_t5 = math.degrees(angle_radians_t5)
    observed_frequency_t5, gain_t5 = doppler_shift_and_gain(V1_t5, V2, angle_degrees_t5, frequency)
    
    d1=[V1, V2, x_acc, y_acc, z_acc, angle_degrees, observed_frequency, gain, observed_frequency_t5, gain_t5, angle_degrees_t5]
    return d1

def write_data(data):
    
    # CSV file path
    csv_file_path = "data_forged.csv"

    # Write data to CSV file
    with open(csv_file_path, mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)

def write_data_fresh(data):
    
    # CSV file path
    csv_file_path = "data_forged.csv"

    # Write data to CSV file
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)


data=[["V1", "V2", "x_acc", "y_acc", "z_acc", "angle_degrees", "observed_frequency", "gain", "observed_frequency_t5", "gain_t5", "angle_degrees_t5"]]
#["V1", "V2", "x_acc", "y_acc", "z_acc", "angle_degrees", "observed_frequency", "gain", "observed_frequency_t5", "gain_t5", "angle_degrees_t5"]
write_data_fresh(data)
data=[]
i=0
while(i<10000):
    try:
        data=data+[random_take_data()]
        i+=1
    except:
        #i-=i
        pass

#print (data)
write_data(data)
print("done making data")