import React from "react";
import Card from "./Card";
import "../css/Card.css"
const CardSection = () => {
  const texts = [
    "Fill in the medicine dose one time and get daily reminders for taking medication.One time engagement and the tension and headache to remember doasge is gone.Enjoy your life and we will take care of your medication.",
    "Do you forget your doctors appointment.We are here to remind you.Add your appointments and get them at one place. Check the appoinments section to know daily schedule",
    "Worried about your health due to lack of sleep.We are here to provide an effortless sleep tracking via our webapp.Monitor your daily sleep statistics and make amends.Happy Sleeping ;).",
  ];
  const headings = [
    "Topic 1",
    "Topic 2",
    "Topic 3",
  ];
  return (
    <div className="main-content">
      <h1 className="content-header">Some Informations about farming</h1>
      <div className="cards">
        <Card id={1} text={texts[0]} topic={headings[0]}></Card>
        <Card id={2} text={texts[1]} topic={headings[1]}></Card>
        <Card id={3} text={texts[2]} topic={headings[2]}></Card>
      </div>
    </div>
  );
};

export default CardSection;