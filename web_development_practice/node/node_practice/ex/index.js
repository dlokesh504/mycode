const Joi = require("joi");
const mongoose = require("mongoose");
const express = require("express");
const app = express();
const genres = require("./routes/genres");
const cust = require("./routes/cust");
const users = require("./routes/users");
const auth = require("./routes/auth");
const config = require("config");

if (!config.get("jwtprivatekey")) {
  console.error("FATAL ERROR:jwtprivatekey is not defined.");
  process.exit(1);
}

mongoose
  .connect("mongodb://localhost/vidly")
  .catch()
  .then(() => {
    console.log("connected to mongodb...");
  })
  .catch((err) => {
    console.log("couldnot connect to db", err.message);
  });

app.use(express.json());
app.use("/api/genres", genres);
app.use("/api/cutomers", cust);
app.use("/api/users", users);
app.use("/api/auth", auth);
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening on port ${port}...`));
