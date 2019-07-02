survey = document.getElementById("survey");
console.log("survey", survey)

question = "<span>Which course <input id='question'/> <button onclick='send();'>OK</button></span>"


function load_question(){
    survey.innerHTML = question
}

function get_tp_target() {
    console.log('Give me all your children ...')
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
.then(response => console.log('Success:', JSON.stringify(response)))
.catch(error => console.error('Error:', error));
}


// STATES: ['starting', 'checking', 'error', 'confirming', 'performing']
// TRANSITIONS:
// starting -> submit -> [error, confirming]
// error -> restart -> starting
// error -> finish -> end?
