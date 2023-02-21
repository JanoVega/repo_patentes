# -*- coding: utf-8 -*-
from PIL import Image

import pytesseract

from modelo_prod import sr_w_vdsr
#%% modularizacion

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



def test_RS(im, option, size):
    """ Para testear Resampling / size
    """
    assert type(size) == tuple, 'size debe ser una tupla '
    assert type(option) == int, 'option debe ser un entero'
    assert option >=0 and option <6 ,'option debe estar entre 0 y 5'
    
    alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"# *-°
    options = "-c tessedit_char_whitelist={}".format(alphanumeric)
    options +=" --psm "+str(10)
    
    im_proc = im.resize(size, Image.Resampling(option))
    
    return pytesseract.image_to_string(im_proc, config = options )


def test_Opt_Sr(im, psm, sr):
    """ Para testear Resampling / size
    """
    assert type(sr) == bool, 'sr es un valor boleano'
    assert type(psm) == int, 'option debe ser un entero'
    assert psm >=0 and psm <14 ,'option debe estar entre 0 y 5'
    
    alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"# *-°
    options = "-c tessedit_char_whitelist={}".format(alphanumeric)
    options +=" --psm "+str(psm)
    
    if sr == True:
        im = sr_w_vdsr(im)
    im_proc = im.resize((144,48), Image.Resampling(3))
    
    return pytesseract.image_to_string(im_proc, config = options )


def test_sin_preproc(im, psm):
    alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"# *-°
    options = "-c tessedit_char_whitelist={}".format(alphanumeric)
    options +=" --psm "+str(psm)
    return pytesseract.image_to_string(im, config = options )
    
# # =============================================================================
# 
# 
# alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
# options = "-c tessedit_char_whitelist={}".format(alphanumeric)
# options +=" --psm "+str(10)
# 
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# 
# im3=im2.resize((160,80), Image.Resampling.LANCZOS)
# im3
# 
# pytesseract.image_to_string(im3, config = options )
# 
# im4=im2.resize((160,80), Image.Resampling.BILINEAR)
# im4
#  
# pytesseract.image_to_string(im4, config = options )
# 
# 
# im5 =  Image.fromarray( ((np.asarray(im3)/2+np.asarray(im4)/2)).astype('uint8'))
# im5
# 
# pytesseract.image_to_string(im5, config = options )
# 
# im6=im2.resize((160,80), Image.Resampling.NEAREST)
# im6
# 
# im9=im2.resize((120,40), Image.Resampling(0))
# print('\n'+pytesseract.image_to_string(im9, config = options ))
# im9
# 
# =============================================================================