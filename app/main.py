from loguru import logger
from src.data_loader import load_data
from src.eda import eda
from src.model import predict, train_model, show_pdp_analysis
from src.utils import setup_logging


def main():
    logger.info("Démarrage de l'application")
    setup_logging()  # Configurer les logs
    logger.debug("Démarrage de l'application en mode debug")
    
    # Charger les données
    df = load_data()

    # Initialiser la variable model
    model = None
    scaler = None
    label_encoder = None

    # Navigation
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Choisissez une section", ["EDA", "Entraînement du Modèle", "Prédiction", "Analyse des Interactions"])

    if choice == "EDA":
        eda(df)
    elif choice == "Entraînement du Modèle":
        model, scaler, label_encoder = train_model(df)
    elif choice == "Prédiction":
        if model is None:  # Vérifie si le modèle a déjà été entraîné
            model, scaler, label_encoder = train_model(df)
        predict(model, scaler, label_encoder)
    elif choice == "Analyse des Interactions":
        if model is None:  # Vérifie si le modèle est entraîné
            model, scaler, label_encoder = train_model(df)
        # Vérifie que le modèle est bien entraîné avant d'afficher les PDP
        if model is not None:
            show_pdp_analysis(model, df.drop(columns=["y"]), df.columns)

    logger.info("Application terminée")

if __name__ == "__main__":
    import streamlit as st
    main()
