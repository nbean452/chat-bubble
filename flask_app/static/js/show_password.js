function show_password(id) {
    // assign variable for the element
    var password = document.getElementById(id)

    // this line below shows the text inputted by the user
    // to the password field and vice versa
    if (password.type === "password") {
        password.type = "text";
    } else {
        password.type = "password";
    }
}