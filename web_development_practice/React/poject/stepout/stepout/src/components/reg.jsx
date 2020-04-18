import React, { Component } from "react";

class Reg extends Component {
  state = {};
  render() {
    return (
      <div className="container-fluid">
        <div className="row">
          <div className="col-3"></div>
          <div className="col-5">
            <br />
            <div
              className="card text-white bg-dark mb-4 sm"
              style={{ width: "50", padding: "20" }}
            >
              <div
                class="card-header"
                style={{ textAlign: "center", textSizeAdjust: "20px" }}
              >
                User Registration
              </div>
              <div class="card-body">
                <h5 class="card-title">Fill out Your Details</h5>

                <form>
                  <div className="form-group">
                    <label for="exampleInputEmail1">Name</label>
                    <input
                      type="email"
                      class="form-control"
                      id="exampleInputEmail1"
                      aria-describedby="emailHelp"
                    />
                    <small id="emailHelp" class="form-text text-muted">
                      We'll never share your email with anyone else.
                    </small>
                    <label for="exampleInputEmail1">Mobile Number</label>
                    <input
                      type="email"
                      class="form-control"
                      id="exampleInputEmail1"
                      aria-describedby="emailHelp"
                    />
                    <label for="exampleInputEmail1">Email address</label>
                    <input
                      type="email"
                      class="form-control"
                      id="exampleInputEmail1"
                      aria-describedby="emailHelp"
                    />
                  </div>
                  <div className="form-group">
                    <label for="exampleInputPassword1">Password</label>
                    <input
                      type="password"
                      class="form-control"
                      id="exampleInputPassword1"
                    />
                  </div>
                  <label for="exampleInputEmail1">Ration card no</label>
                  <input
                    type="text"
                    class="form-control"
                    id="exampleInputEmail1"
                    aria-describedby="emailHelp"
                  />
                  <label for="exampleInputEmail1">Address</label>
                  <input
                    type="text"
                    class="form-control"
                    id="exampleInputEmail1"
                    aria-describedby="emailHelp"
                  />
                  <div className="form-group form-check"></div>
                  <button type="submit" class="btn btn-primary">
                    Register
                  </button>
                </form>
              </div>
            </div>
          </div>
          <div className="col-3"></div>
        </div>
        <br />
      </div>
    );
  }
}

export default Reg;
