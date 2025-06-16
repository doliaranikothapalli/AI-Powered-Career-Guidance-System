from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    math = request.form.get('math')
    computers = request.form.get('computers')
    design = request.form.get('design')
    work = request.form.get('work')

    if math == 'yes' and computers == 'yes':
        suggestion = "You can explore a career in Data Science or Software Engineering."
    elif computers == 'yes' and design == 'yes':
        suggestion = "UI/UX Design or Front-End Development could suit you."
    elif design == 'yes' and work == 'practical':
        suggestion = "Consider Architecture or Graphic Design."
    elif math == 'no' and computers == 'no':
        suggestion = "You might enjoy careers in Arts, Communication, or Management."
    else:
        suggestion = "Explore interdisciplinary fields like Product Management or Business Analytics."

    return render_template('result.html', suggestion=suggestion)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
