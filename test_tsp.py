# -*- coding: utf-8 -*-

import numpy as np

from PIL import Image

from gris_nuevo import patents_l

from tesseract_fun import test_sin_preproc
from tesseract_fun import test_Opt_Sr
from tesseract_fun import test_RS

from TSP import TSP_generator
from TSP import grid_generator
from TSP import sampler

# se seleccion ala imagen para relizar la prueba
XY = patents_l.get_labels()
im = Image.open('.\\gris_nuevo\\'+XY[170][0]).convert('L')


# predicciones sin correccion al paralaje

print('sin preprocesamiento: ', test_sin_preproc(im,10))

for n in range(0,6):
    print('resize 144x48 con opcion '+ str(n)+': ', test_RS(im, n, (144,48)))

print('resize 144x48 -bicubic con sr: ', test_Opt_Sr(im, 10, True))


# aplicando correccion 
im_np = np.asarray(im)

# puntos para el tsp // la mejor prediccion es con K = 6
K = 6
# 2K puntos 
C1 = [np.array([n/(K-1),0]) for n in range(0,K)] # puntos (0,0),...,(1,0)
C2 = [np.array([n/(K-1),-1]) for n in range(0,K)] # puntos (0,1),...,(1,-1)
C = np.vstack((C1,C2))
 
# aqui dejo el cambio en
dC1=[np.array([0,0+n/K**2]) for n in range(0,K)]
dC2=[np.array([0,0-n/K**2]) for n in range(0,K)]
dC_prima = np.vstack((dC1,dC2))
 
C_prima = (C+dC_prima).T
C = C.T
 
# =============================================================================
# obtengo T
T = TSP_generator(C,C_prima)
# =============================================================================
# rectifico una imagen previamente guardada en el kernel
H,W = im_np.shape
G = grid_generator(H,W,C,T)
 
V = np.array( sampler(G,im_np) ).astype('uint8')
V2 = np.reshape(V,(H,W))
im2 = Image.fromarray(V2)

print('mismos tests anteriores pero con la transformacion aplicada \n')

print('sin preprocesamiento: ', test_sin_preproc(im2,10))

for n in range(6):
    print('resize 144x48 con opcion '+ str(n)+': ', test_RS(im2, n, (144,48)))

print('resize 144x48 -bicubic con sr: ', test_Opt_Sr(im2, 10, True))


