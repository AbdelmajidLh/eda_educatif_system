from src.logger import setup_logger
from src.utils.functions import list_installed_packages, process_file

# Configurer le logger
logger = setup_logger("main_logger", log_file="output/project.log")

# Liste des fichiers CSV à analyser
csv_files = {
    "EdStatsCountry": "data/raw/EdStatsCountry.csv",
    "EdStatsCountry-Series": "data/raw/EdStatsCountry-Series.csv",
    "EdStatsData": "data/raw/EdStatsData.csv",
    "EdStatsFootNote": "data/raw/EdStatsFootNote.csv",
    "EdStatsSeries": "data/raw/EdStatsSeries.csv"
}

def main():
    logger.info("🚀 Démarrage de l'analyse des fichiers...")

    # Boucler sur chaque fichier CSV et traiter son analyse
    for file_name, file_path in csv_files.items():
        process_file(file_name, file_path)

    # Liste les versions des modules
    list_installed_packages()

    logger.info("🏁 Fin du programme.")

if __name__ == "__main__":
    main()
