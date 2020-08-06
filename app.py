from flask import Flask, render_template, request
from seoranking import search_ranking

app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('app.html', name=user)

@app.route('/check_ranking', methods=['POST'])
def check_ranking():
   website = request.form['website']
   ad_keyword = request.form['ad_keyword']
   google_extension = request.form['googleextension']
   pos = search_ranking(ad_keyword, extension, google_extension)
   return (f"{website} is in the position:{pos}")
       

if __name__ == '__main__':
   app.run(debug = True)