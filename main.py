"""
Должны существовать источники волн, абсолютные препятствия и экраны
А насколько будет гибкая настройка источника?
Окей, пункт первый: все источники одинаковые и есть абсолютные препятствия
"""
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

import glob, os
from PIL import Image

import timeit

'''
Создание директории
'''
try:
    os.mkdir("frames")
except OSError:
    print("OSError")

for file in glob.glob('frames/*'):
    os.remove(file)

'''
Путь до картинок и до GIF
'''
fp_in = "frames/step*.png"
fp_out = "image.gif"

x_r = np.arange(-1, 1, 0.01)
y_r = np.arange(-1, 1, 0.01)
    
xgrid, ygrid = np.meshgrid(x_r, y_r)
'''
Создание источника(координаты x и y, длина волны и период)
E(r, t)=E_0*cos(k*r + w*t + phi_0)
'''
def create_new_source(x, y, l, t, phi):
    x_shift = xgrid-x
    y_shift = ygrid-y

    radius = np.sqrt(x_shift**2+y_shift**2)
    data = np.cos(-radius*2*np.pi/l + 2*np.pi/t*time_wave + phi)
    return data

'''
Параметры
'''
PAR_L = 1/3
PAR_T = 100

t = timeit.default_timer()
'''
Рисование N картинок
'''
for time_wave in range (0, 100, 5):
    data = xgrid - xgrid
    
    data += create_new_source(0, 0, PAR_L, PAR_T, 0)
    data += create_new_source(0, 0, PAR_L/2, PAR_T, 0)
    
    plt.imshow(data, cmap=cm.seismic)
    
    filename = 'frames/step'+str(100000+time_wave)[1:]+'.png'
    plt.savefig(filename, dpi=50)
    plt.gca()
    
print(timeit.default_timer()-t)
'''
Создание GIF из картинок
'''
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=50, loop=0)
