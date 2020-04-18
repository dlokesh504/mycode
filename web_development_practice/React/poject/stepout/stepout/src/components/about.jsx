import React, { Component } from "react";

class About extends Component {
  state = {};
  render() {
    return (
      <div>
        <br />
        <div className="row">
          <div className="col-3"></div>
          <div className="col-6">
            {" "}
            <div className="container" style={{ backgroundColor: "#283542 " }}>
              <h3 style={{ color: "white" }}>About this project</h3>
              <p style={{ color: "white" }}>
                It has been only three months since reports first emerged from
                China of an unknown virus causing unusual cases of pneumonia,
                and scientists and public health experts already know more about
                it and how it works than at the same point in earlier outbreaks.
                But there's still a lot they don't know. As the new coronavirus
                continues to spread around the world.
              </p>
              <br />
              <h3 style={{ color: "white" }}>
                Main casuse of spread coronavirus through out the worls is
                people does't aware of social distancing{" "}
              </h3>

              <p style={{ color: "white" }}>
                Due to lockdown Many people started purchasing basic goods in
                prior.. As much croud is being created at the basic need shops
                ,This creates problem while we are getting rid of this virus...
                To Avoid such problem this application makes people to step out
                at perfect and planned time..
              </p>
              <br />
              <h3 style={{ color: "white" }}>What we did</h3>
              <p style={{ color: "white" }}>
                We developed an Application medium between buyer and seller with
                web app (using mean stack) and mobile application (using android
                studio) By taking real scenario into consideration this
                aplication helps to book the general public to book there
                timings (slots) to go out for purchasing vegitable and general
                need items during coronavirus pandemic. and get back to home
                safely. as this helps to avoid huge public gathering at market
                places. so we hope it helps in social Distancing in this
                critical situations.
              </p>
            </div>
          </div>
          <div className="col-3"></div>
        </div>
      </div>
    );
  }
}

export default About;
