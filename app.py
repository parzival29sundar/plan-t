from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import InputRequired, Length, ValidationError, Email
from flask_bcrypt import Bcrypt
from markupsafe import Markup

import numpy as np
import pandas as pd
import sklearn
import pickle
import config
import io
import torch
from torchvision import transforms

from PIL import Image
from utils.model import ResNet9

from utils.data import crop_idx, crop_url, fertilizer_data

from utils.disease import disease_dic
# from utils.fertilizer import fertilizer_dic


disease_classes = ['Apple___Apple_scab',
                   'Apple___Black_rot',
                   'Apple___Cedar_apple_rust',
                   'Apple___healthy',
                   'Blueberry___healthy',
                   'Cherry_(including_sour)___Powdery_mildew',
                   'Cherry_(including_sour)___healthy',
                   'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                   'Corn_(maize)___Common_rust_',
                   'Corn_(maize)___Northern_Leaf_Blight',
                   'Corn_(maize)___healthy',
                   'Grape___Black_rot',
                   'Grape___Esca_(Black_Measles)',
                   'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                   'Grape___healthy',
                   'Orange___Haunglongbing_(Citrus_greening)',
                   'Peach___Bacterial_spot',
                   'Peach___healthy',
                   'Pepper,_bell___Bacterial_spot',
                   'Pepper,_bell___healthy',
                   'Potato___Early_blight',
                   'Potato___Late_blight',
                   'Potato___healthy',
                   'Raspberry___healthy',
                   'Soybean___healthy',
                   'Squash___Powdery_mildew',
                   'Strawberry___Leaf_scorch',
                   'Strawberry___healthy',
                   'Tomato___Bacterial_spot',
                   'Tomato___Early_blight',
                   'Tomato___Late_blight',
                   'Tomato___Leaf_Mold',
                   'Tomato___Septoria_leaf_spot',
                   'Tomato___Spider_mites Two-spotted_spider_mite',
                   'Tomato___Target_Spot',
                   'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
                   'Tomato___Tomato_mosaic_virus',
                   'Tomato___healthy']

disease_model_path = 'models/plant_disease_model.pth'
disease_model = ResNet9(3, len(disease_classes))
disease_model.load_state_dict(torch.load(
    disease_model_path, map_location=torch.device('cpu')))
disease_model.eval()






crops_model = pickle.load(open('./models/crops.pkl', 'rb'))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'Flasky123@'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"





@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = 1)
    name = db.Column(db.String(80), nullable = 0)
    email = db.Column(db.String(80), nullable = 0, unique = 1)
    password = db.Column(db.String(80), nullable = 0)


class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Length(min=4, max=40), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    name = HiddenField(id="fullname")
    email = StringField(validators=[InputRequired(), Length(min=4, max=40), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    def validate_email(self, email):
        user_exists = User.query.filter_by(email = email.data).first()
        if user_exists: raise ValidationError("email already taken.")


def predict_image(img, model=disease_model):
    """
    Transforms image to tensor and predicts disease label
    :params: image
    :return: prediction (string)
    """
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.ToTensor(),
    ])
    image = Image.open(io.BytesIO(img))
    img_t = transform(image)
    img_u = torch.unsqueeze(img_t, 0)

    # Get predictions from model
    yb = model(img_u)
    # Pick index with highest probability
    _, preds = torch.max(yb, dim=1)
    prediction = disease_classes[preds[0].item()]
    # Retrieve the class label
    return prediction



@app.route('/')
def homepage():  
    lang = 'English' if request.args.get('lang') == None else request.args.get('lang')
    return render_template('index.html', lang = lang)


@app.route('/crops')
def crops():
    lang = 'English' if request.args.get('lang') == None else request.args.get('lang')
    return render_template('crops.html', lang = lang)


@app.route('/fertilizers')
def fertilizers():
    lang = 'English' if request.args.get('lang') == None else request.args.get('lang')
    return render_template('fertilizers.html', lang = lang)


# @app.route('/disease')
# def disease():
#     lang = 'English' if request.args.get('lang') == None else request.args.get('lang')
#     return render_template('disease.html', lang = lang)



