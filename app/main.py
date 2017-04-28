from flask import Blueprint, render_template, abort, request, session, redirect, flash, url_for
from jinja2 import TemplateNotFound
import subprocess
import time
import app.utils as utils
import app.controler as controler


main_page = Blueprint('main_page', __name__, template_folder='templates')

@main_page.route('/')
@main_page.route('/index')
def index():
    return render_template('index.html')

@main_page.route('/h', methods=['GET', 'POST'])
def hash_create():
    if request.method == 'POST':
        if utils.check_string(str(request.form['hash_tag'])) == False:
            return render_template('bad_hash.html')
        else:
            subprocess.Popen("python3 backend/main.py -d {}".format(request.form['hash_tag']), shell=True)
            time.sleep(3)
            d = controler.diez.check(request.form['hash_tag'])
            result = controler.data.get(d.id)
            print(result)
            return render_template('line.html', result=result)





