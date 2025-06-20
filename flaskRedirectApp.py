from flask import Flask, redirect

app = Flask(__name__)

# simulate the expired path
@app.route('/accounts/jinxboy/projects/knooz/builds/b0ee4444-420b-4094-9e9d-3a6cf36e60f7')
def redirect_to_new_apk():
    return redirect("https://www.youtube.com/results?search_query=how+to+use+expired+link+to+direct+to+a+link+i+want", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