@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = RegistrationForm()

    lang = 'English' if request.args.get('lang') == None else request.args.get('lang')

    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data)
        new_user = User(name = form.name.data, email = form.email.data, password = hashed_pwd)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')

    return render_template('signup.html', form = form, lang = lang)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    lang = 'English' if request.args.get('lang') == None else request.args.get('lang')

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect('/')

    return render_template('login.html', form = form, lang = lang)


@app.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/dashboard', methods = ['GET', 'POST'])
@login_required
def user():
    lang = 'English' if request.args.get('lang') == None else request.args.get('lang')
    return render_template("dashboard.html", lang = lang)






@app.route('/cropsResult', methods = ['POST'])
def cropsResult():
    lang = 'English' if request.args.get('lang') == None else request.args.get('lang')

    if request.method == 'POST':
        n = float(request.form['nitrogen'])
        p = float(request.form['phosphorus'])
        k = float(request.form['potassium'])
        temp = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['rainfall'])

        features = np.array([[n, p, k, temp, humidity, ph, rainfall]])
        predict = crops_model.predict(features)

        # print("crop prediction")
        # print("-------------------------------")
        # print("input data -> ", features[0])
        
        if len(predict) > 0:
            res = []
            res_url = []
            for i in predict: 
                res.append(crop_idx[i])
                res_url.append(crop_url[crop_idx[i]])

            # print("Output -> ", res)
            # print("-------------------------------")
            return render_template('crops.html', result = True, data = [res, res_url], lang = lang)
        else:
            return render_template('crops.html', result = True, data = "-1", lang = lang)

    return render_template('crops.html', result = False, lang = lang)


@app.route('/fertilizersRequired', methods = ['GET', 'POST'])
def requiredFertilizers():

    lang = 'English' if request.args.get('lang') == None else request.args.get('lang')

    if request.method == 'POST':
        n = int(request.form['nitrogen'])
        p = int(request.form['phosphorus'])
        k = int(request.form['potassium'])
        crop = request.form['cropName']

        fert = pd.read_csv('./data/fertilizer.csv')

        nitro = fert[fert['Crop'] == crop]['N'].iloc[0]
        phos = fert[fert['Crop'] == crop]['P'].iloc[0]
        pota = fert[fert['Crop'] == crop]['K'].iloc[0]

        n = abs(nitro - n)
        p = abs(phos - p)
        k = abs(pota - k)

        data = {
            n : "N",
            p : "P",
            k : "K"
        }

        maxx = data[max(data.keys())]

        # if maxx == "N":
        #     if n < 0: key = 'NHigh'
        #     else: key = "Nlow"
        # elif maxx == "P":
        #     if p < 0: key = 'PHigh'
        #     else: key = "Plow"
        # else: 
        #     if k < 0: key = 'KHigh'
        #     else: key = "Klow"
        maxx = data[max(data.keys())]

        if maxx == "N":
            if n < 0: key = 'Nlow'  # Corrected to 'Nlow'
            else: key = "NHigh"      # Corrected to 'NHigh'
        elif maxx == "P":
            if p < 0: key = 'Plow'   # Corrected to 'Plow'
            else: key = "PHigh"      # Corrected to 'PHigh'
        else: 
            if k < 0: key = 'Klow'   # Corrected to 'Klow'
            else: key = "KHigh"      # Corrected to 'KHigh'


        response = Markup(str(fertilizer_data[key]))

        return render_template('fertilizers.html', result = True, data = response, lang = lang)
    
    return render_template('fertilizers.html', result = False, lang = lang)




@app.route('/disease', methods=['GET', 'POST'])
def disease_prediction():
    lang = 'English' if request.args.get('lang') == None else request.args.get('lang')
    

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return render_template('diseases.html', lang=lang)
        # try:
        img = file.read()

        prediction = predict_image(img)

        prediction = Markup(str(disease_dic[prediction]))

        return render_template('disease-result.html', prediction=prediction , lang=lang)
        # except:
        #     pass
    return render_template('diseases.html' , lang=lang)


if __name__ == "__main__" : app.run(debug=True, port=3000)