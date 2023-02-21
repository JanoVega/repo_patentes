# -*- coding: utf-8 -*-

import re

from PIL import Image

from tesseract_fun import test_RS
from gris_nuevo import patents_l

from modelo_prod import sr_w_vdsr
# cargo las patentes
XY = patents_l.get_labels()


# se mide la a cuantos caracteres se acierta x palabra
#%% size = 160 x80
aciertos_x_option_2x1=[]
for n in range(6):
    aciertos_foto_i = []
    for foto in XY:
        # foto[0] es el nombre del archivo; foto[1] es la etiqueta correspondiente
        csv_row = [foto[0],\
                   foto[1],\
                       ]
        try:
            im = Image.open('.\\gris_nuevo\\'+foto[0])
            text = test_RS(im, n, (160,80))
            text = re.sub( '[\W_]','', text)    
        except Exception as e:
            print(e)
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
    aciertos_x_option_2x1.append(sum(aciertos_foto_i)/6/358)

#%% size = 144 x 48
aciertos_x_option_3x1=[]
for n in range(6):
    aciertos_foto_i = []
    for foto in XY:
        # foto[0] es el nombre del archivo; foto[1] es la etiqueta correspondiente
        csv_row = [foto[0],\
                   foto[1],\
                       ]
        try:
            im = Image.open('.\\gris_nuevo\\'+foto[0])
            text = test_RS(im, n, (144,48))
            text = re.sub( '[\W_]','', text)    
        except Exception as e:
            print(e)
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
    aciertos_x_option_3x1.append(sum(aciertos_foto_i)/6/358)
    
#%% con super resolution
aciertos_x_option_3x1_SR=[]
for n in range(6):
    aciertos_foto_i = []
    for foto in XY:
        # foto[0] es el nombre del archivo; foto[1] es la etiqueta correspondiente
        csv_row = [foto[0],\
                   foto[1],\
                       ]
        try:
            im = Image.open('.\\gris_nuevo\\'+foto[0])
            im = sr_w_vdsr(im)
            text = test_RS(im, n, (144,48))
            text = re.sub( '[\W_]','', text)    
        except Exception as e:
            print(e)
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
    aciertos_x_option_3x1_SR.append(sum(aciertos_foto_i)/6/358)    
    
    
#%% size = 144 x 52
#%%timeit
aciertos_x_option_36x13=[]
for n in range(6):
    aciertos_foto_i = []
    for foto in XY:
        # foto[0] es el nombre del archivo; foto[1] es la etiqueta correspondiente
        csv_row = [foto[0],\
                   foto[1],\
                       ]
        try:
            im = Image.open('.\\gris_nuevo\\'+foto[0])
            text = test_RS(im, n, (144,52))
            text = re.sub( '[\W_]','', text)    
        except Exception as e:
            print(e)
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
    aciertos_x_option_36x13.append(sum(aciertos_foto_i)/6/358)
    
    
    
    
#%% quizás deba reworkear la métrica


def txt_match(txt0, txt1):
    score = 0
    L0 = [l for l in txt0]
    for letra in txt1:
        for n,letra2 in enumerate(L0):
            if letra == letra2:
                score += 1
                L0.pop(n)
                
                break
    return score



otro_aciertos_x_option_3x1=[]
for n in range(6):
    aciertos_foto_i = []
    for foto in XY:
        # foto[0] es el nombre del archivo; foto[1] es la etiqueta correspondiente
        csv_row = [foto[0],\
                   foto[1],\
                       ]
        try:
            im = Image.open('.\\gris_nuevo\\'+foto[0])
            text = test_RS(im, n, (144,48))
            text = re.sub( '[\W_]','', text)    
        except Exception as e:
            print(e)
        try:
            text = text[:6]
        except:
            pass
        
        m = txt_match(foto[1], text)
        aciertos_foto_i.append(m)
    otro_aciertos_x_option_3x1.append(sum(aciertos_foto_i)/6/358)

