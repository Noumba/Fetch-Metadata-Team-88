const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#password");
const changeBorder = document.getElementsByTagName("INPUT");
console.log(changeBorder)

togglePassword.addEventListener("click", function () {
    // toggle the type attribute
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);
    
    // toggle the icon
    this.classList.toggle("bi-eye");

});
// bi bi-eye-slash

for (const input of changeBorder) {
    input.addEventListener("mouseout", function(){
        if(changeBorder.value.length > 0){
            this.style.borderColor = "black";
        }
    });

};





