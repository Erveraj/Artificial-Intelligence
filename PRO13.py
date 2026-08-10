#Program No 13: Visualize an Audio Speech Signal in Python
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

sample_rate, audio = wavfile.read("speech.wav")

if len(audio.shape) > 1:
    audio = audio[:, 0]

time = np.arange(len(audio)) / sample_rate

plt.plot(time, audio)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Speech Signal Waveform")
plt.show()

print("Sample Rate:", sample_rate, "Hz")
print("Number of Samples:", len(audio))
