# Portfolio Platform

A production-grade, containerized portfolio website designed with a "Minimalist Cozy" and "IDE-inspired" aesthetic. It features a decoupled architecture with a Vue.js frontend and a Django backend, fully optimized for serverless deployment on Google Cloud Run.

![Portfolio Preview](https://storage.googleapis.com/por7folio-media/projects/gallery/Screenshot_2026-01-01_at_16.00.57.png)

## 🚀 Tech Stack

- **Frontend:** Vue.js 3, TailwindCSS, Lucide Icons
- **Backend:** Django 5, Django REST Framework
- **Database:** PostgreSQL (Production), SQLite (Dev)
- **Infrastructure:** Docker, Nginx, Google Cloud Run
- **Storage:** Google Cloud Storage (Media), WhiteNoise (Static)

## ✨ Features

- **JSON-Terminal UI:** Content is presented as syntax-highlighted data structures.
- **Dynamic Content:** Fully manageable via the Django Admin interface.
- **Project Showcase:** Integrated carousel for project screenshots.
- **Persistent Media:** User uploads are securely stored in Google Cloud Storage.
- **Production Ready:** Nginx reverse proxy, security headers, and automated startup scripts.

## 🛠 Local Development

### Prerequisites
- Docker & Docker Compose
- *Or* Node.js & Python 3.12+

### Option 1: Docker (Recommended)
Running the entire stack with one command:

```bash
# 1. Clone the repo
git clone https://github.com/4yuub/por7folio.git
cd por7folio

# 2. Create .env file (copy from example)
cp backend/.env.example backend/.env

# 3. Start containers
docker-compose up --build
```
The site will be available at `http://localhost`.

### Option 2: Manual Setup

**Backend:**
```bash
cd backend
poetry install
python manage.py migrate
python manage.py runserver
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## ☁️ Deployment (Google Cloud Run)

This project is configured for continuous deployment to Cloud Run.

1.  **Build & Push Images:** images are built from `Dockerfile.backend` and `Dockerfile.frontend`.
2.  **Environment Variables:**
    - `GS_BUCKET_NAME`: Your GCS bucket name.
    - `DATABASE_URL`: Your PostgreSQL connection string.
    - `SECRET_KEY`, `DEBUG`: Django security settings.
3.  **Permissions:** The Cloud Run service account requires `Storage Object Admin` role.
