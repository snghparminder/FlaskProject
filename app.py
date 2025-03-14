from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templates')  # Ensure it points to the correct folder

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)



if __name__ == '__main__':
    app.run(debug=True)
