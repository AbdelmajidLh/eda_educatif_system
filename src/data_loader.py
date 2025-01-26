import pandas as pd
from src.logger import setup_logger

logger = setup_logger(__name__, log_file="output/project.log")

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        """
        Charge les données depuis un fichier CSV.
        
        Returns:
            pd.DataFrame: Le DataFrame chargé.
        """
        try:
            logger.info(f"Chargement des données depuis {self.file_path}")
            df = pd.read_csv(self.file_path)
            logger.info(f"Données chargées avec succès : {len(df)} lignes, {len(df.columns)} colonnes")
            return df
        except FileNotFoundError:
            logger.error(f"Fichier non trouvé : {self.file_path}")
            raise
        except Exception as e:
            logger.error(f"Erreur lors du chargement des données : {e}")
            raise
