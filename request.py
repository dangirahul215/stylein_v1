from flask import Flask, request, jsonify
from recommendation_v1 import *

app = Flask(__name__)

#from recommendation
frame = read_all_files()
node = Operation(frame)
node.algo()
#print(node.recommended_products_similar(prod_id=9786234))
#print(node.recommended_products_pair_with(9786234))


@app.route('/recommendation', methods=['GET'])
def post_route():
    if request.method == 'GET':
        data = request.get_json(force=True)
        # print('Data Received: "{data}"'.format(data=data))
        # return ("Data without stop words---%s \n "% without_stop_words(data['sample_data']))
        #return jsonify(Data_without_stop_words=without_stop_words(data['sample_data']))
        return jsonify(Similar_products=node.recommended_products_similar(int(data['id'])),Pair_with=node.recommended_products_pair_with(int(data['id'])))

@app.route("/")
def hello():
    return "hello your app is runnning okay"


app.run(host="0.0.0.0")