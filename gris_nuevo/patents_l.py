# -*- coding: utf-8 -*-
import glob
import os

def get_labels():
    """
    Returns
    -------
    XY : list
        Devuelve un listado de tuplas, (nombre, label).

    """
    path = os.getcwd() + '\\gris_nuevo\\'
    
    labels = ['DSJG68','DLPR50','HTWJ80','RJCF13','DA5356','RDJD22','SG7143'\
             ,'KCSX21','KY2648','CHWD88','BWHD81','','TE9520','KBFY84'\
             ,'PRLH45','SD3076'
              ]
    XY = list()    
    
    # lee las imagenes que tienen el nombre que coincida 
    file_list = glob.glob(path+'P9_20220623-Noche_lectura ideal_*') 
    
    # ordena las imagenes segun el número de serie que poseen
    list.sort(file_list, key=lambda x:\
              int(x.split('gris_nuevo\\')[1].strip('P9_20220623')\
                  .strip('-Noche_lectura').strip(' ideal_').strip('.jpg')))
    
    # rellena la lista con una tupla que contiene el nombre y
    # el label correspondiente
    for foto in file_list:
        XY.append((foto.split('gris_nuevo\\')[1], labels[0]))
    
    file_list = glob.glob(path+'P9_20220623-Noche_Lluvia_*')
    list.sort(file_list, key=lambda x:\
              int(x.split('gris_nuevo\\')[1].strip('P9_20220623')\
                              .strip('-Noche_Lluvia_').strip('.jpg')))
    for foto in file_list:
        XY.append((foto.split('gris_nuevo\\')[1], labels[1]))
    
    file_list = glob.glob(path+'P11_20220623_Noche_lectura Ideal_*')
    list.sort(file_list, key=lambda x:\
              int(x.split('gris_nuevo\\')[1].strip('P11_20220623_Noche_lectura')\
                  .strip(' Ideal_').strip('.jpg')))
    n=1
    for foto in file_list:
        if n<=5:
            XY.append((foto.split('gris_nuevo\\')[1], labels[2]))
            n += 1
        elif n<=36:
            XY.append((foto.split('gris_nuevo\\')[1], labels[3]))
            n += 1
        else:
            XY.append((foto.split('gris_nuevo\\')[1], labels[4]))
            n += 1
    
    file_list = glob.glob(path+'P11_20220624_Noche_ingreso 2da fila_*')
    list.sort(file_list, key=lambda x:\
              int(x.split('gris_nuevo\\')[1].strip('P11_20220624_Noche_ingreso')\
                  .strip(' 2da').strip(' fila_').strip('.jpg')))
    n=1
    for foto in file_list:
        if n<=70:
            XY.append((foto.split('gris_nuevo\\')[1], labels[5] ))
            n += 1
        else: 
            XY.append((foto.split('gris_nuevo\\')[1], labels[6] ))
            n += 1        
    
    file_list = glob.glob(path+'P11_20220624_Noche_ppu otro lugar_*')
    list.sort(file_list, key=lambda x:\
              int(x.split('gris_nuevo\\')[1].strip('P11_20220624_Noche_ppu')\
                   .strip(' otro').strip(' lugar_').strip('.jpg')))
        
    for foto in file_list:
            XY.append((foto.split('gris_nuevo\\')[1], labels[7] ))
    
    file_list = glob.glob(path+'P122_20220623_Noche_ ppu no visible_*')
    list.sort(file_list, key=lambda x:\
              int(x.split('gris_nuevo\\')[1].strip('P122_20220623_Noche_')\
                  .strip(' ppu').strip(' no').strip(' visible_').strip('.jpg')))
    for foto in file_list:
        XY.append((foto.split('gris_nuevo\\')[1], labels[8]))
    
    file_list = glob.glob(path+'P122_20220623_Noche_Lluvia_*')
    list.sort(file_list, key=lambda x:\
              int(x.split('gris_nuevo\\')[1].strip('P122_20220623_')\
                  .strip('Noche_Lluvia_').strip('.jpg')))
    n=1
    for foto in file_list:
        if n<=17:
            XY.append((foto.split('gris_nuevo\\')[1], labels[9] ))
            n += 1
        else: 
            XY.append((foto.split('gris_nuevo\\')[1], labels[10] ))
            n += 1  
    
    file_list = glob.glob(path+'P122_20220623_Noche_Luces_*')
    list.sort(file_list, key=lambda x:\
              int(x.split('gris_nuevo\\')[1].strip('P122_20220623_Noche_Luces_')\
                  .strip('.jpg')))
    XY.append((file_list[0].split('gris_nuevo\\')[1], labels[11] ))
    
    file_list = glob.glob(path+'P122_20220623_Noche_Noche_Lectura ideal_*')
    list.sort(file_list, key=lambda x:\
              int(x.split('gris_nuevo\\')[1].strip('P122_20220623_Noche')\
                  .strip('_Noche_Lectura').strip(' ideal_').strip('.jpg')))
    n=1
    for foto in file_list:
        if n<=17:
            XY.append((foto.split('gris_nuevo\\')[1], labels[12] ))
            n += 1
        elif n<=22: 
            XY.append((foto.split('gris_nuevo\\')[1], labels[13] ))
            n += 1
    
    file_list = glob.glob(path+'P122_20220623_Noche_ppu otro lugar_*')
    list.sort(file_list, key=lambda x:\
              int(x.split('gris_nuevo\\')[1].strip('P122_20220623_Noche_ppu')\
                  .strip(' otro').strip(' lugar_').strip('.jpg')))
    n=1
    for foto in file_list:
        if n<=1:
            XY.append((foto.split('gris_nuevo\\')[1], labels[14] ))
            n += 1
        else: 
            XY.append((foto.split('gris_nuevo\\')[1], labels[15] ))
            n += 1
    
    return XY

