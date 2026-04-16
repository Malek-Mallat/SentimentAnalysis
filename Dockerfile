# Utiliser une image Python officielle légère
FROM python:3.12-slim

# Permet d'afficher les logs Python en temps réel dans Google Cloud
ENV PYTHONUNBUFFERED True

# Définir le dossier de travail
WORKDIR /app

# Copier les requirements en premier (optimisation Docker)
COPY requirements.txt .

# ⚠️ LA CORRECTION EST ICI : on met à jour pip d'abord, puis on installe
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copier le reste du code (app.py, modèles, templates, etc.)
COPY . .

# Exposer le port par défaut de Cloud Run
EXPOSE 8080

# Lancer l'application avec Gunicorn (Serveur de production)
# On suppose que votre fichier s'appelle app.py et que votre variable Flask s'appelle app
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "--timeout", "0", "app:app"]