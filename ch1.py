import pandas as pd
import numpy as numpy
import platform
import matplotlib.pyplot as plt

path = "C:\Windows\Fonts\malgun.ttf"

from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
     font_name = font_manager.FontProperties(fname=path).get_name()
     rc('font', family=font_name)
else:
     print("Unknown system... sorry~~~")

     plt.rcParams['axes.unicode_minus'] = False
