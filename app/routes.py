from flask import Flask, render_template, request, redirect, flash

from app import app

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'Post':
        first_name = request.form ['first_name']
        last_name = request.form ['last_name']
        phone_number = request.form ['phone_number']
        address = request.form['address']

        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Phonw Number: {phone_number} ")
        print(f"Address: {address}")

        flash("Information submitted successfully")

        return redirect('/')
    
    return render_template("form.html", form = form)

if __name__ == '__main__':
    app.run(debug=True)
