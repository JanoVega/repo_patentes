# -*- coding: utf-8 -*-
"""
TSP
"""
import matplotlib.pyplot as plt
import numpy as np


from PIL import Image
from numba import njit,prange



#%%
def phi(r):
    if r==0:
        return 0
    return r**2*np.log(r**2)

#%%
def grid_generator(H,W,C,T):
    """
    Parameters
    ----------
    im : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    #W,H = im.size
    # se generan pixeles p en una lista
    G = [np.array([w/(W-1),h/(H-1)]) for h in range(H) for w in range(W) ]
   
    # se obtienen las nuevas coordenadas de los pixeles, p'
    for _,p in enumerate(G):
        x,y = T*proyeccion_lineal(p,C)
        
        # se reescala al tamaño de la imagen
        x = int(x*(W-1))
        y = int(y*(H-1))
        
        # se aplica un clipping para dejar la grilla dentro de los bordes de la imagen
        x = np.clip( x, 0, W-1)
        y = np.clip( y, 0, H-1)
        
        # es construida la grilla para utilizar en el sampler
        G[_] = np.array([x, y]) 
    
    return G
#%%
def proyeccion_lineal(p,C):
    # np.array dim (2,1)
    if C.shape[1]!=2:
        C = C.T
    
    phi_p = np.matrix([phi(np.linalg.norm(p-c)) for c in C ])
    pp_1 = np.hstack([1,p])
    pp_1 = np.matrix(pp_1)
    pp = np.hstack((pp_1,phi_p)).T
    
    return pp

#%%
@njit(parallel=True)
def sampler(G,im):
    # im -> np.array
    H,W = im.shape
    V = [0 for _ in range(W*H)]
    # aplico el sampling kernel
    for i in prange(W*H):
        for h in range(H):
            for w in range(W):
                V[i] += im[h][w]\
                           *max(0, 1-abs(G[i][0]-w))\
                           *max(0, 1-abs(G[i][1]-h))     
    return V


#%% La transformacion



def TSP_generator(C,C_prima):
    """
    Genera la transformacion a partir de conjuntos de puntos en los contornos

    Parameters
    ----------
    C : 2x(2*K) np.array
        
    C_prima : 2x(2*K) np.array
        
    Returns
    -------
    T : 2x(2*K+3) 
        Transformacion para una deformar imagen.

    """
    K = int(C.shape[1]/2)
    
    C_gorro = np.matrix([[phi(np.linalg.norm(c-cp)) for c in C.T ] for cp in C_prima.T])
    Zeros_2x3 = np.zeros([2,3])
    T_delta_c = np.hstack((C_prima,Zeros_2x3))
    
    delta_c_1 = np.hstack(( np.ones([1,2*K]),np.zeros([1,3])))
    delta_c_2 = np.hstack(( C, Zeros_2x3 ))
    delta_c_3 = np.hstack(( C_gorro, np.ones([2*K,1]), C.T ))
    
    delta_c = np.vstack((delta_c_1, delta_c_2, delta_c_3))
    
    T = T_delta_c*np.linalg.inv(delta_c)    
    return T

#%% test // pasar a funcion

# =============================================================================
# # =============================================================================
# # puntos para el tsp
# 
# K=6
# # 2K puntos 
# C1 = [np.array([n/(K-1),0]) for n in range(0,K)] # puntos (0,0),...,(1,0)
# C2 = [np.array([n/(K-1),-1]) for n in range(0,K)] # puntos (0,1),...,(1,-1)
# C = np.vstack((C1,C2))
# 
# #aqui dejo el cambio en
# dC1=[np.array([0,0+n/K**2]) for n in range(0,K)]
# dC2=[np.array([0,0-n/K**2]) for n in range(0,K)]
# dC_prima = np.vstack((dC1,dC2))
# 
# C_prima = (C+dC_prima).T
# C = C.T
# 
# # =============================================================================
# # obtengo T
# T = TSP_generator(C,C_prima)
# # =============================================================================
# # rectifico una imagen previamente guardada en el kernel
# H,W = im_np.shape
# G = grid_generator(H,W,C,T)
#  
# V = np.array( sampler(G,im_np) ).astype('uint8')
# V2 = np.reshape(V,(H,W))
# im2 = Image.fromarray(V2)



