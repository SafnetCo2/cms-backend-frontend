from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return 'Flask is working well see in the browser'
if __name__=='__main__':
    app.run(debug=True)