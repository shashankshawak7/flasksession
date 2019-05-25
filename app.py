import flask
app=flask.Flask(__name__)
@app.route('/')
def myfuction():
    var=list(range(1,100,5))
    return flask.render_template('index.html',data=var)


@app.route('/myfile',methods=['GET','POST'])
def readfile():
    import pandas as pd
    
    df=pd.read_csv('completeData.csv',header=0)
    return flask.render_template('data.html',data=df)


@app.route('/x')
def weatherReport():
    url='http://api.apixu.com/v1/current.json?key=949dcc0987734f1caa073340192505&q=Paris'
    import requests
    response=requests.get(url)
    return flask.render_template('index.html',data=response.text)
    
app.run(debug=True)
