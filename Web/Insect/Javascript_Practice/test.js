var global_var = "This is global.";

function newFunction() {
    var local_var = "This is local.";
    console.log(local_var);
}

console.log(global_var);
console.log(local_var); // local_var is not defined
