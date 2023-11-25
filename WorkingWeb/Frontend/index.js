
var xhr = null;

getXmlHttpRequestObject = function (){
    if (!xhr){
        //Create a new XMLHttpRequest object
        xhr = new XMLHttpRequest();
    }
    return xhr;
};

function getDate(){
    date = new Date().toString();
    // Changing the text of the div item to contain the current time
    document.getElementById('time-container').textContent = date;
}


function dataCallback() {
    // Check if response is ready or not
    // A "ReadyState" of "4" means that the request finished and response is ready
    // Status code 200 means that the request was completed successfully
    if (xhr.readyState == 4 && xhr.status == 200){
        console.log("User data received");
        getDate();
        dataDiv = document.getElementById('result-container');
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

// the getDate function is called automatically which adds the update time to the page on load
(function (){
    getDate();
}) ();

function sendData(){
    dataToSend = document.getElementById("data-input").value;
    if (!dataToSend){
        console.log("Data is empty.");
        return;
    }
    console.log("Sending data: " + dataToSend);
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = sendDataCallback;
    // asynchronous requests
    xhr.open("POST", "http://localhost:5885/users", true);
    // Informing the backend about what kind of data we are sending
    xhr.setRequestHeader("Content-Type", "application/json;cahrset=UTF-8");
    // Send the request over the network in proper json that will be
    // turned into a string
    xhr.send(JSON.stringify({"data": dataToSend}));
}

function sendDataCallback(){
    //Check if response is ready or not
    // Status 201 is usually sent when data was sent and the 
    // Backend created a new resource or piece of data
    if (xhr.readyState == 4 && xhr.status == 201){
        console.log("Data creation response received!");
        getDate();
        dataDiv = document.getElementById("sent-data-container");
        // Set current data text
        dataDiv.innerHTML = xhr.responseText;
    }
}

