import logging
import os
import sys

def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """
    Configure un logger pour enregistrer les messages dans un fichier et la console.
    
    Parameters:
        name (str): Nom du logger.
        log_file (str): Chemin vers le fichier de log.
        level (int): Niveau de logging (par défaut : logging.INFO).

    Returns:
        logging.Logger: Logger configuré.
    """
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Formatteur pour le logger
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Handler pour fichier avec UTF-8
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Handler pour la console avec gestion d'encodage
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
