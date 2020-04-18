const express = require("express");
const router = express.Router();

const courses = [
  { id: 1, name: "course1" },
  { id: 2, name: "course2" },
  { id: 3, name: "course3" },
  { id: 4, name: "course4" },
];

//post example
router.post("/", (req, res) => {
  const result = validateCourse(req.body);

  if (result.error) {
    res.status(400).send(result.error.details[0].message);
    return;
  }
  const course = {
    id: courses.length + 1,
    name: req.body.name,
  };
  courses.push(course);
  res.send(course);
});

// update example
router.put("/:id", (req, res) => {
  var course = courses.find((c) => c.id === parseInt(req.params.id));
  if (!course) {
    res.status(404).send("course not found with given id");

    return;
  }

  //validate
  //if invalid , return 400 - bad request

  const result = validateCourse(req.body);
  if (result.error) {
    res.status(400).send(result.error.details[0].message);
    return;
  }

  //update course
  course.name = req.body.name;
  res.send(course);
});

//delete example
router.delete("/:id", (req, res) => {
  //look up course
  // not existing , return 404
  var course = courses.find((c) => c.id === parseInt(req.params.id));
  if (!course) res.status(404).send("course not found with given id");

  // delete
  const index = courses.indexOf(course);
  courses.splice(index, 1);

  //return the same course
  res.send(course);
});

//get
router.get("/", (req, res) => {
  res.send(courses);
});

//  /api/courses/:id

router.get("/:id", (req, res) => {
  var course = courses.find((c) => c.id === parseInt(req.params.id));
  if (!course) res.status(404).send("course not found with given id");
  res.send(course);
});

router.get("/:year/:momth", (req, res) => {
  res.send(req.query);
});

module.exports = router;
