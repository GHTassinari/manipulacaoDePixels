# O código primeiro declara as imagens, e mantém uma versão que não vai ser modificada.
# Depois, eu defino as funções para modificar as imagens, uma para cada efeito.
# Depois, faço uma função que exibe lado a lado, com o a variável da imagem modificada
# e o título.
# Por fim, uma função de execução, que roda todas elas, com um array que em mapa
# que mantém a imagem modificada, e o título.
# Ele mostra cada imagem modificada lado a lado com a original,
# Depois, salva as imagens modificadas no resultado
# O objetivo é que caso eu queria adicionar mais efeitos, eu apenas adiciono no map, 
# e mais uma variável de imagem para ser modificado.

import os
import cv2
import matplotlib.pyplot as plt

os.makedirs("resultados", exist_ok=True)

imagemInicial = cv2.imread('imagens/ponte.jpg')
imagemXadrez = cv2.imread('imagens/ponte.jpg')
imagemVerde = cv2.imread('imagens/ponte.jpg')
imagemDegrade = cv2.imread('imagens/ponte.jpg')

def funcaoXadrez():
   for y in range(0, imagemXadrez.shape[0], 10):
       for x in range(0, imagemXadrez.shape[1], 10):
           if ((y//10) + (x//10)) % 2 == 0:
               imagemXadrez[y:y+3, x:x+3] = (0,255,255)
           else:
               imagemXadrez[y:y+3, x:x+3] = (0,0,0)

def funcaoVerde():
   imagemVerde[:,:,0] = 0
   imagemVerde[:,:,2] = 0

def funcaoDegrade():
    altura, largura = imagemDegrade.shape[:2]
    for y in range(altura):
        for x in range(largura):
            intensidade = int((x / largura) * 255)
            fator_degrade = (intensidade, 255 - intensidade, 0)
            
            imagemDegrade[y, x] = (
                int(imagemDegrade[y, x][0] * fator_degrade[0] / 255),
                int(imagemDegrade[y, x][1] * fator_degrade[1] / 255), 
                int(imagemDegrade[y, x][2] * fator_degrade[2] / 255)
            )

def exibir_lado_a_lado(imagemModificada, titulo):
   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
   
   ax1.imshow(cv2.cvtColor(imagemModificada, cv2.COLOR_BGR2RGB))
   ax1.set_title(titulo)
   ax1.axis("off")
   
   ax2.imshow(cv2.cvtColor(imagemInicial, cv2.COLOR_BGR2RGB))
   ax2.set_title("Imagem original")
   ax2.axis("off")
   
   plt.tight_layout()
   plt.show()

def executar():
   funcaoXadrez()
   funcaoVerde()
   funcaoDegrade()
   
   modificacoes = [
       (imagemXadrez, "Imagem com padrão xadrez"),
       (imagemVerde, "Tons de verde"),
       (imagemDegrade, "Imagem degradê")
   ]
   
   for imagem, titulo in modificacoes:
       exibir_lado_a_lado(imagem, titulo)

executar()

cv2.imwrite("resultados/saidaXadrez.jpg", imagemXadrez)
cv2.imwrite("resultados/saidaVerde.jpg", imagemVerde)
cv2.imwrite("resultados/saidaDegrade.jpg", imagemDegrade)
print("Imagens salvas na pasta resultados/")