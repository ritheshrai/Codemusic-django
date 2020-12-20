const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
 
sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});
/* function validation(){
   username=document.querySelector("#username").value;
   firstname=document.querySelector("#firstname").value;
   lastname=document.querySelector("#lastname").value;
   email=document.querySelector("#email").value;
   pass1=document.querySelector("#pass1").value;
   pass2=document.querySelector("#pass2").value;
   if(pass1==pass2){
    var xhttp3 = new XMLHttpRequest();
    xhttp3.open("GET", "http://127.0.0.1:8000/register?username="+username+"&firstname="+firstname+"& lastname="+ lastname+"&email="+email+"&pass1="+pass1, true);
    xhttp3.send();
    xhttp3.onload = () => {
      if(xhttp3.status==200){
        var h= JSON.parse(xhttp3.response)
        alert(h.result);
   }
 }
}
 }*/