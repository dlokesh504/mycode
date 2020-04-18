const os = require("os");

var totalmemory = os.totalmem();
var freememory = os.freemem();

console.log("total memory :" + totalmemory);

console.log("free memory :" + freememory);
