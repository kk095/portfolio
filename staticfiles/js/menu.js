let x=document.getElementById('menu')
let menu_=document.getElementsByClassName('menu_')
let z=document.getElementById('b')
let cancel=document.getElementsByClassName('cancel')
x.addEventListener('click',fun);
let y=document.getElementsByClassName('div1-2a')
function fun(){
    if(cancel[0]!=undefined){
        y[0].classList.remove('cancel')
    }
    setTimeout(menu,1000)
    y[0].classList.add('a')
    x.style.visibility='hidden'
    z.style.visibility='visible'
    
}
function menu(){
    menu_[0].classList.add('menu_box')
    console.log('done');
}
z.addEventListener('click',fun2);
function fun2(){
    z.style.visibility='hidden'
    x.style.visibility='visible'
    menu_[0].classList.remove('menu_box')
    y[0].classList.add('cancel')
    y[0].classList.remove('a')
}