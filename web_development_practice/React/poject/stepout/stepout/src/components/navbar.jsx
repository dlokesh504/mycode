import React, { Component } from "react";
import { Link } from "react-router-dom";

class Navbar extends Component {
  state = {};
  render() {
    return (
      <div style={{ position: "sticky", position: "-webkit-sticky" }}>
        <nav className="navbar navbar-expand-lg navbar-light bg-light navbar navbar-dark bg-dark sticky">
          <a className="navbar-brand" href="/">
            StepOut
          </a>
          <button
            class="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="''/"
            aria-controls="navbarNavAltMarkup"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div className="navbar-nav">
              <Link className="nav-item nav-link " to="/">
                Home <span className="sr-only">(current)</span>
              </Link>
              <Link className="nav-item nav-link " to="/login">
                Login
              </Link>
              <Link className="nav-item nav-link" to="/reg">
                Register
              </Link>
              <Link className="nav-item nav-link " to="/aboutus">
                AboutUs
              </Link>
            </div>
          </div>
        </nav>
      </div>
    );
  }
}

export default Navbar;
