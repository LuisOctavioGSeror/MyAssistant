from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
import matplotlib.pyplot
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        fig.patch.set_facecolor('#2b2b2b')  # Fundo cinza escuro
        self.axes.set_facecolor('#2b2b2b')  # Fundo cinza escuro do gráfico

        # Remove os eixos
        self.axes.axis('off')  # Desativa os eixos

        # Ajuste os limites dos eixos Y para controlar o zoom
        self.axes.set_ylim(-100, 100)  # Ajuste os valores conforme necessário
        super(MplCanvas, self).__init__(fig)

    def get_cmap(self):
        return matplotlib.pyplot.get_cmap('YlOrBr')

    def get_cInd(self):
        return matplotlib.colors.Normalize(vmin=0, vmax=80)

    def create_waves(self, numDivs):
        waves = []
        for i in range(0, numDivs):
            wave, = self.axes.plot([0.05 + i / numDivs, 0.05 + i / numDivs], [0, 0], color=self.get_cmap()(self.get_cInd()(i)), linewidth=1)
            waves.append(wave)
        return waves
