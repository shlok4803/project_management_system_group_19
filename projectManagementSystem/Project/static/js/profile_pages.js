let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

menuicn.addEventListener("click", () => {
	nav.classList.toggle("navclose");
})


const fullname=document.querySelector("#fullname");
const email=document.querySelector("#email");
const contact=document.querySelector("#contact");
const role=document.querySelector("#role");
const company=document.querySelector("#company");
// const employeeid=document.querySelector("#employeeid");
// const savechanges=document.querySelector("#save_button");
// const changepassword=document.querySelector(".changepassword");
const btn=document.querySelector("#button1");
const buttons=document.querySelector(".buttons");

function editprofile(){
    fullname.readOnly = false;
    contact.readOnly = false;
    buttons.style.display ="flex"; 
    btn.style.display="none";
}

function savechanges(){
    btn.style.display="block";
    buttons.style.display="none";
    fullname.readOnly = true;
    contact.readOnly = true;
    role.readOnly = true;
    company.readOnly = true;
}