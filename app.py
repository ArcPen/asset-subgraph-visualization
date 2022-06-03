from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

@app.route('/')
def main():  # application's code here
    return render_template('mainpage.html')

@app.route('/force_map')
def force_map():
    return render_template('force_map.html')

# To download files in `data` folder.
# May have security problems... but that doesn't matter.
@app.route('/data/<filename>', methods=['GET', 'POST'])
def load_data(filename):
    try:
        return send_from_directory('data', path=filename, as_attachment=True)
    except Exception as e:
        print(filename)
        print(e)
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
