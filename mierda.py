from flask import Flask
app = Flask (__name__)
app.debug= True
@app.route("/")
def hello():
	return "camilooiuoiuoiu"
if __name__ == "__main__":
	app.run()
