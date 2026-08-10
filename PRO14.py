#Program No 14: Generate Audio Signals Using Python
import numpy as np
from scipy.io.wavfile import write

sample_rate = 44100
duration = 2
frequency = 440

time = np.linspace(
    0, duration,
    int(sample_rate * duration),
    endpoint=False
)

signal = 0.5 * np.sin(2 * np.pi * frequency * time)
audio = np.int16(signal * 32767)

write("generated_signal.wav", sample_rate, audio)

print("Audio signal generated successfully.")
print("Frequency:", frequency, "Hz")
print("Duration:", duration, "seconds")
