let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

let progress=document.getElementById("getProgress").innerHTML;
console.log(progress);
progress=parseInt(progress);
document.getElementById("styleProgress").innerHTML='<div class="progress" style="--i:'+progress+';--clr:#cc2020;"><h3>'+progress+'<span>%</span></h3><h4>OVERALL</h4></div>';

menuicn.addEventListener("click", () => {
    nav.classList.toggle("navclose");
})