from flask import Flask, render_template, request, redirect, jsonify
import google.generativeai as genai

key = "" #ENTER YOUR GOOGLE API KEY HERE
app = Flask(__name__)

genai.configure(api_key=key)

model = genai.GenerativeModel('gemini-1.5-flash')

google = model.start_chat(history = [])

@app.route("/", methods = ["GET","POST"])
def main():
    global google
    google = model.start_chat(history = [])
    return render_template("index.html")


@app.route("/chat",methods = ["POST"])
def chat():
    
    data = request.json
    reply = google.send_message(data['prompt'])
    ret = {}
    ret['prompt'] = data['prompt']
    ret['resp'] = reply.text
    return jsonify(ret)

if __name__ == "__main__" :
    app.run(debug=False)
