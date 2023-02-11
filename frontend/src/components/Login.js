import React from "react";
import "../css/Login.css";
function login() {
  return (
    <div className="login">
      {/* <div className="login_box"> */}
      <div className="left">
        <div className="contact">
          <form action="">
            <h3>SIGN IN</h3>
            <input type="text" placeholder="EMAIL" />
            <input type="text" placeholder="PASSWORD" />
            <button className="submit">LET'S GO</button>
          </form>
        </div>
      </div>
      <div className="right">
        <div className="contact">
          <form action="">
            <h3>SIGN UP</h3>
            <input type="text" placeholder="EMAIL" />
            <input type="text" placeholder="PASSWORD" />
            <button className="submit">LET'S GO</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default login;
