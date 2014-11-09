from flask import Flask, redirect, render_template, request, make_response, abort

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
@app.route('/<user>')
def display(user=None):
	d={}
	d["ig"]=[len(request.form["ig"])>1,request.form["ig"]]
	d["fb"]=[len(request.form["fb"])>1,request.form["fb"]]
	d["t"]=[len(request.form["t"])>1,request.form["t"]]
	d["sc"]=[len(request.form["sc"])>1,request.form["sc"]]
	d["gh"]=[len(request.form["gh"]),request.form["gh"]]
	d["ri"]=[len(request.form["ri"])>1,request.form["ri"]]
	for key in d:
		if d[key][0]:
			user=d[key][1]
			break
	if user:
		render_template("kaylee.html",user=user,dic=d)
	
if __name__ == "__main__":
    app.debug=True
    app.run()