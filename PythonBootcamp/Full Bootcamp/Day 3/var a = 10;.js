var a = 10;
var b = "student"
var c = { name: "John", surname: "Doe" };
var d = 0;

console.log(c.name, "is a", d, "year old", b, "with a total mark of", a + ".");

if (a > d) {
    console.log(a + " is greater than " + d);
    console.log(`${a} is greater than ${d}.`);

} else if (d < a) {
    console.log(`${d} is greater than ${a}.`);
} else {
    console.log("COnditions not met")
}

item = 7
while (item <= 10){
    console.log(item * 2);
    item += 1;
}

d += a
console.log(d)

item = 5;
/*for (i = 2; i <= item; i++){
    d += i
    console.log()
}*/