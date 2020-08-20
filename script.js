function upload() {
var msg = window.document.getElementById('msg')
var img = window.document.getElementById('image')
var agora = new Date()
var hora = agora.getHours()
var minuto = agora.getMinutes()
msg.innerHTML = `It's ${hora} hours and ${minuto} minutes.`
if (hora >= 0 && hora < 12) {
    img.src = 'manha.png'
    document.body.style.background = 'green'
    msg2.innerHTML = 'Have a great morning!'

} else if (hora >= 12 && hora <= 18) {
    img.src = 'tarde.png'
    document.body.style.background = 'orange'
    msg2.innerHTML = 'Have a great afternoon!'
} else {
    img.src = 'noite.png'
    document.body.style.background = 'grey'
    msg2.innerHTML = 'Have a great evening!'
}
}
