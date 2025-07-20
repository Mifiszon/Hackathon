import React from 'react';
import Card from './Card';
import trainImage from '../assets/train.jpg';

const CardSection = () => {
  const cards = [
    {
      id: 'szybkie-polaczenie',
      title: 'Szybkie Połączenie',
      description: 'Natychmiastowe Wyznaczanie Trasy',
      form: 'szybkie-polaczenie-form',
    },
    {
      id: 'zaplanuj-podroz',
      title: 'Zaplanuj Podróż',
      description: 'Spersonalizowane Planowanie',
      form: 'zaplanuj-podroz-form',
    },
    {
      id: 'sprawdz-rozklad',
      title: 'Sprawdź Rozkład',
      description: 'Pełen Rozkład Jazdy',
      form: 'sprawdz-rozklad-form',
    },
  ];

  return (
    <nav
      className="bg-neutral-200 p-4"
      style={{
        backgroundImage: `url(${trainImage})`,
        backgroundPosition: 'center 10%',
        backgroundSize: 'cover',
        borderTop: '1px solid black',
        borderBottom: '1px solid black',
      }}
    >
      <div>
        <div className="w-full bg-cover bg-center flex items-center justify-center">
          <div className="flex flex-wrap justify-center">
            {cards.map((card, index) => (
              <div key={card.id} className="mx-12">
                <Card
                  id={card.id}
                  title={card.title}
                  description={card.description}
                  form={card.form}
                  index={index}
                />
              </div>
            ))}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default CardSection;
