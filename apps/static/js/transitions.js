
const app_name = 'transitions'
const survey = document.getElementById("survey");
const survey_response = document.getElementById("survey_response")
console.log("survey", survey)

question = "<span class='f4'>Which course <input id='question'/> <button onclick='send();'>OK</button></span>"


function start(){
    survey.innerHTML = question
}

function response_success(response){
    console.log(response)
    if (response.error == false){
        msg = `<div class="f4">Found course: ${response.result.name} [${response.result.id}]</div>`
    }
    else {
        msg = `<div class="f4">An error occurred: ${response.result[0]}</div>`
    }
    console.log('Success in response_success:', msg)
    survey_response.innerHTML = msg
}

function response_error(error){
    console.error('Application Error:', error)
    msg = `<div class="f4"> A network error occurred, lost contact with server</div>`
    survey_response.innerHTML = msg
}

function check_course_id(){
    course_text = document.getElementById('question').value
    console.log(course_text)
    fetch('/transitions/check_course_id',{
        method:'POST',
        body:JSON.stringify({course: course_text}),
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(res => res.json())
.then(response => response_success(response))
.catch(error => response_error(error));
}


// STATES: ['starting', 'checking', 'error', 'confirming', 'performing']
// TRANSITIONS:
// starting -> submit -> [error, confirming]
// error -> restart -> starting
// error -> finish -> end?
