console.log("before");
getuser(1, function (user) {
  console.log("user", user);
});

console.log("after");

function getuser(id, callback) {
  setTimeout(() => {
    console.log("reading a user from data base.......");
    callback({ id: id, githubUsername: "loki" });
  }, 2000);
}
