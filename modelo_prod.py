# -*- coding: utf-8 -*-

from PIL import Image
import torch
import numpy as np



from vdsr.model import VDSR
from vdsr import config
from vdsr import imgproc


def sr_w_vdsr(im):
    """
    Parameters
    ----------
    im : .jpg
        Imagen para aplicar super resolution con modelo VDSR.

    Returns
    -------
    im2 : .jpg
        Imagen a la que se le ha aplicado SR.

    """
    # Cargar los pesos en la cpu
    model = VDSR().to(torch.device('cpu'))
    
    # 
    checkpoint = torch.load("vdsr\\vdsr.pth.tar",\
                            map_location=torch.device('cpu'))
    
    # cargo los pesos del modelo
    model.load_state_dict(checkpoint["state_dict"])
    
    # instancio al modelo para evaluar
    model.eval()
    
    # imagen a tensor
    lr_y_tensor = imgproc.image2tensor(im, range_norm=False, half=False)\
                                        .to(config.device).unsqueeze_(0)
    # evaluo el modelo con el tensor
    sr_y_tensor = model(lr_y_tensor).clamp_(0, 1.0)
    
    # 
    sr_y_image = imgproc.tensor2image(sr_y_tensor, range_norm=False, half=False)
    
    im2 = Image.fromarray(np.asarray(sr_y_image[0]))
    
    return im2
