from flask import Flask, render_template, send_from_directory, abort, jsonify
from net_excavator import excavate_randomly

app = Flask(__name__)

@app.route('/')
def main():  # application's code here
    return render_template('mainpage.html')

# To download files in `data` folder.
# May have security problems... but that doesn't matter.
@app.route('/data/<filename>', methods=['GET', 'POST'])
def load_data(filename):
    try:
        return send_from_directory('data', filename, as_attachment=True)
    except Exception as e:
        print(filename)
        print(e)
        abort(404)

@app.route('/excavate')
def excavate_group():
    group_info = excavate_randomly()
    print("excavate successfully")
    return jsonify(group_info)

if __name__ == '__main__':
    app.run(debug=True)
