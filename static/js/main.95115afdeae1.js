function side_on(){
    document.getElementById("section1").style = "opacity: 0.5";
    document.getElementById("section2").style = "opacity: 0.5";
    document.getElementById("zapayn").style = "opacity: 0.5";
    document.getElementById("footer").style = "opacity: 0.5";
    document.getElementById("hr1").style = "opacity: 0.5";
    document.getElementById("hr2").style = "opacity: 0.5; background:#18191A; width:100%";
}

function side_of(){
    document.getElementById("section1").style = "opacity: 1";
    document.getElementById("section2").style = "opacity: 1";
    document.getElementById("zapayn").style = "opacity: 1";
    document.getElementById("footer").style = "opacity: 1";
    document.getElementById("hr1").style = "opacity: 1; background:#18191A; width:100%";
    document.getElementById("hr2").style = "opacity: 1; background:#18191A; width:100%";
}


function get_category(){
    document.getElementById("category-name").innerHTML = document.getElementById("select-category").value;
}