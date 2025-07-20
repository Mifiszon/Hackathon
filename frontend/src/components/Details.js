import React, { useState, useEffect } from 'react';
import axios from 'axios';
import bgImage from '../assets/home_bg2.svg';
import ScheduleTable from './ScheduleTable';
import Map from './IMap'

const Details = () => {
  const [routes, setRoutes] = useState([]);
  const [selectedRoute, setSelectedRoute] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/routes/');
        setRoutes(response.data);
      } catch (error) {
        console.error('Błąd pobierania danych:', error);
      }
    };

    fetchData();
  }, []);

  const handleTileClick = (routeId) => {
    setSelectedRoute(routeId);
  };

  return (
    <div id="details" style={{ backgroundImage: `url(${bgImage})`, backgroundSize: 'cover', backgroundPosition: 'center', minHeight: '100vh', borderTop: '1px solid black' }}>
      <div className="flex flex-col items-center justify-center">
        <h1 className="text-black p-4 text-4xl font-bold mb-8">Szczegóły Tras</h1>
        <div className="grid grid-cols-5 md:grid-cols-11 gap-4">
          {routes.map(route => (
            <a key={route.route_id} href={`#skok`} className="m-2 p-2 bg-white border border-black font-bold text-blue-900 rounded-md transition-colors hover:bg-gray-300" onClick={() => handleTileClick(route.route_id)}>
              <p className="text-center">{route.route_short_name}</p>
            </a>
          ))}
        </div>
        {selectedRoute && (
          <>
            <ScheduleTable routeId={selectedRoute} />
            <Map routeId={selectedRoute} />
          </>
        )}
      </div>
    </div>
  );
};

export default Details;
