const Emitex = require("./eventemiter");
const emitobj = new Emitex();
//emit listerner for the out side module eventemiter
emitobj.on("emitteremit", arg => {
  console.log("listener called", arg);
});

emitobj.log("message");
