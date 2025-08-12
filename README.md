# IMS — Inventory Management System  
_Django + PostgreSQL + Redis + Celery (Dockerized with Gunicorn)_

A compact inventory app that lets you manage **Products** and **Categories** and automatically sends a **low-stock alert** when quantities drop below a threshold. It’s built to be easy to run locally via Docker and to showcase common backend skills for interviews.

---

## ✨ Features
- **Products & Categories** with Django Admin CRUD
- **Low-stock email alerts** using **Celery + Redis** (threshold configurable)
- **Docker Compose** stack: `web` (Gunicorn), `db` (Postgres), `redis`, `worker` (Celery), `beat`
- Env-driven settings via `python-decouple`
- Minimal, readable codebase you can extend (dashboard, APIs, etc.)

---

## 🧱 Tech Stack
- **Backend:** Python 3.x, Django 5.x
- **Queue:** Celery 5.x with Redis 7
- **DB:** PostgreSQL 14
- **Server:** Gunicorn
- **Config:** docker-compose, `.env`

---

## ⚡ Quick Start (Docker)

**Prereqs:** Docker Desktop (or Docker + compose plugin)

1. **Clone & configure**
   ```bash
   git clone https://github.com/Ridhimaa7/IMS.git
   cd IMS
   cp .env.example .env
   # edit .env if needed
