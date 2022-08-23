from flask import Flask,render_template,request,redirect,url_for
from urllib import request as request2
import os
from fontTools import ttLib
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/search-font", methods = ['POST', 'GET'])
def searchFont():
    if request.method=='POST':
        url = request.form['url']
        URL = url
        print(URL)

        # Request byte_data from the server:
        req = request2.Request(URL) #create request object
        req.add_header('User-Agent', 'Mozilla/5.0') #add header to the request object.
        reqConn = request2.urlopen(req) #send request to the server and receive response(byte_object).
        byteData = reqConn.read() # read response byte_data and end the connection.(return object holding byte data.)

        # Create new_file to write those response byte_data into new_file in binary formate:
        folderPath = './static'
        fileName = URL.split('/')[-1]
        filepath = os.path.join(folderPath,fileName)
        file = open(filepath, 'wb')
        file.write(byteData) #open file(binary formate) to write.(create specific file if not exist.)
        file.close()
        # Till now file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2) is created.

        # Manipulating fonts of file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2).(fontTools is a library written in Python, for manipulating font files.)
        font = ttLib.TTFont(filepath) #load an existing font_file(4cadb55f-822a-4a35-8918-becfc5a866a3.woff2).
        fontData1 = []

        for i in range(0,20):
            fontData1.append(font['name'].getDebugName(i))
        
        return fontData1
    return render_template('search-font.html')



# @app.route("/process-fontdetial/<url>")
# def processFontDetial(url):
#     # URL = 'https://www.swinton.co.uk/ResourcePackages/Swinton/assets/fonts/4cadb55f-822a-4a35-8918-becfc5a866a3.woff2'
    
#     # return redirect(url_for("fontDetial", fontData={'fontData1':fontData1}))



# @app.route("/font-detial/<fontData>")
# def fontDetial(fontData):
#     # return render_template('font-detial.html')
#     return 'Font Data: %s' % fontData.fontData1


if __name__ == "__main__":
    app.run(debug=True,port=8000)