import React from "react";

const Card = ({ id, topic, text }) => {
  const getClassName = () => {
    return "card c" + id;
  };
  return (
    <div className={getClassName()}>
      <div className="card__heading">
        <h3>{topic}</h3>
      </div>
      <p>{text}</p>
    </div>
  );
};

export default Card;
