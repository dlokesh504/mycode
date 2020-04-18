import React, { Component } from "react";
import { Link } from "react-router-dom";

class Navbar extends Component {
  state = {};
  render() {
    return (
      <div>
        <Link to="/" className="btn  btn-outline-secondary m-2  btn-sm">
          Home
        </Link>
        <Link to="/login" className="btn btn-outline-info btn-sm">
          Login
        </Link>
      </div>
    );
  }
}

export default Navbar;
