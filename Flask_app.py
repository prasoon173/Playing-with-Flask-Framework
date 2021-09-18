from flask import Flask ,jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    message = 'Hey there! Welcome to my home page'
    return jsonify({'myresponse':message})

@app.route('/calculate', methods=['GET'])
def calculate():
    message = 'you are using calculate section here'
    return jsonify({'serversays': message})

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    message = 'Hello  ' + name
    return message

@app.route('/home/<int:num>', methods=['Get'])
def calculator(num):
    message = 'your no is :  ' + str(num)
    square = num*num
    cube = square*num
    message1= 'square of your no is:  ' + str(square)
    message2=  'cube of your no is:   '+str(cube)
    return jsonify({
        'number': message,
        'square':message1,
        'cube':message2
    })

#Using Array
Fruits=['apple','Mango','Banana','Lichi']
@app.route('/fruits',methods=['GET'])
def fruits():
    return jsonify({
        'myFruits':Fruits
    })

#Accepting value from user and then adding to our Fruits list
@app.route('/fruits/<string:fruit>',methods=['GET'])
def AddFruits(fruit):
    Fruits.append(fruit)
    return jsonify({
        'myFruits':Fruits
    })



if __name__ == '__main__':
    app.run(debug=True)
