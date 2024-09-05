from flask import Flask, render_template
api = Flask(__name__)


@api.route('/', methods=['GET'])
def get_main():
    return render_template('main.html')


@api.route('/about', methods=['GET'])
def get_about():
    return render_template('About.html')

if __name__ == '__main__':
    api.run(debug=True)
