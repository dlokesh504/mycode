console.log("before");
const user = getuser(1);
console.log(user);
console.log("after");

function getuser() {
  setTimeout((id) => {
    console.log("reading a user from data base.......");
    return { id: id, githubUsername: "loki" };
  }, 2000);
}
