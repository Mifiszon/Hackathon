# Małopolskie Railways – Route Monitor

A web application that allows users to view Małopolskie Railways routes and stops on an interactive map.  
Users can select a specific railway line from a set of tiles and view its detailed stop schedule.

## Features

- **Interactive map** with all stops marked.
- **Line selection via tiles** – each railway line is displayed as a convenient tile.
- **Detailed stop schedules** available for every line.
- **Responsive design** – works seamlessly on both mobile and desktop devices.
- **User-friendly interface** with simple navigation.

## Technologies

- **React.js** – frontend framework
- **React Leaflet** – map handling
- **Tailwind CSS** – styling
- **JavaScript (ES6)** – application logic
- **OpenStreetMap** – map data provider

## Project Structure

- `src/components/Map.js` – map component displaying all stops.
- `src/components/Navbar.js` – application navigation bar.
- `src/data/stop.js` – dataset containing stops.
- `src/assets/` – graphic assets (logo, marker icons, background).

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/route-monitor.git
   Navigate to the project directory:
   cd route-monitor
   Install dependencies:
   npm install
   Run the application:
   npm start
   Open the app in your browser at:
   http://localhost:3000

## Future Development
- Real-time train position tracking.
- Route filtering by time and station.
- Delay notifications.
