const express = require("express");
const router = express.Router();
const mongoose = require("mongoose");
const joi = require("joi");
const bcrypt = require("bcrypt");
const { User } = require("../models/user");
const jwt = require("jsonwebtoken");
const config = require("config");

// const UserSchema = new mongoose.Schema({
//   email: { type: String, unique: true, required: true },
//   password: { type: String, required: true, maxlength: 1024 },
// });

router.post("/", async (req, res) => {
  const { error } = validate(req.body);
  if (error) return res.status(400).send(error.details[0].message);

  let user = await User.findOne({ email: req.body.email });
  if (!user) return res.status(400).send("invalid email or password....");

  const validpassword = await bcrypt.compare(req.body.password, user.password);
  if (!validpassword) return res.send(400).send("invalid password");

  const token = jwt.sign({ _id: user._id }, config.get("jwtprivatekey"));
  res.send(token);
});

function validate(req) {
  const schema = {
    email: joi.string().min(5).max(50).required().email(),
    password: joi.string().min(5).max(255).required(),
  };
  return joi.validate(req, schema);
}
module.exports = router;
