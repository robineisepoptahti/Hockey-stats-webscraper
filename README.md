# Hockey stat webscraper

Application can be found in Render: [https://hockey-stats-webscraper-frontend.onrender.com](https://hockey-stats-webscraper-frontend.onrender.com)

Webscraper with python3.11 backend and Typescript frontend.
Add player to the list who you want to follow, and it add the stats to SQLite database.
You can follow non-existent players, but they won't show up before they have statistics in either league with their name.

## Local usage

-Clone repo
-Install dependencies for backend from backend/requirements.txt, and make sure you have
Python version of at least 3.11

cd backend
pip3 install -r requirements.txt
python3 main.py

-Install frontend dependencies and run

cd frontend
npm install
npm run start

-Run app (from root src/main.py)

## Requirements

- Python3.11 or newer
- requirements.txt
