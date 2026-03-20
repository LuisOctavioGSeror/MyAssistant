import numpy as np
import pyaudio
from scipy import signal as sig

import localization


class AudioProcessor:
    def __init__(self, canvas):
        self.canvas = canvas
        self.numDivs = 80
        self.freq = []
        self.PSD = []
        self.amp = np.zeros(self.numDivs)
        self.divs = np.zeros(self.numDivs)
        self.sampleRate = 44100
        self.chunk = 256
        self.bandwidth = 2
        self.channels = 1
        self.stream = None

        self.cMap = self.canvas.get_cmap()
        self.cInd = self.canvas.get_cInd()
        self.waves = self.canvas.create_waves(self.numDivs)

        # Inicializa PyAudio
        self.p = pyaudio.PyAudio()
        self.inputChannel = self.get_input_channel()

        # Definir freqDivs para dividir as faixas de frequência
        self.freqDivs = self.calculate_freq_divs()

    def calculate_freq_divs(self):
        freqDivs = []
        freqDivs.append([0])
        freqDivs.append([1, 2])
        for i in range(2, self.numDivs):
            prevLow = freqDivs[i - 1][0]
            prevHigh = freqDivs[i - 1][1]
            freqDivs.append([prevHigh + 1, prevHigh + 1 + int((prevHigh - prevLow) * 1.0625)])
        return freqDivs

    def get_input_channel(self):
        try:
            default_device = self.p.get_default_input_device_info()
            return int(default_device.get("index"))
        except Exception:
            device_info = self.p.get_host_api_info_by_index(0)
            num_devices = device_info.get("deviceCount", 0)
            for i in range(num_devices):
                details = self.p.get_device_info_by_host_api_device_index(0, i)
                if int(details.get("maxInputChannels", 0)) > 0:
                    return i
            return None

    def start_stream(self):
        try:
            self.stream = self.p.open(format=self.p.get_format_from_width(self.bandwidth),
                                      channels=self.channels, rate=self.sampleRate,
                                      input=True, output=False,
                                      input_device_index=self.inputChannel,
                                      frames_per_buffer=self.chunk,
                                      stream_callback=self.callback)
        except Exception as e:
            print(f"{localization.tr('audio_viz_disabled')}: {e}")
            return

        # Inicia a animação
        from matplotlib.animation import FuncAnimation
        self.animation = FuncAnimation(self.canvas.figure, self.update, interval=15, cache_frame_data=False)

    def callback(self, in_data, frame_count, time_info, status):
        audio = np.frombuffer(in_data, dtype=np.int16)
        self.freq, self.PSD = sig.periodogram(audio, self.sampleRate, nfft=int(self.sampleRate / 10))
        return in_data, pyaudio.paContinue

    def stop_stream(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()

    def update(self, frame):
        if not self.PSD.any():
            return  # Aguarda a coleta dos dados
        self.divs[0] = self.PSD[0] ** 0.5
        self.waves[0].set_ydata([-self.divs[0], self.divs[0]])
        for i in range(1, self.numDivs):
            self.divs[i] = np.average(self.PSD[int(self.freqDivs[i][0]):int(self.freqDivs[i][1])]) ** 0.5
            if self.divs[i] > self.amp[i]:
                self.amp[i] = self.divs[i]
            elif self.divs[i] < self.amp[i]:
                self.amp[i] = self.amp[i] - (self.amp[i] - self.divs[i]) / 1.8
            self.waves[i].set_ydata([-self.amp[i], self.amp[i]])
        self.canvas.draw()  # Atualiza o canvas
