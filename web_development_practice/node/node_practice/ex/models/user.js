const mongoose = require("mongoose");
const joi = require("joi");
const UserSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, unique: true, required: true },
  password: { type: String, required: true, maxlength: 1024 },
});

function validateUser(user) {
  const schema = {
    name: joi.string().min(5).max(50).required(),
    email: joi.string().min(5).max(50).required().email(),
    password: joi.string().min(5).max(255).required(),
  };
  return joi.validate(user, schema);
}

const User = mongoose.model("Users", UserSchema);
exports.User = User;
exports.validateUser = validateUser;
