from flask import Flask

import vsearch

app = Flask(__name__)

@app.route('/')
def hello() ->str:
    return 'Hello world from Flask!'

@app.route('/search4') 
def do_search() ->str:
    return str(vsearch.search4latters('Ride the lightning', 'oiurf'))
    
app.run()
