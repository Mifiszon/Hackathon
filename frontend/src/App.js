import React from 'react';
import PageHelmet from './components/PageHelmet';
import Navbar from './components/Navbar';
import Map from './components/IMap';
import CardSection from './components/CardSection';
import Details from './components/Details';



const App = () => {
  return (
    <div className="h-screen overflow-y-scroll overflow-x-hidden">
      <PageHelmet title="Koleje Małopolskie - Monitor Tras"/>
      <Navbar />
      <CardSection />
      <Map />
      <Details />
    </div>
  );
}

export default App;
