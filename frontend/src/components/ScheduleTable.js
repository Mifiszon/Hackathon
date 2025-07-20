import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ScheduleTable = ({ routeId, setSelectedTripId }) => {
  const [schedule, setSchedule] = useState([]);
  const [currentPage, setCurrentPage] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const tripsResponse = await axios.get(`http://localhost:8000/api/trips/${routeId}`);
        const trips = tripsResponse.data;

        const scheduleData = await Promise.all(trips.map(async (trip) => {
          const stopsResponse = await axios.get(`http://localhost:8000/api/stops/${trip.trip_id}`);
          let stops = stopsResponse.data;

          stops.sort((a, b) => new Date(a.stop.arrival_time) - new Date(b.stop.arrival_time));

          const firstStopTime = stops.length > 0 ? stops[0].arrival_time : null;

          return {
            trip,
            stops,
            firstStopTime,
          };
        }));

        scheduleData.sort((a, b) => new Date(a.firstStopTime) - new Date(b.firstStopTime));

        setSchedule(scheduleData);
      } catch (error) {
        console.error('Błąd pobierania danych:', error);
      }
    };

    fetchData();
  }, [routeId]);

  const currentStops = schedule.length > 0 ? schedule[currentPage].stops : [];

  const handleNextPage = () => {
    setCurrentPage(prevPage => Math.min(prevPage + 1, schedule.length - 1)); 
  };

  const handlePrevPage = () => {
    setCurrentPage(prevPage => Math.max(prevPage - 1, 0)); 
  };

  return (
    <div id="skok" className="overflow-x-auto pb-4 w-full pt-4">
      <table className="w-full bg-white shadow-md rounded-lg overflow-hidden">
        <thead>
          <tr className="bg-[#385088] text-white">
            <th className="px-4 py-2">Trasa</th>
            <th className="px-4 py-2">Strefa</th>
            <th className="px-4 py-2">Przystanek</th>
            <th className="px-4 py-2">Przyjazd</th>
          </tr>
        </thead>
        <tbody>
          {currentStops.map((stop, index) => (
            <tr key={index} className={index % 2 === 0 ? "bg-gray-200" : "bg-gray-100"}
              onClick={() => setSelectedTripId(schedule[currentPage].trip.trip_id)}>
              <td className="px-4 py-2 text-center">{schedule[currentPage].trip.route.route_long_name}</td>
              <td className="px-4 py-2 text-center">{schedule[currentPage].trip.route.route_type}</td>
              <td className="px-4 py-2 text-center">{stop.stop.stop_name}</td>
              <td className="px-4 py-2 text-center">{stop.arrival_time}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="flex justify-center mt-4">
        <button
          onClick={handlePrevPage}
          className="bg-[#385088] text-white px-4 py-2 m-2 rounded"
          disabled={currentPage === 0}
        >
          Poprzednia
        </button>
        <button
          onClick={handleNextPage}
          className="bg-[#385088] text-white px-4 py-2 m-2 rounded"
          disabled={currentPage === schedule.length - 1}
        >
          Następna
        </button>
      </div>
    </div>
  );
};

export default ScheduleTable;
