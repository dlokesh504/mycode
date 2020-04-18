import React, { Component } from "react";
import log1 from "../assets/social_11.jpeg";
//import log2 from "../assets/so_2.jpg";
import log3 from "../assets/social_1.jpg";
import log4 from "../assets/final.jpg";
import wmap from "../assets/time.jpg";
import wmap1 from "../assets/map1.jpg";
import { Link } from "react-router-dom";

class Main extends Component {
  state = {};
  render() {
    return (
      <div className="content">
        <div
          id="carouselExampleIndicators"
          class="carousel slide"
          data-ride="carousel"
          data-interval="1500"
        >
          <ol class="carousel-indicators">
            <li
              data-target="#carouselExampleIndicators"
              data-slide-to="0"
              class="active"
            ></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
          </ol>
          <div class="carousel-inner">
            <div class="carousel-item active  ">
              <img class="d-block w-100" src={log1} alt="First slide" />
            </div>
            <div class="carousel-item">
              <img class="d-block w-100" src={log3} alt="Second slide" />
            </div>
            <div class="carousel-item">
              <img class="d-block w-100" src={log4} alt="Third slide" />
            </div>
          </div>
          <a
            class="carousel-control-prev"
            href="#carouselExampleIndicators"
            role="button"
            data-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a
            class="carousel-control-next"
            href="#carouselExampleIndicators"
            role="button"
            data-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>

        {/* //end of carouselExampleIndicators  */}

        <div
          class="card mb-3  "
          style={{ border: "1px solid black", margin: "0" }}
        >
          <div className="row no-gutters">
            <div className="col-md-2">
              <img
                src={wmap}
                class="card-img"
                alt="..."
                width={20}
                height={350}
              />
            </div>

            <div className="col-md-4" style={{ marginTop: "200" }}>
              <br />
              <br></br>
              <div class="list-type2" style={{ height: " 10" }}>
                <h3
                  style={{
                    color: "dark",
                    bold: "true",
                    fontFamily: "jockerman"
                  }}
                >
                  How it works
                </h3>
                <ol>
                  <li>
                    <a href="#">Register</a>
                  </li>
                  <li>
                    <a href="#">Book your slot</a>
                  </li>
                  <li>
                    <a href="#">get verified Your id </a>
                  </li>
                  <li>
                    <a href="#">Do your shoping</a>
                  </li>
                  <li>
                    <a href="#">Return to home in time </a>
                  </li>
                </ol>
              </div>
              {/* <small class="text-muted">Last updated 3 mins ago</small> */}
            </div>
            <div className="col-md-6" style={{ marginRight: "0" }}>
              <br />
              <br />
              <div class="card text-white bg-dark mb-2">
                <div class="card-header">
                  The importance of social distancing during a pandemic
                </div>
                <div class="card-body">
                  <h5 class="card-title">
                    Why Experts Are Urging Social Distancing to Combat
                    Coronavirus Outbreak
                  </h5>
                  <p class="card-text">
                    As cities and towns across the United States confront the
                    growing number of COVID-19 cases, epidemiologists say we are
                    now in the mitigation phase of the outbreak. The virus is
                    already in our communities, so the focus now is to mitigate,
                    or reduce, the damage from the disease.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* card with img background */}

        <div
          style={{ border: "1px solid black", margin: "0" }}
          className="card bg-dark text-white"
        >
          <img src={wmap1} class="card-img" alt="..." height={350} />

          <div className="card-img-overlay">
            <h5 className="card-title">Be responsable and save the World</h5>
            <p className="card-text red">
              Keep calm and carry on." "The only thing we have to fear is fear
              itself." "Don't worry, be happy{" "}
            </p>
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            {/* <p className="card-text">Last updated 3 mins ago</p> */}
          </div>
        </div>

        {/* fotter */}

        <footer className="site-footer">
          <div className="container">
            <div className="row">
              <div className="col-sm-12 col-md-6">
                <h6>About</h6>
                <p className="text-justify">About this aplication !</p>
                <p>
                  this aplication helps to book the general public to book there
                  timings (slots) to go out for purchasing vegitable and general
                  need items during coronavirus pandemic. and get back to home
                  safely. as this helps to avoid huge public gathering at market
                  places.
                  <br />
                  so we hope it helps in social Distancing in this critical
                  situations.
                </p>
              </div>

              <div classNameName="col-xs-6 col-md-3">
                <h6>Categories</h6>
                <ul classNameName="footer-links">
                  <li>
                    <Link to="/reg">Register</Link>
                  </li>
                  <li>
                    <Link to="/login">Login</Link>
                  </li>
                  <li>
                    <Link to="/aboutus">About Us</Link>
                  </li>
                </ul>
              </div>

              <div classNameName="col-xs-6 col-md-3">
                <h6>Quick Links</h6>
                <ul classNameName="footer-links">
                  <li>
                    <a href="/">copyrights</a>
                  </li>
                </ul>
              </div>
            </div>
            <hr />
          </div>
          <div className="container">
            <div className="row">
              <div className="col-md-8 col-sm-6 col-xs-12">
                <p className="copyright-text">
                  Copyright &copy; 2020 All Rights Reserved by
                  <a href="#"> Thunders</a>.
                </p>
              </div>
            </div>
          </div>
        </footer>
      </div>
    );
  }
}

export default Main;
