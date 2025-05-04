import logo from "./logo.svg";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import React from "react";

const App = () => {
  return (
    <div className="container mt-5">
      <h1 className="text-primary">Hello Bootstrap + React!</h1>
      <button className="btn btn-success">Click Me</button>
    </div>
  );
};

export default App;
