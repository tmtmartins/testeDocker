from flask import Flask
from flask import Response
from flask import Request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chamar():
    Response = request.post(url="http://0.0.0.0:5020/")
    print(Response)
    return Response

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5021)
    
app.run()
