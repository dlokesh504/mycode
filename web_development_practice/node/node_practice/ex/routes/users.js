const express = require("express");
const router = express.Router();
const mongoose = require("mongoose");
const joi = require("joi");
const _ = require("lodash");
const bcrypt = require("bcrypt");
const { User, validateUser } = require("../models/user");
const jwt = require("jsonwebtoken");
const config = require("config");

router.post("/", async (req, res) => {
  const { error } = validateUser(req.body);
  if (error) return res.status(400).send(error.details[0].message);

  let user = await User.findOne({ email: req.body.email });
  if (user) return res.status(400).send("user already registerd..");

  user = new User({
    name: req.body.name,
    email: req.body.email,
    password: req.body.password,
  });
  tt = req.body.password;
  const salt = await bcrypt.genSalt(10);
  user.password = await bcrypt.hash(tt, salt);

  await user.save();
  const token = jwt.sign({ _id: user._id }, config.get("jwtprivatekey"));

  res.header("x-auth-token", token).send(_.pick(user, ["name", "email"]));
  //console.log(user.password);
});

module.exports = router;
