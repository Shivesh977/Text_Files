var bulb=document.querySelector("#bulb")
var onn=document.querySelector("#onn")
var off=document.querySelector("#off")

onn.addEventListener("click",function(){
    bulb.style.backgroundColor="yellow" 
})

off.addEventListener("click",function(){
    bulb.style.backgroundColor="white"
})