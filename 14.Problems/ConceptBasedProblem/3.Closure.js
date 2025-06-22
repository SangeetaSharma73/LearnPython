for (var i = 0; i < 3; i++) {
  console.log("1", i);
  setTimeout(function () {
    console.log("2", i);
  }, 1000);
}

// ✅ 1. Loop Closure Puzzle (with var)

for (var i = 0; i < 3; i++) {
  setTimeout(function () {
    console.log(i);
  }, 1000);
}
// Output:
// 3
// 3
// 3
// Why?
// var is function-scoped, so all closures inside the loop share the same i.
// After the loop ends, i is 3, so each setTimeout logs 3.
// Fix with let:

for (let i = 0; i < 3; i++) {
  setTimeout(function () {
    console.log(i); // 0, 1, 2
  }, 1000);
}

// ✅ 2. Closure Preserving State
const counter1 = makeCounter();
const counter2 = makeCounter();
console.log(counter1()); // 1
console.log(counter1()); // 2
console.log(counter2()); // 1
// Why?
// Each call to makeCounter() creates a new closure with its own count variable.
// counter1 and counter2 are independent.

// ✅ 3. Function Factory Trap

function createAdders() {
  var adders = [];
  for (var i = 1; i <= 3; i++) {
    adders.push(function (x) {
      return i + x;
    });
  }
  return adders;
}

const adders = createAdders();
console.log(adders); // 4 + 5 = 8? NO → 4
console.log(adders); // 4
console.log(adders); // 4
// Output:
// 4
// 4
// 4
// Why?
// After the loop, i is 4, so all functions return 4 + x.
// They all share the same i.

// Fix with let:
for (let i = 1; i <= 3; i++) {
  adders.push(function (x) {
    return i + x;
  });
}

// Or use an IIFE:
for (var i = 1; i <= 3; i++) {
  (function (j) {
    adders.push(function (x) {
      return j + x;
    });
  })(i);
}
// ✅ 4. Closure with let in Loop

for (let i = 0; i < 3; i++) {
  setTimeout(function () {
    console.log(i);
  }, 1000);
}
// Output:
// 0
// 1
// 2
// Why?
// let is block-scoped, so each iteration creates a new i for the closure.
// Works as expected.

// ✅ 5. Hidden State Exposure (Private Variables)
const holder = secretHolder("initial");
holder.setSecret("new");
console.log(holder.getSecret()); // "new"
// Why?
// secret is a private variable, only accessible via closures.
// This simulates encapsulation, like in OOP.

// ✅ 6. Closure Trap with this

function Person(name) {
  this.name = name;
  this.sayName = function () {
    setTimeout(function () {
      console.log(this.name); // undefined
    }, 1000);
  };
}
const p = new Person("Alice");
p.sayName();
// Output:
// undefined
// Why?
// Inside setTimeout, this refers to the global object (window or undefined in strict mode), not the Person instance.

// Fix with arrow function (lexical this):

this.sayName = function () {
  setTimeout(() => {
    console.log(this.name); // "Alice"
  }, 1000);
};

// ✅ 7. Closure Inside IIFE

var result = (function () {
  var name = "Closure";
  return {
    getName: function () {
      return name;
    },
    setName: function (newName) {
      name = newName;
    },
  };
})();

result.setName("Magic");
console.log(result.getName()); // "Magic"
// Why?
// The IIFE runs once and creates a private name variable.
// getName and setName form closures over it, simulating a module pattern.
