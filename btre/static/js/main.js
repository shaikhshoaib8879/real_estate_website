const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


setTimeout(function(){
    $('#messgae').fadeOut('slow');
},3000);