import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from src.logger import setup_logger

logger = setup_logger(__name__, log_file="output/project.log")

class MissingValuesHandler:
    def __init__(self, save_path: str = None):
        """
        Initialise le gestionnaire de valeurs manquantes.
        
        Parameters:
            save_path (str): Chemin pour sauvegarder les résultats (optionnel).
        """
        self.save_path = save_path

    def analyze(self, df: pd.DataFrame, heatmap_path: str = None) -> pd.DataFrame:
        """
        Analyse les valeurs manquantes dans un DataFrame et génère une heatmap.

        Parameters:
            df (pd.DataFrame): Le DataFrame à analyser.
            heatmap_path (str): Chemin pour sauvegarder la heatmap (optionnel).

        Returns:
            pd.DataFrame: DataFrame contenant le nombre et le pourcentage de valeurs manquantes.
        """
        try:
            logger.info("Analyse des valeurs manquantes commencée.")
            
            # Calcul des valeurs manquantes
            missing_counts = df.isnull().sum()
            total_rows = len(df)
            missing_percentages = (missing_counts / total_rows) * 100

            # Créer le DataFrame des résultats
            missing_data = pd.DataFrame({
                "Colonnes": df.columns,
                "Nombre de valeurs manquantes": missing_counts,
                "Pourcentage de valeurs manquantes (%)": missing_percentages
            }).reset_index(drop=True)

            # Sauvegarder les résultats si nécessaire
            if self.save_path:
                missing_data.to_csv(self.save_path, index=False)
                logger.info(f"Résultats des valeurs manquantes sauvegardés dans : {self.save_path}")

            # Générer une heatmap si un chemin est fourni
            if heatmap_path:
                self._generate_heatmap(df, heatmap_path)

            logger.info("Analyse des valeurs manquantes terminée.")
            return missing_data

        except Exception as e:
            logger.error(f"Erreur lors de l'analyse des valeurs manquantes : {e}")
            raise

    def _generate_heatmap(self, df: pd.DataFrame, heatmap_path: str):
        """
        Génère une heatmap des valeurs manquantes et la sauvegarde dans un fichier.

        Parameters:
            df (pd.DataFrame): Le DataFrame à analyser.
            heatmap_path (str): Chemin pour sauvegarder la heatmap.
        """
        try:
            logger.info(f"Génération de la heatmap des valeurs manquantes dans : {heatmap_path}")
            
            plt.figure(figsize=(10, 8))
            sns.heatmap(df.isnull(), cbar=False, cmap="viridis", yticklabels=False)
            plt.title("Heatmap des valeurs manquantes")
            plt.savefig(heatmap_path)
            plt.close()

            logger.info(f"Heatmap sauvegardée dans : {heatmap_path}")
        except Exception as e:
            logger.error(f"Erreur lors de la génération de la heatmap : {e}")
            raise
