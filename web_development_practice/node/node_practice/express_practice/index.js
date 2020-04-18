const config = require("config");
const Joi = require("joi");
const login = require("./logger");
const helmet = require("helmet");
const startupdebugger = require("debug")("app:startup");
const dbdebugger = require("debug")("app:db");
const morgan = require("morgan");
const ex = require("express");
const coursesr = require("./routes/courses");
const home = require("./routes/home");
const app = ex();

app.set("view engine", "pug");

//configuration
console.log("Application NAme : " + config.get("name"));
console.log("mail server :" + config.get("mail.host"));

console.log("mail pass :" + config.get("mail.password"));

console.log(`NODE_ENV :${process.env.NODE_ENV}`);

if (app.get("env") === "development") {
  app.use(morgan("tiny"));
  startupdebugger("morgon enabled"); // to see this set DEBUG= app:startup
}
// db work
dbdebugger("connected to db........"); // to see this set DEBUG= app:db
app.use(ex.json());
app.use(helmet());
app.use(morgan("tiny"));
app.use("/api/courses", coursesr);
app.use("/", home);

app.use(ex.urlencoded({ extended: true }));
app.use(ex.static("public"));
app.use(login);

app.use(function (req, res, next) {
  console.log("authenticating....");
  next();
});

/// get exapmle

//port
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`listening on port ${port}......`);
});

function validateCourse(course) {
  const schema = {
    name: Joi.string().min(3).required(),
  };
  return Joi.validate(course, schema);
}
