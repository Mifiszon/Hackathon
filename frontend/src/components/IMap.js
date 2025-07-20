import React, { useState, useEffect } from "react";
import { MapContainer, TileLayer, Marker, Popup, Polyline } from "react-leaflet";
import L from "leaflet";
import axios from "axios";
import "leaflet/dist/leaflet.css";
import MarkIcon from '../assets/Mark.png'; 

const Map = () => {
  const [krakowStops, setKrakowStops] = useState([]);

  const bounds = [
    [49.002, 19.243],
    [50.505, 21.053],
  ];
  
  const markIcon = L.icon({
    iconUrl: MarkIcon,
    iconSize: [32, 32],
    iconAnchor: [16, 32],
    popupAnchor: [0, -32],
  });

  useEffect(() => {
    const fetchStops = async () => {
      try {
        const response = await axios.get("http://localhost:8000/api/stops/");
        // Przekształcamy dane do oczekiwanego formatu
        const formattedStops = response.data.map(stop => ({
          id: stop.stop_id,
          lat: stop.stop_lat,
          lng: stop.stop_lon,
          stop_name: stop.stop_name
        }));
        setKrakowStops(formattedStops);
      } catch (error) {
        console.error("Error fetching stops:", error);
      }
    };

    fetchStops();
  }, []);

  const renderKrakowStops = () => {
    return krakowStops.map((stop) => (
      <Marker key={stop.id} position={[stop.lat, stop.lng]} icon={markIcon}>
        <Popup>
          {stop.stop_name}
        </Popup>
      </Marker>
    ));
  };


  return (  
    <div className="relative overflow-hidden z-40">
      <div className="flex flex-col h-screen">
        <MapContainer
          center={[50.0615, 19.937]}
          zoom={9}
          minZoom={9}
          maxZoom={14}
          maxBounds={bounds}
          maxBoundsViscosity={1.0}
          className="flex-grow"
          scrollWheelZoom={false}
          scrollWheelZoomControl={false}
        >
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          />
          {renderKrakowStops()}
        </MapContainer>
      </div>
    </div>
  );
};

export default Map;
