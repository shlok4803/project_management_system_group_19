let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

menuicn.addEventListener("click", () => {
	nav.classList.toggle("navclose");
})


const fname=document.querySelector("#fname");
const mail=document.querySelector("#mail");
const phone=document.querySelector("#phone");
const mobile=document.querySelector("#mobile");
const address=document.querySelector("#address");
const employeeid=document.querySelector("#employeeid");
const savechanges=document.querySelector(".savechanges");
const changepassword=document.querySelector(".changepassword");
const btn=document.querySelector(".btn");

function editprofile(){
    fname.readOnly = false;
    mail.readOnly = false;
    phone.readOnly = false;
    mobile.readOnly = false;
    address.readOnly = false;
    employeeid.readOnly = false;
    savechanges.style.visibility ="visible"; 
    changepassword.style.visibility ="visible"; 
    btn.style.visibility="hidden";
}

function savechange(){
    btn.style.visibility="visible";
    savechanges.style.visibility="hidden";
    changepassword.style.visibility ="hidden";
    fname.readOnly = true;
    mail.readOnly = true;
    phone.readOnly = true;
    mobile.readOnly = true;
    address.readOnly = true;
    employeeid.readOnly = true;
}