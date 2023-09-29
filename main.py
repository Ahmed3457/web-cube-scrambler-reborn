from lib import gen_scramble
try:
    from flask import Flask, render_template, request, jsonify
except:
    system("python -m pip install flask")
    from flask import Flask, render_template, request,jsonify

app = Flask(__name__)
port = 5000
# Preventing flask from messing up vue's work
app.jinja_env.variable_start_string = "^^"
app.jinja_env.variable_end_string = "^^"

def mainpage():
    return render_template("index.html")
    
def timer():
    return render_template("timer.html")

def register_FE_endpoints():
    app.add_url_rule("/", view_func=mainpage)
    app.add_url_rule("/timer", view_func=timer)
register_FE_endpoints()

@app.route("/api/scramble")
def scramble():
    cube = request.args.get("cube", "333")
    length = request.args.get("len", "20")
    length = int(length)
    scramble = gen_scramble(cube=cube, length=length)
    response = {
        "scramble": scramble,
        "length": length
    }
    return jsonify(response)
app.run(port=port, host="127.0.0.1", debug=True)