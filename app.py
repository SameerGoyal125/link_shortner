from flask import *
from pandas import *
from random import choice

al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        sht = ""
        taken = 0
        data = pandas.read_csv("urls.csv")
        shrt = data["short"].tolist()
        if request.form['special']:
            if request.form['special'] in shrt:
                taken = 1
            else:
                sht = request.form['special']
        else:
            for x in range(0, 2):
                sht += str(choice(al))
                sht += str(choice(num))
        if taken == 0:
            shorturl = {
                'short': [sht],
                'urls': [request.form['url']]
            }
            df = pandas.DataFrame(shorturl)
            df.to_csv('urls.csv', mode='a', index=False, header=False)
            sgh = "Your link is " + sht
        else:
            sgh = request.form['special'] + " is already taken"
        return render_template('index.html', short=sgh)
    return render_template('index.html')


@app.route('/<search>')
def user(search):
    data = pandas.read_csv("urls.csv")
    shrt = data["short"].tolist()
    if search in shrt:
        return redirect(data[data["short"] == search]["urls"].to_string(index=False))
    else:
        return "Not Found"


if __name__ == '__main__':
    app.run(debug=True)
