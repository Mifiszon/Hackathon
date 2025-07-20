# Małopolskie Railways – Route Monitor

A web application that displays train routes and stops of Małopolskie Railways on an interactive map.  
The system consists of a **React.js frontend** and a **Python backend**, all containerized with **Docker**.

## Features

- **Interactive map** with marked stops.
- **Line selection via tiles** – each railway line is available as a separate tile.
- **Detailed timetable** for each line with its stops and route.
- **Python backend** with REST API serving train line and stop data.
- **Dockerized setup** – easy deployment and development environment.
- **Responsive design** – optimized for both mobile and desktop devices.

## Tech Stack

- **Frontend:** React.js, React Leaflet, Tailwind CSS, JavaScript
- **Backend:** Python, REST API
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose

## Project Structure

- `frontend/src/components/Map.js` – map component with all stops.
- `frontend/src/components/Navbar.js` – navigation bar.
- `frontend/src/data/stop.js` – stop data definitions.
- `backend/app/` – backend logic and API endpoints.
- `docker-compose.yml` – Docker Compose setup for both frontend and backend.

## Installation & Running

Clone the repository and start the application using Docker Compose:

```bash
   git clone https://github.com/your-repo/route-monitor.git
   cd route-monitor
   docker-compose up --build
```

## The application will be available at:

Frontend: http://localhost:3000

Backend API: http://localhost:8000


## Future Plans
- Real-time train position tracking.
- Filtering routes by time and stations.
- Delay notifications.

## Authors
Developed as part of a web technology learning project – Małopolskie Railways – Route Monitor.
