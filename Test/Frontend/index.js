
var xhr = null;

getXmlHttpRequestObject = function (){
    if (!xhr){
        //Create a new XMLHttpRequest object
        xhr = new XMLHttpRequest();
    }
    return xhr;
};

function dataCallback() {
    // Check if response is ready or not
    // A "ReadyState" of "4" means that the request finished and response is ready
    // Status code 200 means that the request was completed successfully
    if (xhr.readyState == 4 && xhr.status == 200){
        console.log("User data received");
        getDate();
        dataDiv = document.getElementById('data-container');
        // Set current data text
        dataDiv.innerHTML = xhr.responseText;
    }
}

function getUsers(){
    console.log("Get Users...");
    xhr = getXmlHttpRequestObject();
    // One the state of the request changes to the optimal status and readystate
    // We will call the dataCallback function
    xhr.onreadystatechange = dataCallback;
    // asynchronous requests
    // Sends a request to the webpage created with Python in app.py
    xhr.open("GET", "http://localhost:5885/users", true);
    // Send the request over the network
    // The "null" will makesure that there is no extra text after the data
    // has been received
    xhr.send(null);
}


