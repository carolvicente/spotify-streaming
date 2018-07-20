from flask import Flask, request, render_template, redirect, url_for

app = Flask('spotify-predictor')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['tk']
      return redirect(url_for('success',token = user))
   else:
      user = request.args.get('tk')
      return redirect(url_for('success',token = user))


@app.route('/my-dashboard/<token>')
def success(token):
   return 'welcome %s' % token


app.run(debug=True, use_reloader=True)