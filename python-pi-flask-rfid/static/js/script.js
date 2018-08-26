// https://www.taniarascia.com/how-to-connect-to-an-api-with-javascript/

const app = document.getElementById('root');

const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(container);

var scan_id = {};

function start_scanning(){
scan_id = setInterval(scan_card, 5000); //5 seconds
console.log("scanning started");
console.log(scan_id);
}

function stop_scanning(){
console.log(scan_id);
clearInterval(scan_id)
console.log("scanning stopped");
}

function scan_card() {
var request = new XMLHttpRequest();

request.open('GET', '/scan-card', true);
request.onload = function () {

  // Begin accessing JSON data here
  var data = JSON.parse(this.response);

  if (request.status >= 200 && request.status < 400) {
    console.log(data.text);
	const p = document.createElement('p')
	p.textContent = data.text;

	container.appendChild(p); 
	} else {
	const errorMessage = document.createElement('p');
    errorMessage.textContent = data.error;
    container.appendChild(p);
  }
}

request.send();
}


//clearInterval(id)