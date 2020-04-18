import React, { Component } from "react";

class LoginForm extends Component {
  handleSubmit = e => {
    e.PreventDefault();

    const Username = this.username.value;

    console.log("Submitted sucesfully", Username);
  };

  render() {
    return (
      <div>
        <h1>LoginForm</h1>
        <form onSubmit={this.handleSubmit}>
          <div className="from-group">
            <lable htmlFor="username"> Username</lable>
            <input
              ref={this.username}
              autoFocus
              id="username"
              type="text"
              className="form-control"
            />
          </div>
        </form>
        <form action="">
          <div className="from-group">
            <lable htmlFor="password"> Password</lable>
            <input id="password" type="text" className="form-control" />
          </div>
          <button className="btn btn-primary m-1">Login</button>
        </form>
      </div>
    );
  }
}

export default LoginForm;
