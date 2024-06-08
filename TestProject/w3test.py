import pandas as pd
import numpy as np

d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

df = pd.DataFrame(data=d)

print(df)

count_row = df.shape[0]

print()
print(count_row)

pulse_readings = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]

print(pulse_readings)

print(max(pulse_readings))

print(min(pulse_readings))

average_pulse = np.mean(pulse_readings)

print(average_pulse)