from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def home():
    return "This is Home page"

@app.route("/prime")
def cal_prime():
    num = request.json["num"]
    l1 =[]
    for i in range(2,num+1):
        if num > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                l1.append(i)

    return str(l1)

if __name__ == "__main__":
    app.run(debug=True)