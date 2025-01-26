import logging
import os

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
    # Crée le répertoire pour les logs s'il n'existe pas
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Configure le logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Formatteur pour les logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Handler pour le fichier
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Handler pour la console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Ajout des handlers au logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
