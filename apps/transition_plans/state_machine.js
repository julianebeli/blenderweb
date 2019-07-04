var StateMachine = require('javascript-state-machine');

var State = {}

var fsm = new StateMachine(
{
    init: 'establish',
    transitions: [
        {name:'load_state', from: 'establish', to:'ready'},
        {name:'get_course_id', from: 'ready', to:'process_input'},
        {name:'confirm', from: 'process_input', to:'confirm_request'},
        {name:'client_error', from: 'process_input', to:'input_fail'},
        {name:'server_error', from: 'process_input', to:'server_fail'},
        {name:'input_error', from: 'process_input', to:'no_input'},
        {name:'complete_task', from: 'confirm_request', to:'request_complete'},
        {name:'restart', from: 'no_input', to:'establish'},
        {name:'restart', from: 'server_fail', to:'establish'},
        {name:'restart', from: 'input_fail', to:'establish'},
        {name:'restart', from: 'request_complete', to:'establish'},
    ],
    methods:{
        onLoad_state: initialise(),
        onGet_course_id: check_input(),
        onConfirm: proceed(),
        onClient_error: process_client_error(),
        onServer_error: process_server_error(),
        onInput_error: process_input_error(),
        onComplete_task: complete_request(),
        onRestart: re_start()
    }
})

function initialise(){}
function check_input(){}
function proceed(){}
function process_client_error(){}
function process_server_error(){}
function process_input_error(){}
function complete_request(){}
function re_start(){}


