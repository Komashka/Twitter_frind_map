from flask import Flask, render_template, request
import folium
from friend_map import map_formation

myMap = folium.Map()
app = Flask(__name__)
app.secret_key = "hi"


@app.route('/')
def main():
    return render_template('index.html')


@app.route("/info_return", methods=['POST', 'GET'])
def info_return():
    twi = str(request.args.get('account'))
    fg = map_formation(twi)
    myMap.add_child(fg)
    myMap.add_child(folium.LayerControl())
    myMap.save("myMap.html")
    return render_template('myMap.html')


if __name__ == "__main__":
    app.run(debug=True)
