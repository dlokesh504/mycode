const mongoose = require("mongoose");
mongoose
  .connect("mongodb://localhost/playground")
  .then(() => console.log("connected to mongodb.."))
  .catch((err) => console.log("could not connect to mongodb...", err));

const courseschema = new mongoose.Schema({
  name: String,
  author: String,
  tags: [String],
  date: { type: Date, default: Date.now },
  ispublished: Boolean,
});

const Course = mongoose.model("course", courseschema);

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
getcourses();
