/* 
Team ID: 2b171785-d807-4c24-9080-26b981ee626e *
Team API Key: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiMjBjMjdmODctODE2NC0zNjM1LTg3ZjYtMjhmYWRkZjg0ZTNjIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiIyYjE3MTc4NS1kODA3LTRjMjQtOTA4MC0yNmI5ODFlZTYyNmUifQ.VQ_O_kd0Rt3Kd3u4nIUa2nZdQxPMjI9ohD0Ym6lQhUA
*/    

var apiKey = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiMjBjMjdmODctODE2NC0zNjM1LTg3ZjYtMjhmYWRkZjg0ZTNjIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiIyYjE3MTc4NS1kODA3LTRjMjQtOTA4MC0yNmI5ODFlZTYyNmUifQ.VQ_O_kd0Rt3Kd3u4nIUa2nZdQxPMjI9ohD0Ym6lQhUA"

var branches = {
  	method: 'GET',
  	headers: {
    	'Authorization': apiKey
  	}
};

var body = {
  		
}

// sendGetRequest('https://api.td-davinci.com/api/branches', branches)
// sendPostRequest('https://api.td-davinci.com/api/transfers')

function sendGetRequest(url, initObj) {
	var myRequest = new Request(url, initObj);

	fetch(myRequest)
  	.then(response => response.json())
  	.then(json => { // the json variable contains the response from the API
 	    for (var i=0; i<json.result.length; i++) {
	    	console.log(json.result[i])
	    }
  	});
}

postData("https://api.td-davinci.com/api/transfers", {answer: 42})
  .then(data => console.log(JSON.stringify(data))) // JSON-string from `response.json()` call
  .catch(error => console.error(error));

function postData(url = ``, data = {}) {
  // Default options are marked with *
    return fetch(url, {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        // mode: "cors", // no-cors, cors, *same-origin
        // cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        // credentials: "same-origin", // include, same-origin, *omit
        headers: {
        	"Content-Type": "application/json; charset=utf-8",
    		'Authorization': apiKey
  		},
        // redirect: "follow", // manual, *follow, error
        // referrer: "no-referrer", // no-referrer, *client
        body: {
		    "amount": 10,
		  	"currency": "CAD",
		  	"fromAccountID": "b9955b28-afbd-4e3e-8c30-61d0603806c5",
		  	"receipt": "{ \"reason\": \"My half of the lunch bill\"}",
		  	"toAccountID": "b9955b28-afbd-4e3e-8c30-61d0603806c5"
        } // body data type must match "Content-Type" header
    })
    .then(response => response.json()); // parses response to JSON
}