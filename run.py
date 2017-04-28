#!flask/bin/python
from app import app
app.secret_key = '#HHHscxcAsdxd!e3'
app.config['SESSION_TYPE'] = 'filesystem'
app.run(debug=True, port=5050)