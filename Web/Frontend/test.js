//Figuring out how to redirect a user to another page 
//after authenticating and adding the entry into the database

// Check if response is ready or not
// A "ReadyState" of "4" means that the request finished and response is ready
// Status code 200 means that the request was completed successfully
// Make a variable for the location of the Element that will hold the text of the data
// Change the text of that Element to the "responeText" from the request
var xhr = null;

console.log("working");

const startUsernameHolder = document.getElementById('Start-Username');
const topicHolder = document.getElementById('Start-Topic');
const endUsernameHolder = document.getElementById('End-Username')


//Create a new XMLHttpRequest object
const getXmlHttpRequestObject = () => {
    if (!xhr){
        xhr = new XMLHttpRequest();
    }
    return xhr;
};


function sendStartEntry(){
    var username = startUsernameHolder.value;
    var topic = topicHolder.value;
    var dataToSend = `[${username}, ${topic}]`

    if (!(username && topic) || username == "Username" || topic == 'Topic'){
        console.log("One or more fields are empty.");
        addItem('Start','Start-Session-Display','*One or more fields are empty*');
        return;
    }else if(document.getElementById('Start-error-item')){
        document.getElementById('Start-error-item').remove();
    }

    topicHolder.value = "Username";
    startUsernameHolder.value = "Username";
    console.log("Initiating Post Request...");
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 4 && xhr.status == 201){
            console.log("Post Request Finished")
            sendPopUp(`New Session Created!
                \nUsername: ${username}\nTopic: ${topic}`);
        }
    };
// asynchronous requests
    xhr.open("POST", "http://localhost:5885/logStart", true);
// Informing the backend about what kind of data we are sending
    xhr.setRequestHeader("Content-Type", "application/json;charset=utf-8");
// Send the request over the network in proper json that will be
// turned into a string
    console.log(JSON.stringify({"data": dataToSend}));
    xhr.send(JSON.stringify({"data": dataToSend}));
};

function sendEndEntry(){
    const username = endUsernameHolder.value;
    if (!(username) || username == "Username"){
        addItem('End','End-Session-Display','*Username field is empty*');
        return;
    }else if(document.getElementById('End-error-item')){
        document.getElementById('End-error-item').remove();
    }
    //endUsernameHolder.value = "";
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 4 && xhr.status == 201){
            console.log("sendEndEntry has finished");
            addEndSessionTime();
        }
    }
    xhr.open("POST", "http://localhost:5885/logEnd", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=utf-8");
    console.log(JSON.stringify({"username": username}));
    xhr.send(JSON.stringify({"username": username}));
};


const addEndSessionTime = () => {
        console.log('addEndSessionTime running..');
        sendEndUsername(getSessionTime);
}

const sendEndUsername = (callback) => {
    let form = document.getElementById('End-Username');
    let username = form.value;
    console.log(`Sending username: ${username}`);
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = function(){
        if (xhr.readyState == 4 && xhr.status == 201){
            console.log("Picking up user entry.");
            callback();
        }
    };
    xhr.open('POST','http://localhost:5885/sendEndUsername',true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=utf-8');
    xhr.send(JSON.stringify({'username': username}));
};

const getSessionTime = () => {
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = function(){
        if (xhr.readyState == 4 && xhr.status == 200){
            let parsedData = JSON.parse(xhr.responseText);
            console.log("User data received.");
            let data = parsedData['data'];
            sendPopUp(`Session Ended!\nYour Study Session Lasted:\n${data}`);
        }
    };
    xhr.open('GET','http://localhost:5885/getEndInfo', true);
    xhr.send(null);
}

const addItem = (displayName, containerId, textToAdd) => {
    holder = document.getElementById(containerId);
    newItem = document.createElement('h2');

    if(!(document.getElementById(`${displayName}-error-item`))){
        newItem.setAttribute('id',`${displayName}-error-item`);
        newItem.setAttribute('class', 'error-item');
        newItem.innerText = textToAdd;
        holder.appendChild(newItem);
    }    
};

const sendPopUp = (text) => {
    let body = document.getElementById('body');
    let container = document.createElement('div');
    let popText = document.createElement('h1');
    let popButton = document.createElement('button');
    popButton.setAttribute('id', 'popButton');
    popButton.setAttribute('onclick', 'document.getElementById("popUpContainer").remove()');
    popButton.innerText = 'Exit';
    container.setAttribute('class', 'fixed-div');
    container.setAttribute('id', 'popUpContainer');
    popText.setAttribute('class', 'fixed-text');
    console.log(text)
    popText.innerText = text;
    container.appendChild(popText);
    container.appendChild(popButton);
    body.appendChild(container);
}
