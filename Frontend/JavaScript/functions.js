let userDataBase=[]

const registerUser=(name,email,password)=>{
    const newUser={
        name,email,password
    }
    userDataBase.push(newUser);
    return `user ${name} registered successfully`
};

console.log(registerUser('John','john@example.com','password123')); 
console.log(userDataBase);