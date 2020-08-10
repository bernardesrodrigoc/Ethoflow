"""
See readme for information about this file.
Ethoflow: computer vision and artificial intelligence-based software for automatic behavior analysis
v 1.0

DOI: 10.1101/2020.07.23.218255
LicenseCC BY-NC-ND 4.0

@developer: Rodrigo Cupertino Bernardes
https://www.researchgate.net/profile/Rodrigo_Cupertino_Bernardes
"""

import cv2

def Coordenada (I):
    
    XY=list()
    
    
    escala = min(700./I.shape[0], 700./I.shape[1]) 
    largura_window = int(I.shape[1] * escala)
    altura_window = int(I.shape[0] * escala)
    cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Original', largura_window, altura_window)
    cv2.imshow('Original', I)
    
    def direito_down(evento, x, y, flags, params):
    #
        if evento == 2:
             XY.append([x, y]) 
        
    cv2.setMouseCallback('Original', direito_down)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return XY
