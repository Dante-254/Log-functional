import logo from "./logo.svg";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import React from "react";
import Alert from "./Alert.tsx";
import Button from "./Button.tsx";
import { useState } from "react";

const App = () => {
  const [alertVisible, setAlertVisibility] = useState(false);
  return (
    <div>
      {alertVisible && (
        <Alert onClose={() => setAlertVisibility(false)}>
          <h1>Hello World</h1>
        </Alert>
      )}
      <Button onClick={() => setAlertVisibility(true)}>
        <h3>Log In</h3>
      </Button>
    </div>
  );
};

export default App;
