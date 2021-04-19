from app import app, render_template, redirect, url_for, request

from app.models.formsModel import InputDataForm

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/', methods=["GET","POST"])
def index():
    form = InputDataForm()

    if form.validate_on_submit():
        print(form)
    else:
        print(form.errors)

    return render_template('index.html', form=form)
  

