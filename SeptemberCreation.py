import pandas as pd
import random
import numpy as np

# Generate normal network data
def generate_normal_data(num_samples):
    data = []
    for _ in range(num_samples):
        src_ip = f"192.168.1.{random.randint(1, 255)}"
        dst_ip = f"10.0.0.{random.randint(1, 255)}"
        protocol = random.choice(['TCP', 'UDP', 'ICMP'])
        bytes_transferred = random.randint(100, 5000)
        data.append([src_ip, dst_ip, protocol, bytes_transferred, 'normal'])
    return data

# Generate anomalous network data
def generate_malicious_data(num_samples):
    data = []
    for _ in range(num_samples):
        src_ip = f"172.16.{random.randint(1, 10)}.{random.randint(1, 255)}"
        dst_ip = f"10.0.0.{random.randint(1, 255)}"
        protocol = random.choice(['TCP', 'UDP'])
        bytes_transferred = random.randint(5000, 100000)  # Larger byte counts to simulate attack
        data.append([src_ip, dst_ip, protocol, bytes_transferred, 'malicious'])
    return data

# Combine normal and malicious data into one dataset
def create_dataset():
    normal_data = generate_normal_data(1000)  # 1000 normal entries
    malicious_data = generate_malicious_data(200)  # 200 malicious entries
    
    # Combine and shuffle the dataset
    dataset = normal_data + malicious_data
    random.shuffle(dataset)
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(dataset, columns=['Source IP', 'Destination IP', 'Protocol', 'Bytes Transferred', 'Label'])
    return df

# Create and save the dataset
df = create_dataset()
df.to_csv('network_traffic_dataset.csv', index=False)
print(df.head())

