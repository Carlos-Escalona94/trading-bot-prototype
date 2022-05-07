from flask import Flask

app = Flask('app')

@app.route('/')
async def get():
    return 'a'


@app.route('/', methods = ['POST'])
async def post():
    return 'a'
