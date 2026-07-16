// console.log("this is standard log message")
// console.info("this is an informational message");
// console.warn('warning:');
// console.error('error message')

// const users = [
//     { id: 1, name: "Alex", role: "Admin" },
//     { id: 2, name: "Bharat", role: "Developer" },
//     { id: 3, name: "Somnath", role: "Designer" }
// ];
// console.table(users);


// // console assert () conditional logging 

// // let userAge=19

// // console.assert(userAge >=18 , "voting")


// // console.time() and consol.timeend()

// // console.time('time start now')

// // for (let i=0;i<10000;i++){

// // }
// // console.timeEnd("loop timer")



// //  data types  

// // primitive data types ( objects )
// //  non primitives data types 



// // object : collections of key-values paris


// const studentInfo={
//     name:"suraj",
//     age:19,
//     email:'suraj@gmail.com'
// };

// console.log(studentInfo);
// console.log(studentInfo['name']);
// console.log(studentInfo['age']);
// console.log(studentInfo['email']);




// // array : a special type of object used to store ordered list of data 
 
// const colors =[12,32,43,53,1,32]

// console.log(colors);
// console.log(colors[0]);

// // functions callable object that execute a block of code 

// const sayHi= function(){

//     return "this is say hi function"
// }

// console.log(sayHi());



// console.log("string concatenations ");

// const firstname="suraj"
// const role="developer"

// const message="hello , my name is " + firstname + " and i am a " +role+ "."
// console.log(message);



// // dynamic variable injections 

// const emailTemplate=`Hi Customer,

// Thank you for your recent purchase.
// Your item will ship tomorrow.

// Best,
// Support Team

// `;

// console.log(emailTemplate);


// let day ="Monday"
// switch (day) {
//     case "Monday":
//         console.log("start of the work week");
//         break;

//    case "Friday":
//          console.log("weekend in almost hear");
//          break;
//     default:
//         console.log("just a regular day.");
// }


// // functions declarations ( the standard way )



// function greetUser(username){
//     return `hello , ${username} !`;
// }
// let message1=greetUser("suraj")
// console.log(message1);

// // function expressions 

// const addNumbers = function(a,b){
//     return a+b;
// };


// console.log(addNumbers(5,32));


// console.log("arrow functions (modern ES6 syntax");
// console.log("=>");


// const multiply = (x,y)=> {
//     return x * y;
// };

// console.log(multiply(23,2));


// const calculateTotal= (k,k1=2)=> {
//     return k * k1;
// };
// console.log(calculateTotal(34));



// // function has no return 

// console.log(`if you write a functions without 
//     a return statement , 
//     or if you write the keyword return by itself
//      without giving it a value ,
//      javascript automatically return undefined`);



// function doNothing() {
//     let x=13+3;
//     return x
// }
// let output= doNothing();
// console.log(output);


// //  short hand returns with arrow functions 
// console.log("short hand return with arrow functions ");
// const add=(a,b) => { 
//     return a+b;
// }
// console.log(add(23,22));


// console.log("array Basics ");

// // an array is a special non- primitive data types used to store an ordered list of values 


// const fruits =['apple','banana', 'cherry']

// console.log(fruits);
// console.log(fruits[0]);
// console.log(fruits.length);



// //  .push() -> adds one or more items to the very end 

// fruits.push('bronze')

// console.log(fruits);


// //  pop () - > remove the very last item and return it 

// fruits.pop();
// console.log(fruits);


// //  .unshift() -> adds an item to the very beginning 

// fruits.unshift('platinum')
// console.log(fruits);

// //  .shift() -> remove the very first item 

// fruits.shift();
// console.log(fruits);

// // indexOf() 


// console.log(fruits.indexOf('apple'));

// //  .lastIndexOf()
// // .includes() --> checks if an item exits anywhere in the array 


console.log("DOM (Document object models ");


const headingElement=document.getElementById('title')

headingElement.addEventListener("click",()=>{
    headingElement.innerText="welcome to js"
})


//  types of common events 


// 1 mouse event  -> click , dbclick , mouseenter
   
// 2 keyboard events -> keydown 

// 3 form events ->submit , change ,input
// document /window events -> domconTextLoaded 

