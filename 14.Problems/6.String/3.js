function mech() {
  let coin = 10; // private
  return {
    addCoins: function () {
      coin++;
      console.log("added coins", coin);
    },
    seeCoins: function () {
      console.log("total coins", coin);
    },
  };
}

let m = mech();
console.log(m.addCoins());
