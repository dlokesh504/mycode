const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost/mongo-excercises");

const courseSchema = mongoose.Schema({
  name: String,
  author: String,
  tags: [String],
  date: Date,
  isPublished: Boolean,
  price: Number,
});

const Course = mongoose.model("Course", courseSchema);

async function getcourses() {
  return await Course.find({ isPublished: true, tags: "backend" })
    .sort({ name: 1 })
    .select({ name: 1, author: 1 });
  //.count();
}

async function run() {
  const courses = await getcourses();
  console.log(courses);
}

run();
