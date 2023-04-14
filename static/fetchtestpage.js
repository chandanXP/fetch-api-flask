function fetch_test(){
    fetch('/fetchtest')
    .then(response => response.json())
        .then(function(data){
            document.getElementById("to_change").innerHTML = data["1"]["pname"];
            document.getElementById("rev").innerHTML = "Reviews: "+ data["1"]["rcount"];
    })
}
