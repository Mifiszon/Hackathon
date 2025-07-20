import Logo from '../assets/Logo.png';
import homeBG from '../assets/home_bg2.svg';
import React from 'react';

const Navbar = () => {
  return (
    <nav 
      className="bg-white p-4" 
      style={{ 
        backgroundImage: `url(${homeBG})`, 
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center'
      }}
    >
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        <div className="">
          <img src={Logo} alt="Koleje Małopolskie" className="w-24 h-auto" />
        </div>
        <div className="hidden md:block flex-shrink-0">
          <a href="/" className="text-blue-950 font-bold text-xl">Koleje Małopolskie - Monitor Tras</a>
        </div>
        <div className="flex-shrink-0">
          <a href="/" className="text-blue-950 text-base mr-4 hover:text-blue-500">Kontakt</a>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
