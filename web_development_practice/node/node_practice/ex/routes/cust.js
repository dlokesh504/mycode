const express = require("express");
const route = express.Router();
const mongoose = require("mongoose");
const joi = require("joi");

const custSchema = new mongoose.Schema({
  name: String,
  isGold: Boolean,
  phone: Number,
});

const Cust = mongoose.model("costomers", custSchema);
route.post("/", async (req, res) => {
  let cust = new Cust({
    name: req.body.name,
    isGold: req.body.isGold,
    phone: req.body.phone,
  });
  cust = await cust.save(cust);
  res.send(cust);
});
route.get("/", async (req, res) => {
  const custs = await Cust.find();
  res.send(custs);
});

module.exports = route;
