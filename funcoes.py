import cv2
import matplotlib.pyplot as plt
import numpy as np


def carregar_imagem_rgb(caminho: str) -> np.ndarray:
    """
    Carrega uma imagem a partir de um caminho especificado.

    Args:
        caminho (str): O caminho para a imagem.

    Returns:
        numpy.ndarray: A imagem carregada.
    """
    img = cv2.imread(caminho)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img_rgb


def exibir_imagem(imagem: np.ndarray, titulo: str = "Imagem") -> None:
    """
    Exibe uma imagem usando matplotlib.

    Args:
        imagem (numpy.ndarray): A imagem a ser exibida.
        titulo (str): O título da janela de exibição.
    """
    plt.imshow(imagem)
    plt.title(titulo)
    plt.axis('off')
