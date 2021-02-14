import flask 
import pickle
import pandas as pd
import pickle
with open(f'model/model.pkl', 'rb') as f:
    model = pickle.load(f)
with open(f'model/model1.pkl', 'rb') as f:
    model_p = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates') 

app = flask.Flask(__name__, static_url_path='/static')
app.static_folder = 'static'


@app.route('/')
def hello_world():
    return(flask.render_template('index.html'))


@app.route('/test', methods=['GET', 'POST'])
def test():
    if flask.request.method == 'GET':
        return(flask.render_template('test.html'))
    if flask.request.method == 'POST':
        lump_hard = flask.request.form['lump_hard']
        swollen_area = flask.request.form['swollen_area']
        change_size= flask.request.form['change_size']
        discolouring= flask.request.form['discolouring']
        pain= flask.request.form['pain']
        nipple_inwards= flask.request.form['nipple_inwards']
        nipple_discharge=flask.request.form['nipple_discharge']
        increasing_weight= flask.request.form['increasing_weight']
        unhealthy_diet= flask.request.form['unhealthy_diet']
        not_exercise= flask.request.form['not_exercise']
        alcohol= flask.request.form['alcohol']
        exposure_estrogen= flask.request.form['exposure_estrogen']
        contraceptive=flask.request.form['contraceptive']
        stress= flask.request.form['stress']
        Age= flask.request.form['Age']
        Family_history= flask.request.form['Family_history']
        Personal_history= flask.request.form['Personal_history']
        Radiation= flask.request.form['Radiation']
        Pregnancy= flask.request.form['Pregnancy']

        
        
        input_variables = pd.DataFrame([[lump_hard, swollen_area, change_size,discolouring,pain,nipple_inwards,nipple_discharge,increasing_weight,unhealthy_diet,not_exercise,alcohol,exposure_estrogen,contraceptive,stress,Age,Family_history,Personal_history,Radiation,Pregnancy]],
                                       columns=['lump_hard', 'swollen_area', 'change_size','discolouring','pain','nipple_inwards','nipple_discharge','increasing_weight','unhealthy_diet','not_exercise','alcohol','exposure_estrogen','contraceptive','stress','Age','Family_history','Personal_history','Radiation','Pregnancy'],
                                       dtype=float)
        prediction = model.predict(input_variables)[0]
        return flask.render_template('test.html',
                                     original_input={'lump_hard':lump_hard,
                                                     'swollen_area':swollen_area,
                                                     'change_size':change_size,
                                                     'discolouring':discolouring,
                                                     'pain':pain,
                                                     'nipple_inwards':nipple_inwards,
                                                     'nipple_discharge':nipple_discharge,
                                                     'increasing_weight':increasing_weight,
                                                     'unhealthy_diet':unhealthy_diet,
                                                     'not_exercise':not_exercise,
                                                     'alcohol':alcohol,
                                                     'exposure_estrogen':exposure_estrogen,
                                                     'contraceptive':contraceptive,
                                                     'stress':stress,
                                                     'Age':Age,
                                                     'Family_history':Family_history,
                                                     'Personal_history':Personal_history,
                                                     'Radiation':Radiation,
                                                     'Pregnancy':Pregnancy
                                                     
                                                     },
                                     result=prediction,
                                     )

@app.route('/test1', methods=['GET', 'POST'])
def test1():
    if flask.request.method == 'GET':
        return(flask.render_template('test.html'))
    if flask.request.method == 'POST':
        age = flask.request.form['age']
        pregnant = flask.request.form['pregnant']
        aborptions= flask.request.form['aborptions']
        Bloated= flask.request.form['Bloated']
        facial_hair= flask.request.form['facial_hair']
        chest_hair= flask.request.form['chest_hair']
        obesity=flask.request.form['obesity']
        mood_swings= flask.request.form['mood_swings']
        stress= flask.request.form['stress']
        Irregular_sleep= flask.request.form['Irregular_sleep']
        Weight_gain= flask.request.form['Weight_gain']
        hair_growth= flask.request.form['hair_growth']
        Skin_darkening=flask.request.form['Skin_darkening']
        Hair_loss= flask.request.form['Hair_loss']
        Pimples= flask.request.form['Pimples']
        Fast_food= flask.request.form['Fast_food']
        Reg_Exercise= flask.request.form['Reg_Exercise']
        Weight= flask.request.form['Weight']
        Height= flask.request.form['Height']
        BMI= flask.request.form['BMI']
        Blood_Group= flask.request.form['Blood_Group']
        Pulse_rate= flask.request.form['Pulse_rate']
        Cycle_months= flask.request.form['Cycle_months']
        Cycle_length= flask.request.form['Cycle_length']
        Marriage_Status= flask.request.form['Marriage_Status']
        Hip= flask.request.form['Hip']
        Waist= flask.request.form['Waist']
        whratio= flask.request.form['whratio']



        
        
        input_variables = pd.DataFrame([[age,pregnant,aborptions,Bloated,facial_hair,chest_hair,obesity,mood_swings,stress,Irregular_sleep,Weight_gain,hair_growth,Skin_darkening,Hair_loss,Pimples,Fast_food,Reg_Exercise,Weight,Height,BMI,Blood_Group,Pulse_rate,Cycle_months,Cycle_length,Marriage_Status,Hip,Waist,whratio]],
                                       columns=['age', 'pregnant','aborptions','Bloated','facial_hair','chest_hair','obesity','mood_swings', 'stress','Irregular_sleep','Weight_gain','hair_growth','Skin_darkening','Hair_loss','Pimples','Fast_food','Reg_Exercise','Weight','Height','BMI','Blood_Group','Pulse_rate','Cycle_months','Cycle_length','Marriage_Status','Hip','Waist','whratio'],
                                       dtype=float)
        prediction = model_p.predict(input_variables)[0]
        return flask.render_template('test1.html',
                                     
                                                     
                                                    
                                     result=prediction,
                                     )
