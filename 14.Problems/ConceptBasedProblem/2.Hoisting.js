//1.
// console.log(a);
// var a = 5;

// 🟩 Output: undefined
// 🧠 Why?
// var a is hoisted to the top and initialized as undefined. The assignment happens later.

//2.
// console.log(b);
// let b = 10;
// 🟥 Output: ReferenceError: Cannot access 'b' before initialization
// 🧠 Why?
// let is hoisted but not initialized. It exists in the Temporal Dead Zone (TDZ) until the line let b = 10.

//3.
// foo();
// function foo() {
//   console.log("Hoisted!");
// }
// 🟩 Output: Hoisted!
// 🧠 Why?
// Function declarations are hoisted completely, including their body.

//4.
// foo();

// var foo = function () {
//   console.log("Will this run?");
// };
// 🟥 Output: TypeError: foo is not a function
// 🧠 Why?
// Only the declaration var foo is hoisted (as undefined). The assignment to a function happens later, so at the time of call, foo is still undefined.

//5.
// foo();
// var foo = () => {
//   console.log("arrow function");
// };

//6.
// function test() {
//   console.log(x);
//   var x = 10;
//   console.log(x);
// }
// test();

//7.
// var a = 1;
// function test() {
//   console.log(a);
//   var a = 2;
// }
// test();

//8.
// function test() {
//   console.log(x);
//   let x = 10;
// }
// test();

//9.
// var a = 5;
// function foo() {
//   console.log(a);
//   var a = 10;
// }
// foo();
// console.log(a);

//10.
// function outer() {
//   var x = 10;

//   function inner() {
//     console.log(x);
//     var x = 20;
//   }

//   inner();
// }
// outer();

function outer() {
  var x = 10;

  function inner() {
    console.log(x); // Now this logs 10
  }

  inner();
}
outer();

//11.
// var x = 21;

// // if (x) {
// //   var x = 23;
// // }
// var fun = function () {
//   console.log(x);
//   var x = 20;
// };

// fun();
// console.log(x);
