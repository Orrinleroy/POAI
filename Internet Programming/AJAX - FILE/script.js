function loadDoc(){
    var xml = new XMLHttpRequest();
    xml.open("GET", "rec.txt", true);
    xml.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            document.getElementById("demo").innerHTML = this.responseText;
        } else if (this.readyState == 4) {
            document.getElementById("demo").innerHTML = "Error loading data.";
        }
    };
    xml.onerror = function(){
        document.getElementById("demo").innerHTML = "Request error.";
    };
    xml.send();
} 