import cv2 as cv

def procurarVermelho(img):
    linhas, colunas, canais = img.shape
    for linha in range(linhas):
        for coluna in range(colunas):
            pixel = img[linha, coluna]

            if pixel[0] == 0 and pixel[1] and pixel[2] == 255:
                print(linha, coluna)
                return

print("Sem vermelho")

img = cv.imread("robot.jpg")
procurarVermelho(img)    