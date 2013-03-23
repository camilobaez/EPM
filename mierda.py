from flask import Flask
app = Flask (__name__)
app.debug= True
@app.route("/")
def hello():
<<<<<<< HEAD
	return "camilonicolas"
=======
	return "camilobaez"
>>>>>>> branch 'master' of https://github.com/camilobaez/EPM.git
if __name__ == "__main__":
	app.run()
