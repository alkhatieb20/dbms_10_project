# Project P01 AUP: Automatic Exam Generation

**Term Project - Introduction to Database Management Systems (Summer Term 2026)**
**Author:** Abdullah Alkhatieb (259697)
**Lecturer:** Stephan Bökelmann

## 📖 Project Overview
This repository contains the complete term project, including the database setup (PostgreSQL), REST API (FastAPI), and the frontend source code (Tkinter). The system is designed to automate the creation of exams, securely store questions, and automatically aggregate total points without calculation errors.

## 🎥 Presentation Video
[Click here to watch the presentation video (YouTube) - Unlisted](https://youtu.be/akVMgwjJSN0)

## 📦 Releases & Documentation
The final compiled documentation (`documentation.pdf`) and the frontend Debian installer (`exam-frontend_0.1.0_amd64.deb`) can be downloaded directly from the **[Releases](../../releases/latest)** page.

---

## 🚀 How to Run the Project (Deployment)

**1. Setup Environment Variables (Security):**
Before starting the containers, please create your own `.env` file based on the provided example. This ensures that sensitive credentials are not tracked by version control.

```bash
cp .env.example .env

(Please edit the new .env file to set your own custom API_KEY and database passwords).

2. Start the Backend:
Run the following command to build and start the PostgreSQL database and FastAPI containers:
Bash

docker compose up -d --build

3. Start the Frontend:

    Download and install the provided Debian package (.deb) from the Releases page.

    Open the application.

    When the Connection Dialog appears, enter http://localhost:8000 as the API URL.

    Enter the exact same API_KEY you defined in your .env file to authenticate successfully.
