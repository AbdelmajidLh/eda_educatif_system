from src.logger import setup_logger
from src.data_loader import DataLoader
from src.missing_values import MissingValuesHandler
import pkg_resources

# Configurer le logger
logger = setup_logger("main_logger", log_file="output/project.log")

def list_installed_packages():
    """
    Liste les versions des modules installés utilisés dans le projet.
    """
    logger.info("Versions des modules utilisés dans le projet :")
    packages = ["pandas", "seaborn", "matplotlib"]
    for package in packages:
        try:
            version = pkg_resources.get_distribution(package).version
            logger.info(f"{package} : {version}")
        except pkg_resources.DistributionNotFound:
            logger.warning(f"{package} n'est pas installé.")

def main():
    # Fichier CSV à charger
    csv_file = "data/raw/example.csv"
    missing_values_csv = "output/missing_values_report.csv"
    heatmap_path = "output/missing_values_heatmap.png"

    # Vérification du fichier de données
    logger.info("Démarrage du programme...")

    # Charger les données
    loader = DataLoader(file_path=csv_file)
    try:
        df = loader.load_data()
        logger.info(f"Voici un aperçu des données :\n{df.head()}")
    except Exception as e:
        logger.error(f"Erreur lors du chargement des données : {e}")
        return

    # Analyser les valeurs manquantes
    handler = MissingValuesHandler(save_path=missing_values_csv)
    try:
        missing_report = handler.analyze(df, heatmap_path=heatmap_path)
        logger.info(f"Rapport des valeurs manquantes :\n{missing_report}")
    except Exception as e:
        logger.error(f"Erreur lors de l'analyse des valeurs manquantes : {e}")
        return

    # Liste les versions des modules
    list_installed_packages()

    logger.info("Fin du programme.")

if __name__ == "__main__":
    main()
