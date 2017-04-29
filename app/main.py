from flask import Blueprint, render_template, request, jsonify
import subprocess
import time
import app.utils as utils
import app.controler as controler


main_page = Blueprint('main_page', __name__, template_folder='templates')



# lending page
@main_page.route('/')
@main_page.route('/index')
def index():
    return render_template('index.html')

# old method get hash in db
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


# new method get hash tag in db
@main_page.route('/h/<hastag>', methods=['GET', 'POST'])
def get_hash():
    if request.method == 'POST':
        if utils.check_string(str(request.form['hash_tag'])) == False:
            return jsonify({'code':404,'data': 'ERROR'})
        else:
            checkNewHashTag = controler.diez.check(request.form['hash_tag'])
            if checkNewHashTag is None:
                subprocess.Popen("python3 backend/main.py -d {}".format(request.form['hash_tag']), shell=True)
                time.sleep(5)
            d = controler.diez.check(request.form['hash_tag'])
            subprocess.Popen("python3 backend/main.py -d {}".format(request.form['hash_tag']), shell=True)
            result = controler.data.get(d.id)
            return jsonify({'code': 200, 'data': result})








