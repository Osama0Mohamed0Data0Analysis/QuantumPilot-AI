# QuantumPilot AI

**AI Orchestration Platform for Quantum Computing**  
*NeuralUCB-Based Autonomous Decision Engine for Adaptive Quantum Execution*

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Next.js](https://img.shields.io/badge/Next.js-14-black)](https://nextjs.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)](https://www.docker.com/)

> **Production-ready research platform** that acts as an intelligent autopilot for IBM Quantum — from circuit submission to cost-optimized execution with continuous learning.

---

## 🚀 Live Demo

- **Frontend (Vercel)**: https://quantum-pilot-ai.vercel.app/
- **API Docs**: [https://quantumpilot-ai.vercel.app/api/v1/docs](https://quantumpilot-ai.vercel.app/api/v1/docs)
- **GitHub Repo**: [https://github.com/ahmedzogly/QuantumPilot-AI](https://github.com/ahmedzogly/QuantumPilot-AI)

---

## 📸 Screenshots

### Real IBM Quantum Execution
![Real Execution Success](assets/screenshots/Screenshot%202026-07-31%20181427.png)
![Job Monitor - Completed](assets/screenshots/Screenshot%202026-07-31%20181422.png)
![Execution Results](assets/screenshots/Screenshot%202026-07-31%20181455.png)

### Main Dashboard & Circuit Input
![Main Dashboard](assets/screenshots/Screenshot%202026-07-31%20181416.png)
![Circuit Input + Real Execute](assets/screenshots/Screenshot%202026-07-31%20181407.png)

### Analytics, Charts & Cost Dashboard
![Quantum Backends + Decision Engine](assets/screenshots/Screenshot%202026-07-31%20181416.png)
![T1 Drift + Space Weather Correlation](assets/screenshots/Screenshot%202026-07-31%20181407.png)
![Mitigation Factory Comparison](assets/screenshots/Screenshot%202026-07-31%20181427.png)
![Cost Dashboard & 76% Savings](assets/screenshots/Screenshot%202026-07-18%20192419.png)

---

## ✨ Key Features

- **Full Lifecycle Management**: Circuit input (QASM 3.0 / Qiskit) → Q-LEAR Analysis → NeuralUCB Decision → Real IBM Execution → Monitoring → Learning
- **NeuralUCB Decision Engine**: 22-dimensional context (calibration + space weather) → 72 arms → multi-objective optimization
- **Advanced Mitigation**: S-ZNE (1.2× overhead = **76% saving** vs traditional 5× ZNE)
- **Live Space Weather Integration**: NOAA Kp-index + Oulu neutron flux
- **Real IBM Quantum Execution**: Direct `QiskitRuntimeService` integration
- **Professional Bilingual UI** (Arabic + English)
- **Production Ready**: Docker (6 services), Vercel, CI/CD, Clean DDD Architecture

---

## 🏗️ Architecture

```
Circuit (QASM/Qiskit) 
  → Circuit Analyzer (Q-LEAR)
  → Backend Repository (Live IBM + 8M drift)
  → SpaceWeatherService (NOAA + Oulu)
  → NeuralUCB (22-D context)
  → Mitigation Factory (S-ZNE, ZNE, PEC...)
  → QiskitRuntimeService (Real Execution)
  → Job Monitor + Cost Dashboard
  → Reward → Learning Engine
```

**Tech Stack**:
- Backend: FastAPI + Qiskit + Mitiq + PyTorch
- Frontend: Next.js + Recharts + Bilingual
- Infra: Docker Compose (Postgres, Redis, RabbitMQ, Celery), Vercel

---

## 📚 References & Resources

All external resources used in this project are documented in:

→ **[docs/REFERENCES.md](docs/REFERENCES.md)**

### Quick Highlights

**Key GitHub Repos**:
- [S-ZNE Surrogates](https://github.com/weiyouLiao/Sample-efficient-quantum-error-mitigation-via-classical-learning-surrogates)
- [Mitiq](https://github.com/unitaryfund/mitiq)
- [QDataSet](https://github.com/eperrier/QDataSet)

**Major Datasets**:
- [Qiskit Calibration Drift (8M rows)](https://huggingface.co/datasets/phanerozoic/qiskit-calibration-drift)
- [NVIDIA QCalEval](https://huggingface.co/datasets/nvidia/QCalEval)

**Key Papers**:
- S-ZNE (arXiv:2511.07092)
- QNTK-UCB, NNAS, RL QEC (Google/Nature 2026), and more

**External APIs**:
- [NOAA Kp-index](https://services.swpc.noaa.gov/json/planetary_k_index_1m.json)
- [IBM Quantum](https://quantum.cloud.ibm.com/)
- [Hugging Face Granite-8B](https://huggingface.co/Qiskit/granite-8b-qiskit)

---

## 🛠️ Quick Start (Docker - Recommended)

```bash
git clone https://github.com/ahmedzogly/QuantumPilot-AI.git
cd QuantumPilot-AI

cp .env.example .env
# Edit .env and add your IBM_TOKEN + IBM_CRN

docker-compose -f docker-compose.prod.yml up --build
```

- Backend: http://localhost:8000/docs
- Frontend: http://localhost:3000

---

## 🔑 Required Environment Variables

```env
IBM_TOKEN=your_ibm_cloud_api_key
IBM_CRN=your_crn_here
```

---

## 📖 Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [API Reference](docs/API.md)
- [Error Mitigation](docs/ERROR_MITIGATION.md)
- [NeuralUCB](docs/NEURALUCB.md)
- [Deployment](DEPLOYMENT.md)
- [Full References](docs/REFERENCES.md)

---

## 📊 Research Highlights

- **76% cost saving** with S-ZNE (1.2× vs 5×)
- First platform integrating **live space weather** with qubit calibration
- NeuralUCB trained on **8,847 real contexts** from 8M+ IBM records
- Full bilingual professional interface

---

## 📄 License

Apache 2.0 — see [LICENSE](LICENSE)

---

**Built for the quantum computing research community.**

If you use this platform in your research, please cite the repository and the referenced papers.
