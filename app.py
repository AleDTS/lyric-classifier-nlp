# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from flask import Flask, render_template, request
from genre_classifier import GenreClassifier as gc

app = Flask(__name__)

classi = gc().load_model()

@app.route('/', methods=['GET', 'POST'])
def classifier():
	result = []
	lyric = []
	if request.method == 'POST':
		lyric.append(request.form['lyric'])
		result = classi.predict(lyric)
		return render_template('index.html',result=result[0])
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')