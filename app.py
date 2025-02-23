from flask import(
    Flask,
    redirect,
    render_template,
    request
)
app = Flask(__name__)

product = {}

@app.route('/', methods=['GET','POST'])
def get_main():
    if request.method == 'POST':
        title = request.form.get('title', type=str)
        price = request.form.get('price', type=int)
        if title and price:
            product[title] = price
        return render_template('index.html', product =product)
    return render_template('index.html', product =product)

@app.route('/log', methods=['GET','POST'])
def get_log():

    return render_template('log.html')

@app.route('/reg', methods=['GET','POST'])
def get_reg():

    return render_template('reg.html')




if __name__ == '__main__':
    app.run(debug=True)

# сделать что бы ваши объявления все выходили в отдельном диве и шли рядом друг с другом 
# если хватит сил  сделать кнопку удалить все объявления
# На дизайном сильно не парьтес