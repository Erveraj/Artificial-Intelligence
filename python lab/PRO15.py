import numpy as np
from scipy.io.wavfile import write

sample_rate = 44100
note_duration = 0.5

notes = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00
}

melody = ['C4', 'D4', 'E4', 'F4', 'G4', 'G4', 'F4', 'E4']

music = np.array([], dtype=np.float64)

for note in melody:
    t = np.linspace(
        0, note_duration,
        int(sample_rate * note_duration),
        endpoint=False
    )
    tone = 0.5 * np.sin(2 * np.pi * notes[note] * t)
    music = np.concatenate((music, tone))

audio = np.int16(music * 32767)
write("music.wav", sample_rate, audio)

print("Music synthesized successfully.")
print("Notes:", melody)
print("File created: music.wav")