import pandas as pd
from src.logger import setup_logger

logger = setup_logger(__name__)

class ExploratoryDataAnalysis:
    @staticmethod
    def describe_data(df: pd.DataFrame):
        """Affiche les informations générales du DataFrame."""
        try:
            logger.info("Affichage des informations générales sur les données.")
            print(df.info())
            print(df.describe())
        except Exception as e:
            logger.error(f"Erreur lors de l'analyse exploratoire : {e}")
            raise
