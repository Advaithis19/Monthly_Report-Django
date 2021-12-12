const showNav = (toggleId,navbarId,mainId)=>{
    const toggle = document.getElementById(toggleId)
    navbar = document.getElementById(navbarId)
    mainpadding = document.getElementById(mainId)
    if(toggle && navbar){
      toggle.addEventListener('click',()=>{
        navbar.classList.toggle('expand');
        mainpadding.classList.toggle('main-padding')
      })
    }
}

showNav('nav-toggle','navbar','main-id')