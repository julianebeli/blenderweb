survey = document.getElementById("survey");
survey_response = document.getElementById("survey_response")
console.log("survey", survey)

question = "<span class='f4'>Which course <input id='question'/> <button onclick='send();'>OK</button></span>"


function load_question(){
    survey.innerHTML = question
}

function get_tp_target() {
    console.log('Give me all your children ...')
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

function send(){
    course_text = document.getElementById('question').value
    console.log(course_text)
    fetch('/transitions/course_id',{
        method:'POST',
        body:JSON.stringify({course: course_text}),
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(res => res.json())
.then(response => response_success(response))
.catch(error => console.error('Application Error:', error));
}


// STATES: ['starting', 'checking', 'error', 'confirming', 'performing']
// TRANSITIONS:
// starting -> submit -> [error, confirming]
// error -> restart -> starting
// error -> finish -> end?
