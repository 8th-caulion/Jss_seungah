const targetForm = document.querySelector('.jss_content_form') //값 불변 
// let b =  값 가변
// console.log(targetForm) python 에서 프린트 역할을 해주는 것
const counted_text = document.querySelector('.counted_text')
targetForm.addEventListener("keyup", function() {
    counted_text.innerHTML = targetForm.value.length
})

// 장고로 했으면 깜빡거림 + view단에서 처리하는 번거로움?