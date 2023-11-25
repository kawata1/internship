from flask import Flask, request, jsonify

app = Flask(__name__)

passes = []


@app.route('/passes', methods=['GET'])
def get_passes():
    return jsonify(passes)


@app.route('/passes', methods=['POST'])
def add_pass():
    data = request.get_json()
    name = data['name']
    height = data['height']
    coordinates = data['coordinates']
    description = data['description']

    new_pass = Pass(name, height, coordinates, description)
    passes.append(new_pass)

    return jsonify({'message': 'Перевал успешно добавлен'})


if __name__ == '__main__':
    app.run()
