# Project P01 AUP: Automatic Exam Generation

**Term Project - Introduction to Database Management Systems (Summer Term 2026)**
**Author:** Abdullah Alkhatieb (259697)
**Lecturer:** Stephan Bökelmann

## 📖 Project Overview
This repository contains the complete term project, including the database setup (PostgreSQL), REST API (FastAPI), and the frontend source code (Tkinter). The system is designed to automate the creation of exams, securely store questions, and automatically aggregate total points without calculation errors.

## 🎥 Presentation Video
[Click here to watch the presentation video (YouTube) - Unlisted](https://youtu.be/akVMgwjJSN0)

## 📦 Releases & Documentation
The final compiled documentation (`documentation.pdf`) and the frontend Debian installer (`exam-frontend_0.1.0_amd64.deb`) can be downloaded directly from the [**Releases**](../../releases/latest) page.

---

## 🚀 How to Run the Project (Deployment)

**1. Setup Environment Variables (Security):**
Before starting the containers, please create your own `.env` file based on the provided example.
\`\`\`bash
cp .env.example .env
\`\`\`

**2. Start the Backend:**
Run the following command:
\`\`\`bash
docker compose up -d --build
\`\`\`

**3. Start the Frontend:**
- Download the **.deb** file from Releases.
- Enter your API URL (http://localhost:8000) and your **API_KEY**.
