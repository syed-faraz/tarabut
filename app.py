import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask

def get_shell_script_output_using_check_output():
    stdout = check_output(['./encrypt.sh']).decode('utf-8')
    return stdout

app = Flask(__name__)

@app.route('/',methods=['GET',])
def home():
    return '<pre>'+get_shell_script_output_using_check_output()+'</pre>'

app.run(debug=True)