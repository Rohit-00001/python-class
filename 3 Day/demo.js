console.log("A");
setTimeout(() => {
  console.log("C");
}, 0);
Promise.resolve().then(() => {
  console.log("D");
});
console.log("B");
