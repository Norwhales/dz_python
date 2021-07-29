from flask import Flask, jsonify, request

app = Flask(__name__)

client = app.test_client()

movieList = [
    {
        'title': "The LightHouse",
        'description': "some text"
    },
    {
        'title': "Avengers",
        'description': "some text"
    }
]


@app.route('/getHelloWorld', methods=['GET'])
def get_HelloWorld():
    return "Hello World!"

@app.route('/', methods=['GET'])
def main_page():
    return "Main Page"

@app.route('/getList', methods=['GET'])
def get_list():
    return jsonify(movieList)

@app.route('/postList', methods=['POST'])
def update_list():
    newMovie = request.json
    movieList.append(newMovie)
    return jsonify(movieList)

# функция с передачей параметров через поиск в строке (+)

@app.route('/getPLus', methods=['GET'])
def get_Plus():
    var = int(request.args.get('var', 1))
    secondWord = int(request.args.get('desc', 1))
    y = int(var + secondWord)
    x = str(y)
    return x

# функция с передачей параметров через поиск в строке (-)

@app.route('/getMinus', methods=['GET'])
def get_Minus():
    var = int(request.args.get('var', 1))
    secondWord = int(request.args.get('desc', 1))
    y = int(var - secondWord)
    x = str(y)
    return x

# функция с передачей параметров через поиск в строке (*)

@app.route('/getMultipli', methods=['GET'])
def get_Multipli():
    var = int(request.args.get('var', 1))
    secondWord = int(request.args.get('desc', 1))
    y = int(var * secondWord)
    x = str(y)
    return x

#http://127.0.0.1:5000/getDiv?var=6&desc=4 пример ссылки
# функция с передачей параметров через поиск в строке (/%)

@app.route('/getDiv', methods=['GET'])
def get_Div():
    var = int(request.args.get('var', 1))
    secondWord = int(request.args.get('desc', 1))
    y = int(var / secondWord)
    g = int(var % secondWord)
    e = str(g)
    x = str(y)
    return "Деление без остатка: " + x + ", " + "остаток: " + e



if __name__ == '__main__':
    app.run()
