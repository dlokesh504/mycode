const http = require("http");

// const server1 = http.createServer();
// //
// server1.on("connection", socket => {
//   console.log("new conncection");
// });

const server = http.createServer((req, res) => {
  if (req.url == "/") {
    res.write("Hello world");
    res.end();
  }

  if (req.url == "/api/courses") {
    res.write(JSON.stringify([1, 5, 4, 5, 4, 5, 4, 4]));
    res.end();
  }
});

server.listen(3000);

console.log("listinig on port no : 3000.....");
