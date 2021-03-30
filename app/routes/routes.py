from app import app, render_template

from app.models.formsModel import InputDataForm


@app.route('/')
def index():
    form = InputDataForm();
    return render_template('index.html', form=form)