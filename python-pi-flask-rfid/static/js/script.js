// https://www.taniarascia.com/how-to-connect-to-an-api-with-javascript/
// 5000 = 5 seconds
const refresh_rate = 5000; 

const app = document.getElementById('root');

const container = document.createElement('div');
container.setAttribute('class', 'container');

const scanner = document.createElement('div');
scanner.setAttribute('id', 'scanner');

const page = document.createElement('div');
page.setAttribute('id', 'page');

app.appendChild(container);
app.appendChild(scanner);
app.appendChild(page);

// Card Scanner

const p = document.createElement('p')
p.id = "scan_card";
scanner.appendChild(p);

// Page

const page_h1 = document.createElement('h1')
const page_p = document.createElement('p')
const page_img = document.createElement('img')

page.appendChild(page_h1);
page.appendChild(page_p);
page.appendChild(page_img);


var scan_id = {};

function start_scanning(){
	scan_id = setInterval(scan_card, refresh_rate); 
	console.log("scanning started");
	console.log(scan_id);
}

function stop_scanning(){
	console.log(scan_id);
	clearInterval(scan_id);
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

	if (data.text != undefined) {

	const new_card = document.createElement('p')
	new_card.id = "scan_card";
	new_card.textContent = "Card data: " + data.text;
	
	previous_card = document.getElementById("scan_card")
	var parentDiv = previous_card.parentNode;

	parentDiv.replaceChild(new_card, previous_card)

	get_page(data.text);
	stop_scanning();

	} else {
	const card = document.createElement('p')
	card.id = "scan_card";
	card.textContent = "Card data: unavailable";

	previous_card = document.getElementById("scan_card")
	var parentDiv = previous_card.parentNode;

	parentDiv.replaceChild(card, previous_card)
	no_page = document.getElementById("page")
	no_page.innerHTML = '';
	
	}} else {
	const errorMessage = document.createElement('p');
	errorMessage.textContent = data.error;
	container.appendChild(errorMessage);
  }
}

request.send();
}


function get_page(page_id) {
var request = new XMLHttpRequest();

page_url = '/page/'+ page_id
console.log(page_url);

request.open('GET', page_url, true);
request.onload = function () {

  // Begin accessing JSON data here
  var data = JSON.parse(this.response);

  if (request.status >= 200 && request.status < 400) {
    console.log(data.description);
	const new_page = document.createElement('div')
	new_page.id = "page";

	const new_h1 = document.createElement('h1')
	new_h1.textContent = data.title;

	const new_p = document.createElement('p')
	new_p.textContent = data.description;
	
	const new_img = document.createElement('img')
	new_img.src = data.image_url;

	new_page.appendChild(new_h1);
	new_page.appendChild(new_p);
	new_page.appendChild(new_img);

	previous_page = document.getElementById("page")
	var parentDiv = previous_page.parentNode;

	parentDiv.replaceChild(new_page, previous_page)

	} else {
	const errorMessage = document.createElement('p');
	errorMessage.textContent = data.error;
	container.appendChild(errorMessage);
  }
}

request.send();
}

//clearInterval(id)