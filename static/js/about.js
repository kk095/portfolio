
function percent(){
    let percent=document.getElementsByClassName('per')
    for (let index = 0; index <percent.length; index++) {
        let per=percent[index].classList[1]
        let id=percent[index].id
        let ele=document.getElementById(id)
        ele.style.width=per+'%';
            }
}