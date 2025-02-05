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

    frameTonsCinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    frameContornos = cv.Canny(frameTonsCinza, 100, 200)
    
    cv.imshow('Captured Image', frame)
    cv.imshow('Captured Image', frameTonsCinza)
    cv.imshow('Captured Image', frameContornos)
    

    if cv.waitKey(1) == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()


