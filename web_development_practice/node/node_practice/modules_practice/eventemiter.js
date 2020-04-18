const EventEmitter = require("events");
const emitter = new EventEmitter();

//emitter listener
// emitter.on("messageloges", arg => {
//   console.log("listener called", arg);
// });

// //raiser event

// emitter.emit("messageloges", { id: 1, url: "htps://" });

class Emitex extends EventEmitter {
  log(message) {
    console.log(message);

    this.emit("emitteremit", { id: 1, url: "https://" });
  }
}

module.exports = Emitex;
