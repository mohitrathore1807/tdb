function fullname() {
    var a = document.getElementById('fname');
    a.classList.add("is-active");
    document.getElementById("phone").classList.remove("is-active");
    document.getElementById("email").classList.remove("is-active");
    document.getElementById("enquiry").classList.remove("is-active");
    document.getElementById("help").classList.remove("is-active");
    document.getElementById("company").classList.remove("is-active");

}


function phone() {
  var a = document.getElementById("phone");
    a.classList.add("is-active");
    document.getElementById("fname").classList.remove("is-active");
    document.getElementById("email").classList.remove("is-active");
    document.getElementById("enquiry").classList.remove("is-active");
    document.getElementById("help").classList.remove("is-active");
    document.getElementById("company").classList.remove("is-active");

}
function email() {
  var a = document.getElementById("email");
    a.classList.add("is-active");
        document.getElementById("fname").classList.remove("is-active");
        document.getElementById("phone").classList.remove("is-active");
        document.getElementById("enquiry").classList.remove("is-active");
        document.getElementById("help").classList.remove("is-active");
        document.getElementById("company").classList.remove("is-active");
}
function enquiry() {
  var a = document.getElementById("enquiry");
    a.classList.add("is-active");
        document.getElementById("fname").classList.remove("is-active");
        document.getElementById("email").classList.remove("is-active");
        document.getElementById("phone").classList.remove("is-active");
        document.getElementById("help").classList.remove("is-active");
        document.getElementById("company").classList.remove("is-active");
}
function help() {
  var a = document.getElementById("help");
    a.classList.add("is-active");
        document.getElementById("fname").classList.remove("is-active");
        document.getElementById("email").classList.remove("is-active");
        document.getElementById("enquiry").classList.remove("is-active");
        document.getElementById("phone").classList.remove("is-active");
        document.getElementById("company").classList.remove("is-active");
}
function company() {
  var a = document.getElementById("company");
    a.classList.add("is-active");
        document.getElementById("fname").classList.remove("is-active");
        document.getElementById("email").classList.remove("is-active");
        document.getElementById("enquiry").classList.remove("is-active");
        document.getElementById("help").classList.remove("is-active");
        document.getElementById("phone").classList.remove("is-active");
}


function crossbtn() {
    document.getElementById("c3-getstartedform-modal").style.display = 'none';
}

function openbtn() {
  document.getElementById("c3-getstartedform-modal").style.display = 'block';
}