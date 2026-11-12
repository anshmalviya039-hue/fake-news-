# 🔍 AI-Powered Fake News Detection & Evidence Verification System

A multilingual fake news detection platform combining classical ML, transformer models (FakeBERT, XLM-RoBERTa, MuRIL), explainable AI (SHAP/LIME), and evidence retrieval — built with FastAPI, React, and PyTorch.

---

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [API Documentation](#api-documentation)
- [Training Models](#training-models)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- **Multilingual Detection** — English and Hindi fake news classification
- **Multi-Model Analysis** — Classical ML (LogReg, RF, XGBoost) + Transformers (FakeBERT, XLM-RoBERTa, MuRIL)
- **Explainable AI** — SHAP and LIME explanations for every prediction
- **Evidence Retrieval** — Automated fact-check evidence from Google Fact Check API
- **Linguistic Analysis** — 15+ linguistic features (readability, sentiment, POS distribution, etc.)
- **Modern UI** — React + Tailwind CSS dashboard with confidence gauges, charts, and history
- **RESTful API** — FastAPI with auto-generated OpenAPI docs

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    React Frontend                        │
│  ┌──────────┐ ┌──────────┐ ┌─────────┐ ┌────────────┐  │
│  │ Analyze  │ │ Results  │ │ History │ │   Models   │  │
│  │  Page    │ │   Page   │ │  Page   │ │    Page    │  │
│  └──────────┘ └──────────┘ └─────────┘ └────────────┘  │
└─────────────────────┬───────────────────────────────────┘
                      │ HTTP/REST
┌─────────────────────▼───────────────────────────────────┐
│                   FastAPI Backend                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │              Analysis Pipeline                    │   │
│  │  ┌───────────┐  ┌────────────┐  ┌─────────────┐ │   │
│  │  │Linguistic │  │ Classifiers│  │ Transformers│ │   │
│  │  │ Features  │  │ (ML)       │  │ (DL)        │ │   │
│  │  └───────────┘  └────────────┘  └─────────────┘ │   │
│  │  ┌───────────┐  ┌────────────┐                   │   │
│  │  │ Evidence  │  │   XAI      │                   │   │
│  │  │ Retrieval │  │ SHAP/LIME  │                   │   │
│  │  └───────────┘  └────────────┘                   │   │
│  └──────────────────────────────────────────────────┘   │
│                         │                                │
│                    SQLite / PostgreSQL                    │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 18, Vite, Tailwind CSS, Recharts, React Router |
| **Backend** | FastAPI, Uvicorn, SQLAlchemy, Pydantic, Alembic |
| **ML/DL** | PyTorch, Transformers (HuggingFace), XGBoost, Scikit-learn |
| **XAI** | SHAP, LIME |
| **Database** | SQLite (dev) / PostgreSQL (prod) |
| **DevOps** | Docker, Docker Compose, GitHub Actions |

---

## 📁 Project Structure

```
fake-news/
├── backend/
│   ├── app/
│   │   ├── api/              # FastAPI route handlers
│   │   ├── models/           # SQLAlchemy ORM models
│   │   ├── schemas/          # Pydantic request/response schemas
│   │   ├── services/         # Business logic layer
│   │   ├── ml/               # ML pipeline
│   │   │   ├── classifiers/  # Classical ML models
│   │   │   ├── transformers/ # Transformer inference wrappers
│   │   │   ├── linguistic/   # Feature extraction
│   │   │   ├── evidence/     # Fact-check API integration
│   │   │   └── explainability/ # SHAP + LIME
│   │   ├── main.py           # FastAPI app entry point
│   │   └── config.py         # Application settings
│   ├── tests/                # Pytest test suite
│   ├── alembic/              # Database migrations
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/            # Page-level components
│   │   ├── services/         # API client
│   │   └── App.jsx
│   └── package.json
├── data/
│   ├── raw/                  # Original datasets
│   └── processed/            # Cleaned & split datasets
├── notebooks/                # Colab training notebooks
├── models/                   # Saved model checkpoints
├── docker-compose.yml
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Git

### 1. Clone & Setup

```bash
git clone <repo-url>
cd fake-news
```

### 2. Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

Backend runs at `http://localhost:8000`. API docs at `http://localhost:8000/docs`.

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`.

### 4. Docker (Alternative)

```bash
docker-compose up --build
```

---

## 📡 API Documentation

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/analyze` | Submit text/URL for analysis |
| `GET` | `/api/articles` | List all analyzed articles |
| `GET` | `/api/articles/{id}` | Get article details |
| `GET` | `/api/history` | Paginated analysis history |
| `GET` | `/api/models` | Available models & metadata |
| `GET` | `/api/evidence/{id}` | Evidence for a prediction |
| `GET` | `/api/health` | System health check |

Full interactive docs: `http://localhost:8000/docs` (Swagger UI)

---

## 🧠 Training Models

Model training is performed in Google Colab notebooks (GPU required):

1. `notebooks/01_data_preparation.ipynb` — Download & prepare datasets
2. `notebooks/02_classical_ml.ipynb` — Train classical ML models
3. `notebooks/03_fakebert_training.ipynb` — Fine-tune FakeBERT
4. `notebooks/04_xlm_roberta_training.ipynb` — Fine-tune XLM-RoBERTa
5. `notebooks/05_muril_hindi.ipynb` — Fine-tune MuRIL for Hindi
6. `notebooks/06_ensemble_fusion.ipynb` — Build ensemble/fusion model
7. `notebooks/07_evaluation.ipynb` — Full evaluation suite

After training, download model checkpoints to the `models/` directory.

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## 📚 References

- Based on research published in *Procedia Computer Science* (2025)
- Datasets: ISOT, X-FACT, AVeriTeC
- Models: FakeBERT, XLM-RoBERTa, MuRIL (Google)
