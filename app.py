from flask import Flask , render_template, request

from Gun_ViolenceRisk import predicting_algo

app = Flask(__name__)




@app.route('/', methods=['POST'])
def my_form_post():

	address = request.form['Address']
	month = str(request.form['Month'])
	weekday = str(request.form['WeekDay'])
	# address = "7600 oakdale street massillon ohio 44646"
	# month = "May"
	# weekday = "sunday"
	# city = "massillon"
	city = request.form['City']
	month = month.lower()
	weekday = weekday.lower()

	if "janurary" in month:
		month = 1
	elif "feburary" in month:
		month = 2
	elif "march" in month:
		month = 3
	elif "april" in month:
		month = 4
	elif "may" in month:
		month =5
	elif "june" in month:
		month = 6
	elif "july" in month:
		month = 7
	elif "august" in month:
		month = 8
	elif "september" in month:
		month = 9
	elif "october" in month:
		month = 10
	elif "november" in month:
		month = 11
	elif "december" in month:
		month = 12

	if "sunday" in weekday:
		weekday =0
	elif "saturday" in weekday:
		weekday= 0
	else:
		weekday = 1

	toReturn = ""

	month = str(month)
	weekday = str(weekday)

	toReturn = address +"|"+month+"|"+weekday+"|"+city
	
	
	return render_template('home.html',result="%0.2f"% predicting_algo(toReturn) +'%')

@app.route('/', methods = ["GET"])
def index():
		
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	#debug mode app.run()
	app.run(debug=True)
