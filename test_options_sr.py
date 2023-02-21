# -*- coding: utf-8 -*-
""" las imagenes son reajustadas a un tamaño de 144 x 48 pixeles, utilizando un
    resampling cubico.
"""

import re

from PIL import Image

from tesseract_fun import test_Opt_Sr
from tesseract_fun import test_sin_preproc

from gris_nuevo import patents_l
# cargo las patentes
XY = patents_l.get_labels()


# se mide la a cuantos caracteres se acierta x palabra

#%% test sin preprocesamiento
aciertos_x_option_wo_proc=[]
for n in range(14):
    aciertos_foto_i = []
    for foto in XY:
        # foto[0] es el nombre del archivo; foto[1] es la etiqueta correspondiente
        csv_row = [foto[0],\
                   foto[1],\
                       ]
        try:
            im = Image.open('.\\gris_nuevo\\'+foto[0])
            text = test_sin_preproc(im, n)
            text = re.sub( '[\W_]','', text)    
        except :
            pass
        try:
            text = text[:6]
        except:
            pass
        W1 = [letra for letra in foto[1]]
        W2 = [letra for letra in text]
        
        m=0
        for i in range(6):
            try:
                m += W1[i]==W2[i]
            except:
                pass
        aciertos_foto_i.append(m)
    aciertos_x_option_wo_proc.append(sum(aciertos_foto_i)/6/358)
    
#%% wo sr
aciertos_x_option_wo_sr=[]
for n in range(13):
    aciertos_foto_i = []
    for foto in XY:
        # foto[0] es el nombre del archivo; foto[1] es la etiqueta correspondiente
        csv_row = [foto[0],\
                   foto[1],\
                       ]
        try:
            im = Image.open('.\\gris_nuevo\\'+foto[0])
            text = test_Opt_Sr(im, n, False)
            text = re.sub( '[\W_]','', text)    
        except :
            pass
        try:
            text = text[:6]
        except:
            pass
        W1 = [letra for letra in foto[1]]
        W2 = [letra for letra in text]
        
        m=0
        for i in range(6):
            try:
                m += W1[i]==W2[i]
            except:
                pass
        aciertos_foto_i.append(m)
    aciertos_x_option_wo_sr.append(sum(aciertos_foto_i)/6/358)
#%% w/wo sr opcion 13
aciertos_x_option13_w_wo_sr=[]
for n in [True, False]:
    aciertos_foto_i = []
    for foto in XY:
        # foto[0] es el nombre del archivo; foto[1] es la etiqueta correspondiente
        csv_row = [foto[0],\
                   foto[1],\
                       ]
        try:
            im = Image.open('.\\gris_nuevo\\'+foto[0])
            text = test_Opt_Sr(im, 13, n)
            text = re.sub( '[\W_]','', text)    
        except :
            pass
        try:
            text = text[:6]
        except:
            pass
        W1 = [letra for letra in foto[1]]
        W2 = [letra for letra in text]
        
        m=0
        for i in range(6):
            try:
                m += W1[i]==W2[i]
            except:
                pass
        aciertos_foto_i.append(m)
    aciertos_x_option13_w_wo_sr.append(sum(aciertos_foto_i)/6/358)

#%% w sr
aciertos_x_option_w_sr=[]
for n in range(13):
    aciertos_foto_i = []
    for foto in XY:
        # foto[0] es el nombre del archivo; foto[1] es la etiqueta correspondiente
        csv_row = [foto[0],\
                   foto[1],\
                       ]
        try:
            im = Image.open('.\\gris_nuevo\\'+foto[0])
            text = test_Opt_Sr(im, n, True)
            text = re.sub( '[\W_]','', text)    
        except :
            pass
        try:
            text = text[:6]
        except:
            pass
        W1 = [letra for letra in foto[1]]
        W2 = [letra for letra in text]
        
        m=0
        for i in range(6):
            try:
                m += W1[i]==W2[i]
            except:
                pass
        aciertos_foto_i.append(m)
    aciertos_x_option_w_sr.append(sum(aciertos_foto_i)/6/358)
    


