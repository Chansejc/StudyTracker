
var xhr = null;

//Create a new XMLHttpRequest object
getXmlHttpRequestObject = function (){
    if (!xhr){
        xhr = new XMLHttpRequest();
    }
    return xhr;
};

// Check if response is ready or not
// A "ReadyState" of "4" means that the request finished and response is ready
// Status code 200 means that the request was completed successfully
// Make a variable for the location of the Element that will hold the text of the data
// Change the text of that Element to the "responeText" from the request
function dataCallback() {
    if (xhr.readyState == 4 && xhr.status == 200){
        console.log("User data received");
        dataDiv = document.getElementById('data-container');
        // Set current data text
        dataDiv.innerHTML = xhr.responseText;
    }
}

// One the state of the request changes to the optimal status and readystate
// We will call the dataCallback function
// asynchronous requests
// Sends a request to the webpage created with Python in app.py
// Send the request over the network
// The "null" will makesure that there is no extra text after the data
// has been received
function getUsers(){
    console.log("Get Users...");
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    xhr.open("GET", "http://localhost:5885/users", true);
    xhr.send(null);
}


