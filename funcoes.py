import cv2
import matplotlib.pyplot as plt
import numpy as np


def carregar_imagem(caminho: str, cor="cinza") -> np.ndarray:
    """
    Carrega uma imagem a partir de um caminho especificado.

    Args:
        caminho (str): O caminho para a imagem.

    Returns:
        numpy.ndarray: A imagem carregada.
    """
    img = cv2.imread(caminho)

    if cor == "cinza":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif cor == "rgb":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img


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
