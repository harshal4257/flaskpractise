from flask import Flask,request,render_template,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "This is Home page"

@app.route("/prime",methods = ["GET","POST"])
def cal_prime():
    if request.method == "GET":
        return render_template('form.html')
    else:
        num = request.form['num']
        int(num)
        l1 =[]
        for i in range(2,int(num)+1):
            if int(num) > 1:
                for j in range(2,i):
                    if i % j == 0:
                        break
                else:
                    l1.append(i)

    return render_template("result.html",n1 = num,no = l1)

if __name__ == "__main__":
    app.run(debug=True)