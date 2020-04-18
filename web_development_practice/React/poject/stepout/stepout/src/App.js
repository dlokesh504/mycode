import React from "react";
import "./App.css";
import Main from "./components/main";
import Navbar from "./components/navbar";
import Login from "./components/login";
import Reg from "./components/reg";
import { Component } from "react";
import { Route } from "react-router-dom";
import About from "./components/about";

class App extends Component {
  state = {
    ac: { home: 0, login: 0, reg: 0 }
  };
  render() {
    return (
      <div ClassName="App">
        <Navbar></Navbar>
        <Route path="/" exact component={Main}></Route>
        <Route path="/login" exact component={Login}></Route>
        <Route path="/reg" exact component={Reg}></Route>
        <Route path="/aboutus" exact component={About}></Route>
      </div>
    );
  }
}

export default App;
