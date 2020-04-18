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
  return await Course.find({
    isPublished: true,
    tags: { $in: ["frontend", "backend"] },
  })
    .sort("-price")
    .select("name author price");
  //.count();
}

async function run() {
  const courses = await getcourses();
  console.log(courses);
}

run();
