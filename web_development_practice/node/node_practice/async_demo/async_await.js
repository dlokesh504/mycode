// const p = new Promise((resolve, reject) => {
//   setTimeout(() => {
//     resolve([1, 2, 4, 3, 45, 4]); //pending =>resolved,fulfiled
//     reject(new Error("message")); //pending => ejected
//   }, 2000);
// });

// p.then((result) => console.log("result", result));
// p.catch((err) => console.log("Error", err.message));

async function demo() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve([1, 2, 4]);
    }, 2000);
  });
}

async function doo() {
  console.log("before");
  console.log("loading data.......");
  console.log(await demo());
  console.log("after");
}

doo();
