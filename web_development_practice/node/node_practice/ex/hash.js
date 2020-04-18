const bcrypt = require("bcrypt");
async function run() {
  const salt = await bcrypt.genSalt(10);
  const hashedpass = await bcrypt.hash("134", salt);
  console.log(salt);
  console.log(hashedpass);
}
run();
