import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FormWindow = ({ onClose, formType, title }) => {
  const [location, setLocation] = useState('');
  const [time, setTime] = useState('');
  const [date, setDate] = useState('');
  const [suggestions, setSuggestions] = useState([]);
  const [destination, setDestination] = useState('');
  const [allStops, setAllStops] = useState([]);

  useEffect(() => {
    if (formType === 'szybkie-polaczenie-form') {
      navigator.geolocation.getCurrentPosition((position) => {
        const { latitude, longitude } = position.coords;
        setLocation(`Lat: ${latitude}, Lon: ${longitude}`);
      });

      const currentTime = new Date().toLocaleTimeString('pl-PL', {
        hour: '2-digit',
        minute: '2-digit',
      });
      setTime(currentTime);

      const currentDate = new Date().toISOString().split('T')[0];
      setDate(currentDate);
    }
  }, [formType]);

  useEffect(() => {
    const fetchStops = async () => {
      try {
        const response = await axios.get("http://localhost:8000/api/stops/");
        setAllStops(response.data);
      } catch (error) {
        console.error("Error fetching stops:", error);
      }
    };

    fetchStops();
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission
  };

  const handleDestinationChange = (e) => {
    const value = e.target.value;
    setDestination(value);
    fetchSuggestions(value);
  };

  const fetchSuggestions = (query) => {
    if (query.length > 0) {
      const filteredStops = allStops.filter(stop =>
        stop.stop_name.toLowerCase().includes(query.toLowerCase())
      );
      setSuggestions(filteredStops);
    } else {
      setSuggestions([]);
    }
  };

  return (
    <div className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex justify-center items-center z-50">
      <div className="bg-white p-6 rounded shadow-lg w-10/12">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-bold">{title}</h2>
          <button onClick={onClose} className="bg-transparent text-black font-semibold text-xl leading-none outline-none focus:outline-none">
            <span>×</span>
          </button>
        </div>
        {formType === 'szybkie-polaczenie-form' && (
          <form onSubmit={handleSubmit}>
            <div className="mb-4">
              <label htmlFor="skad" className="block text-gray-700 font-bold mb-2">Skąd:</label>
              <input
                type="text"
                id="skad"
                name="skad"
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                placeholder="Wpisz skąd"
                value={location}
                readOnly
                required
              />
            </div>
            <div className="mb-4">
              <label htmlFor="dokad" className="block text-gray-700 font-bold mb-2">Dokąd:</label>
              <input
                type="text"
                id="dokad"
                name="dokad"
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                placeholder="Wpisz dokąd"
                value={destination}
                onChange={handleDestinationChange}
                required
              />
              {suggestions.length > 0 && (
                <ul className="border rounded bg-white mt-2">
                  {suggestions.map((suggestion, index) => (
                    <li
                      key={index}
                      className="px-4 py-2 cursor-pointer hover:bg-gray-200"
                      onClick={() => {
                        setDestination(suggestion.stop_name);
                        setSuggestions([]);
                      }}
                    >
                      {suggestion.stop_name}
                    </li>
                  ))}
                </ul>
              )}
            </div>
            <div className="mb-4">
              <label htmlFor="data" className="block text-gray-700 font-bold mb-2">Data:</label>
              <input
                type="date"
                id="data"
                name="data"
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                value={date}
                readOnly
                required
              />
            </div>
            <div className="mb-4">
              <label htmlFor="godzina" className="block text-gray-700 font-bold mb-2">Godzina:</label>
              <input
                type="time"
                id="godzina"
                name="godzina"
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                value={time}
                readOnly
                required
              />
            </div>
            <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Szukaj</button>
          </form>
        )}
        {formType === 'zaplanuj-podroz-form' && (
          <form onSubmit={handleSubmit}>
            <div className="mb-4">
              <label htmlFor="skad" className="block text-gray-700 font-bold mb-2">Skąd:</label>
              <input
                type="text"
                id="skad"
                name="skad"
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                placeholder="Wpisz skąd"
                required
              />
            </div>
            <div className="mb-4">
              <label htmlFor="dokad" className="block text-gray-700 font-bold mb-2">Dokąd:</label>
              <input
                type="text"
                id="dokad"
                name="dokad"
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                placeholder="Wpisz dokąd"
                required
              />
            </div>
            <div className="mb-4">
              <label htmlFor="data" className="block text-gray-700 font-bold mb-2">Data:</label>
              <input
                type="date"
                id="data"
                name="data"
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                required
              />
            </div>
            <div className="mb-4">
              <label htmlFor="godzina" className="block text-gray-700 font-bold mb-2">Godzina:</label>
              <input
                type="time"
                id="godzina"
                name="godzina"
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                required
              />
            </div>
            <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Szukaj</button>
          </form>
        )}
        {formType === 'sprawdz-rozklad-form' && (
          <div className="mb-4">
            {/* Add form content for 'sprawdz-rozklad-form' */}
          </div>
        )}
      </div>
    </div>
  );
};

export default FormWindow;
