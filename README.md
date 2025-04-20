A full-stack server monitoring dashboard that provides real-time metrics such as CPU usage, memory consumption, and disk activity. Built with React.js, FastAPI, and PostgreSQL, and deployed on Render.

🚀 Live Frontend:  https://server-monitorimng-dashboard-app.onrender.com/
🌐 Live Backend: https://server-monitorimng-dashboard-1.onrender.com/

📸 Screenshots
Dashboard View

![pikudon](https://github.com/user-attachments/assets/bfa2f495-1824-4895-bd45-b4f71eb17503)

Prerequisites
Python 3.9+
Node.js 16+ & npm
PostgreSQL 13+

🧪 Backend

cd server-monitoring-dashboard/backend


python3 -m venv .venv
source .venv/scripts/activate        

pip install --upgrade pip
pip install -r requirements.txt

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

💻 3. Frontend

cd server-monitoring-dashboard/frontend

npm install

npm start
