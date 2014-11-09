from flask import Flask, redirect, render_template, request, make_response, abort
import facebook,insta,github,reddit,soundCloud,twitter
app = Flask(__name__)
app.config.from_object(__name__)

#@app.route('/',methods="POST")
@app.route('/<user>',methods="POST")
def display(user=None):
	d={}
	d["IG"]=[len(request.form["IG"])>1,request.form["IG"]]
	d["FB"]=[len(request.form["FB"])>1,request.form["FB"]]
	d["T"]=[len(request.form["T"])>1,request.form["T"]]
	d["SC"]=[len(request.form["SC"])>1,request.form["SC"]]
	d["GH"]=[len(request.form["GH"]),request.form["GH"]]
	d["RI"]=[len(request.form["RI"])>1,request.form["RI"]]
	for key in d:
		if d[key][0]:
			user=d[key][1]
			break
	if d["IG"][0]:
		d["IG"]+=insta.getAll(d["IG"][1])

	if d["FB"][0]:
		d["FB"]+=facbook.getAll(d["FB"][1])
	
	if d["T"][0]:
		d["T"]+=twitter.getAll(d["T"][1])
	
	if d["SC"][0]:
		d["SC"]+=soundCloud.getAll(d["SC"][1])
	
	if d["GH"][0]:
		d["GH"]+=github.getAll(d["GH"][1])
	
	if d["RI"][0]:
		d["RI"]+=reddit.getAll(d["RI"][1])
				
	if user:
		return render_template("kaylee.html",user=user,dic=d)
	else:
		return render_template("index.html")
	
if __name__ == "__main__":
    app.debug=True
    app.run()