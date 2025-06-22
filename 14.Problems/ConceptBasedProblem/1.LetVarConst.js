var name = "siya";
console.log(name);
var name = "Diya";
console.log(name); //redeclaration allowed

var age = 23;
age = 24;
console.log(age); //re- assign allowed

function checkVar() {
  console.log("age inside checkVar1", age); //undefined because var is function-scoped and the value is hoisted and initialized with undefined
  var age = 25;
  console.log("age inside checkVar2", age);
  if (age == 25) {
    var age = 26;
  }
  console.log("after block", age);
}

var key = "diya";
console.log("before block", key);
if (key == "diya") {
  var key = "siya";
}
console.log("after block", key);
checkVar();
console.log("after function call");
console.log("outside function", age); //24

let checkLet1 = "let";
// let checkLet = "new let" // re-declare not allowed
checkLet1 = "new let with re-assign"; // reassign is allowed
console.log(checkLet1);

function checkLet() {
  //   console.log("checklet1 inside checkLet1", checkLet1); refrence error checkLet1 cannot access before initialization because it is block scope
  let checkLet1 = 25;
  console.log("checklet1 inside checkLet2", checkLet1);
  for (let i = 0; i < 3; i++) {
    let checkLet1 = 34; //can be re-declare in another block but not in same block because it is block scoped
    console.log(checkLet1);
  }
}
checkLet();
console.log("after function call");
console.log(checkLet1); //new let with re-assign

const keyword = "const";
// const keyword = "new let"; // re-declare not allowed
// keyword = "new const with re-assign"; // reassign is not allowed
console.log(keyword);

function checkConst() {
  //   console.log("checkConst1 inside checkConst1", keyword); //const is block scoped so can't access in this scope that's why referenceError:can't acess keyword before initialization

  const keyword = 25;
  console.log("checkConst1 inside checkConst2", keyword);
  for (let i = 0; i < 3; i++) {
    const keyword = 34; //can be re-declare in another block but not in same block because it is block scoped
    console.log(keyword);
  }
}
checkConst();
console.log("after function call");
console.log(keyword); //new let with re-assign

// const a;
// a = 10;
// Answer: ❌ SyntaxError: Missing initializer in const declaration
// Explanation: const must be initialized at the time of declaration.

for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Answer: 3, 3, 3
// Explanation: var is function-scoped. By the time the callback runs, i is already 3.

for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Answer: 0, 1, 2
// Explanation: let is block-scoped, so each iteration gets a new i.
