const mongoose = require("mongoose");
mongoose
  .connect("mongodb://localhost/playground")
  .then(() => console.log("connected to mongodb.."))
  .catch((err) => console.log("could not connect to mongodb...", err));

const courseschema = new mongoose.Schema({
  name: { type: String, required: true, minlength: 5, maxlength: 25 },
  author: String,
  tags: [String],
  date: { type: Date, default: Date.now },
  ispublished: Boolean,
});

const Course = mongoose.model("courses", courseschema);

async function createcourse() {
  const course = new Course({
    name: "angular",
    author: "mosh",
    tags: ["amgular", "frontend"],
    ispublished: true,
  });

  const result = await course.save();
  console.log(result);
}

async function createcoursewithvalidate() {
  const course = new Course({
    //name: "angular",
    // author: "mosh",
    tags: ["amgular", "frontend"],
    ispublished: true,
  });
  try {
    await course.validate();
    const result = await course.save();
    console.log(result);
  } catch (ex) {
    console.log(ex.message);
  }
}
async function getcourses() {
  const courses = await Course.find({ name: "angular" })

    //.find({price:{$gte:10,$lte:20}})
    //.find({ price: { $in: [10, 20, 30] } }) // comparision opertators
    //.find()
    //or({name:'angular},{ispublished:True})//logical quiery ops
    //and(name:'angular},{ispublished:True)

    //starts with Mosh
    .find({ author: /^mosh/ })
    //ends with hamidhani
    .find({ author: /Hamidhani$/i })
    //if it has mosh
    .find({ author: /.*mosh.*/i })
    //.count() //returs matching documents
    .select({
      name: 1,
      author: 1,
    });
  console.log(courses);
}

async function updatecourse(ij) {
  const course = await Course.findById(ij);
  if (!course) return;

  course.ispublished = true;
  course.author = "another author";

  const result = await course.save();
  console.log(result);
}

async function removecourse(id) {
  const result = await Course.deleteOne({ _id: id });
  const course = await Course.findById(id);
  console.log(result);
  console.log(course);
}
//removecourse("5e8f40f98692e22a34c5ce30");
//updatecourse("5e8f40f98692e22a34c5ce30");
//getcourses();
createcoursewithvalidate();
