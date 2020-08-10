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

for i in range(1,725):
    img = cv2.imread("non_trofalax/1 (" + str(i) +")" + ".png")
    img2 = cv2.resize(img, (124, 124))

    cv2.imwrite("non_trofalax_pad1/" + str(i) + ".jpeg",img2)
print('\a')
