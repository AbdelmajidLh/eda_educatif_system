import pandas as pd
from src.logger import setup_logger

logger = setup_logger(__name__)

class ColumnSelector:
    def __init__(self, columns: list):
        self.columns = columns

    def select(self, df: pd.DataFrame) -> pd.DataFrame:
        """Sélectionne des colonnes spécifiques."""
        try:
            logger.info(f"Sélection des colonnes : {self.columns}")
            return df[self.columns]
        except Exception as e:
            logger.error(f"Erreur lors de la sélection des colonnes : {e}")
            raise
