import os
import pkg_resources
from src.logger import setup_logger
from src.data_loader import DataLoader
from src.missing_values import MissingValuesHandler

# Configurer le logger
logger = setup_logger("utils_logger", log_file="output/project.log")

def list_installed_packages():
    """
    Liste les versions des modules installés utilisés dans le projet.
    """
    logger.info("📌 [INFO] Versions des modules utilisés :")
    packages = ["pandas", "seaborn", "matplotlib"]
    for package in packages:
        try:
            version = pkg_resources.get_distribution(package).version
            logger.info(f"[INFO] {package} : {version}")
        except pkg_resources.DistributionNotFound:
            logger.warning(f"[WARNING] {package} non installé.")

def process_file(file_name: str, file_path: str):
    """
    Traite un fichier CSV : chargement, analyse des valeurs manquantes, et génération de heatmap.

    Parameters:
        file_name (str): Nom court du fichier (sans l'extension).
        file_path (str): Chemin du fichier CSV.
    """
    logger.info(f"[INFO] Début du traitement de : {file_name}")

    # Vérifier si le fichier existe avant de le charger
    if not os.path.exists(file_path):
        logger.error(f"[ERROR] Fichier non trouvé : {file_path}")
        return

    # Charger les données
    loader = DataLoader(file_path=file_path)
    try:
        df = loader.load_data()
        logger.info(f"[INFO] Données chargées avec succès pour {file_name}. Aperçu :\n{df.head()}")
    except Exception as e:
        logger.error(f"[ERROR] Erreur lors du chargement de {file_name} : {e}")
        return

    # Définir les chemins de sortie pour chaque fichier
    missing_values_csv = f"output/{file_name}_missing_values.csv"
    heatmap_path = f"output/{file_name}_missing_values_heatmap.png"

    # Analyser les valeurs manquantes
    handler = MissingValuesHandler(save_path=missing_values_csv)
    try:
        missing_report = handler.analyze(df, heatmap_path=heatmap_path)
        logger.info(f"[INFO] Rapport des valeurs manquantes pour {file_name} :\n{missing_report}")
    except Exception as e:
        logger.error(f"[ERROR] Erreur lors de l'analyse des valeurs manquantes de {file_name} : {e}")
        return

    logger.info(f"[INFO] Fin du traitement pour {file_name}.\n")
