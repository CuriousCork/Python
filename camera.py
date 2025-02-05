'''
    Programador.......: (C) 2025 Diogo Ramiro
    Data..............: 05/02/2025
    Observações.......: Primeiro Exemplo em OpenCv
'''

import cv2 as cv

webcam = cv.VideoCapture(0)

if not webcam.isOpened():
    print('Startup Error!')
    exit()

while True:
    retorno, frame = webcam.read()

    if not retorno:
        print('Erro na captura')
        break

    cv.imshow('Captured Image', frame)

    if cv.waitKey(1) == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()


