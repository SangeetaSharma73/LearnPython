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

// 🟩 Output:
// undefined
// 10
// 🧠 Why?
// var x is hoisted to the top of test, initialized as undefined. First log gives undefined, then it's assigned 10.

//7.
// var a = 1;
// function test() {
//   console.log(a);
//   var a = 2;
// }
// test();
// 🟩 Output: undefined
// 🧠 Why?
// Inside test(), var a is hoisted and shadows the global a. So console.log(a) refers to the local a, which is undefined at that point.

//8.
// function test() {
//   console.log(x);
//   let x = 10;
// }
// test();
// 🟥 Output: ReferenceError: Cannot access 'x' before initialization
// 🧠 Why?
// let x is block-scoped and in the TDZ. Accessing it before the let x = 10 line throws an error.

//9.
// var a = 5;
// function foo() {
//   console.log(a);
//   var a = 10;
// }
// foo();
// console.log(a);
// 🟩 Output:
// undefined
// 5
// 🧠 Why?
// In foo(), local var a is hoisted, so global a is shadowed. Local a is undefined at the first log. The outer a remains 5.

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
// 🟩 Output: undefined
// 🧠 Why?
// In inner(), var x is hoisted, so it shadows the x in outer. It’s undefined at the time of console.log(x).

function outer() {
  var x = 10;

  function inner() {
    console.log(x); // Now this logs 10
  }

  inner();
}
outer();

// 💥 JavaScript Hoisting:
// In JavaScript, var declarations are hoisted to the top of their scope, but not their assignments. So the function is interpreted like this:

// function inner() {
//   var x;          // hoisted declaration
//   console.log(x); // x is undefined here
//   x = 20;
// }
// ✅ So, does it follow closure behavior?
// ✔️ Yes, the function inner() still forms a closure over the outer scope (it could access x = 10).

// ❌ But, because it declares a local variable named x, it shadows the outer x, and due to hoisting, that local x is undefined at the time of the console.log.

// ✅ Fix it by removing the local x:
// function outer() {
//   var x = 10;

//   function inner() {
//     console.log(x); // Now this logs 10
//   }

//   inner();
// }
// outer();

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
// 🟩 Output: undefined
// 🧠 Why?
// Inside fun, var x is hoisted and shadows global x. It's undefined at the time of console.log(x).
