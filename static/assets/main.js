const goTop = document.querySelector(".gotop-btn");

window.addEventListener("scroll", scrollFunction)

function scrollFunction(){
    if(window.pageYOffset > 340){
        goTop.style.display = "block"
    }
    else{
        goTop.style.display = "none"
    }
}



const acordionItemHeader = document.querySelectorAll(".acordion-item-header");

acordionItemHeader.forEach(acordionItemHeader => {
    acordionItemHeader.addEventListener("click", event =>{
        acordionItemHeader.classList.toggle("active");
        acordionItemHeader.classList.toggle("b-bottom");
    })
})


const navbarToggle = document.getElementsByClassName("navbar-toggle")[0]
const navbarLink = document.getElementsByClassName("navbar-links")[0]

navbarToggle.addEventListener("click", () => {
    navbarLink.classList.toggle('active')
})


const icotgle = document.getElementById("ham-icon")

icotgle.addEventListener("click", () => {
    
    if ( document.getElementById("ham-icon").classList.contains('fa-bars') ){
        document.getElementById("ham-icon").classList.add('fa-times');
        document.getElementById("ham-icon").classList.remove('fa-bars');
    }
    else{
        document.getElementById("ham-icon").classList.add('fa-bars');
        document.getElementById("ham-icon").classList.remove('fa-times');
    }



})

function order(id){
    $.ajax({
        type : 'POST',
        url : 'make_order',
        data : {
            name : $('#name').val(),
            contact : $('#contact').val(),
            message : $('#message').val(),
            qty : $('#qty').val(),
            district : $('#district').val(),
            remarks : $('#remarks').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success : function (response){
            document.getElementById(id).style.color = "green";
            document.getElementById(id).innerHTML = response["responseJSON"]["message"];
            document.getElementById(id).style.border = "2px solid green";
            document.getElementById(id).style.borderRadius = "10px";
            document.getElementById(id).style.padding = "10px";
        },
        error : function (response){
            document.getElementById(id).style.color = "red";
            document.getElementById(id).innerHTML = response["responseJSON"]["message"];
            document.getElementById(id).style.border = "2px solid red";
            document.getElementById(id).style.borderRadius = "10px";
            document.getElementById(id).style.padding = "10px";
        }
    })
}

function question(id){
    $.ajax({
        type : 'POST',
        url : 'make_question',
        data : {
            name : $('#name').val(),
            contact : $('#contact').val(),
            e_mail : $('#e-mail').val(),
            message : $('#message').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success : function (response){
            document.getElementById(id).style.color = "green";
            document.getElementById(id).innerHTML = response["responseJSON"]["message"];
            document.getElementById(id).style.border = "2px solid green";
            document.getElementById(id).style.borderRadius = "10px";
            document.getElementById(id).style.padding = "10px";
        },
        error : function (response){
            document.getElementById(id).style.color = "red";
            document.getElementById(id).innerHTML = response["responseJSON"]["message"];
            document.getElementById(id).style.border = "2px solid red";
            document.getElementById(id).style.borderRadius = "10px";
            document.getElementById(id).style.padding = "10px";
        }
    })
}



//document.getElementById("ham-icon").classList.add('fa-chart-bar');

//document.getElementById("MyElement").classList.remove('fa-bars');



