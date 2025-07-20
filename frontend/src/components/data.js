export const krakowStops = [
    { id: 1, lat: 50.064701 , lng: 19.94501, name: "Main Square" },
    { id: 2, lat: 50.0615, lng: 19.937, name: "Wawel Castle" },
    { id: 3, lat: 50.0511, lng: 19.935, name: "Kazimierz District" },
    { id: 4, lat: 50.0514, lng: 19.937, name: "Old Synagogue" },
    { id: 5, lat: 50.0467, lng: 19.948, name: "Nowa Huta" },
    { id: 6, lat: 50.0708, lng: 19.920, name: "Planty Park" },
    { id: 7, lat: 50.0643, lng: 19.920, name: "University of Krakow" },
    { id: 8, lat: 50.0867, lng: 19.959, name: "Zakopane Bus Station" },
    // Add more stops as needed
  ];
  export const malopolskaRoutes = [
    { id: 'A1', stopIds: [1, 2, 3] },
    { id: 'A2', stopIds: [3, 4, 5] },
    { id: 'A3', stopIds: [1, 3, 5] },
    { id: 'B1', stopIds: [1, 4, 5, 6] },
    { id: 'B2', stopIds: [2, 3, 4, 7] },
    { id: 'C1', stopIds: [3, 7, 6, 8] },
    // Add more routes as needed
  ];
  
  export const routeColors = {
    'A1': 'red',
    'A2': 'blue',
    'A3': 'green',
    'B1': 'orange',
    'B2': 'purple',
    'C1': 'teal',
    // Assign colors to additional routes
  };
  
  export const schedule = [
    { routeId: 'A1', stopId: 1, times: ["08:00", "09:00", "10:00"] },
    { routeId: 'A1', stopId: 2, times: ["08:10", "09:10", "10:10"] },
    { routeId: 'A1', stopId: 3, times: ["08:20", "09:20", "10:20"] },
    { routeId: 'A2', stopId: 3, times: ["08:30", "09:30", "10:30"] },
    { routeId: 'A2', stopId: 4, times: ["08:40", "09:40", "10:40"] },
    { routeId: 'A2', stopId: 5, times: ["08:50", "09:50", "10:50"] },
    { routeId: 'A3', stopId: 1, times: ["09:00", "10:00", "11:00"] },
    { routeId: 'A3', stopId: 3, times: ["09:10", "10:10", "11:10"] },
    { routeId: 'A3', stopId: 5, times: ["09:20", "10:20", "11:20"] },
    { routeId: 'B1', stopId: 1, times: ["08:00", "09:00", "10:00"] },
    { routeId: 'B1', stopId: 4, times: ["08:20", "09:20", "10:20"] },
    { routeId: 'B1', stopId: 5, times: ["08:40", "09:40", "10:40"] },
    { routeId: 'B1', stopId: 6, times: ["08:50", "09:50", "10:50"] },
    { routeId: 'B2', stopId: 2, times: ["08:10", "09:10", "10:10"] },
    { routeId: 'B2', stopId: 3, times: ["08:30", "09:30", "10:30"] },
    { routeId: 'B2', stopId: 4, times: ["08:50", "09:50", "10:50"] },
    { routeId: 'B2', stopId: 7, times: ["09:00", "10:00", "11:00"] },
    { routeId: 'C1', stopId: 1, times: ["08:00", "09:00", "10:00"] },
    { routeId: 'C1', stopId: 2, times: ["08:20", "09:20", "10:20"] },
    { routeId: 'C1', stopId: 5, times: ["08:40", "09:40", "10:40"] },
    { routeId: 'C1', stopId: 8, times: ["09:00", "10:00", "11:00"] },
    // Add more schedule entries as needed
  ];
  