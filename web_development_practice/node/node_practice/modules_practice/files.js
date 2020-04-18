const fs = require("fs");

// synchoranus readdir
const files = fs.readdirSync("./");
console.log(files);

// assyncharonus readdir

fs.readdir("./", function(err, files1) {
  if (err) console.log("error", err);
  else console.log("result", files1);
});
