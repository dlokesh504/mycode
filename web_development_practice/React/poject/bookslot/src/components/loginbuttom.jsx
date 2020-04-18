import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.css";
import LoginForm from "../components/loginform";
import { Link } from "react-router-dom";

class Login extends Component {
  state = {};
  render() {
    return (
      <div>
        <Link to="/login" className="btn btn-danger btn-sm">
          Login
        </Link>
      </div>
    );
  }
}

export default Login;
