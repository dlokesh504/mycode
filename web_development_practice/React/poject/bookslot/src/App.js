import React from "react";
import "./App.css";
import { Route } from "react-router-dom";
import LoginForm from "./components/loginform";
import Navbar from "./components/Navbar";
import Home from "./components/Home";

function App() {
  return (
    <div>
      <Navbar></Navbar>
      <div className="content container">
        <Route path="/" exact component={Home}></Route>

        <Route path="/login" exact component={LoginForm}></Route>
      </div>
    </div>
  );
}

export default App;
