console.log('hello world')
console.warn('this is a warning')
console.error('this is an error')   

const users=[
    {
        name:'John',role:'admin'

    },
    {
        name:'Jane',role:'user'
    }
]
console.table(users)

//  use the time() and timeEnd()


console.time('MyTimer')

for (let i=0;i<3;i++){

}
console.timeEnd('MyTimer'); 


//modern and most used

let nums =[1,2,3,4,5]
let doubled=nums.map(x=> x*2)
console.log(doubled);


let age=[12,13,14,15,16,17,18,19,20,21,22,23,24,25]
let adult=age.filter(age=> age>=18);
console.log(adult);

// reduce method 

let prices=[100,200,300,400,500]
let total=prices.reduce((accumulator,currentValue)=> accumulator+currentValue,0 )
console.log(total); 


/// foreach()
let colors=['red','green','blue'];
colors.forEach(element => {
    console.log(element);
});