import parselmouth

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set() # Use seaborn's default style to make attractive graphs
plt.rcParams['figure.dpi'] = 100 # Show nicely large images in this notebook

snd1 = parselmouth.Sound("output.mp3")
snd2 = parselmouth.Sound("in2.wav")
def draw_spectrogram(spectrogram, dynamic_range=70):
    X, Y = spectrogram.x_grid(), spectrogram.y_grid()
    sg_db = 10 * np.log10(spectrogram.values)
    plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - dynamic_range, cmap='afmhot')
    plt.ylim([spectrogram.ymin, spectrogram.ymax])
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")

def draw_intensity(intensity):
    limpio = [i if i >= 60 else 0 for i in intensity.values[0]]
    print(limpio)
    plt.plot(intensity.xs(), limpio, linewidth=3, color='w')
    plt.plot(intensity.xs(), limpio, linewidth=1)
    plt.grid(False)
    plt.ylim(0)
    plt.ylabel("intensity [dB]")

intensity = snd1.to_intensity()
spectrogram = snd1.to_spectrogram()

plt.figure()
draw_spectrogram(spectrogram)
plt.twinx()
draw_intensity(intensity)
plt.xlim([snd1.xmin, snd1.xmax])
plt.savefig("bot2.png")

intensity = snd2.to_intensity()
spectrogram = snd2.to_spectrogram()
plt.figure()
draw_spectrogram(spectrogram)
plt.twinx()
draw_intensity(intensity)
plt.xlim([snd2.xmin, snd2.xmax])
plt.savefig("sound12.png")
