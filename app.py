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
        if 'delete' in request.form:
            product.clear()
        else:
            title = request.form.get('title', type=str)
            price = request.form.get('price', type=int)
            if title and price:
                product[title] = price
    return redirect('index.html', product=product)


@app.route('/delete', methods=['POST'])
def delete():
    product.clear()
    return render_template('index.html')

@app.route('/log', methods=['GET','POST'])
def get_log():

    return render_template('log.html')

@app.route('/reg', methods=['GET','POST'])
def get_reg():

    return render_template('reg.html')




if __name__ == '__main__':
    app.run(debug=True)

