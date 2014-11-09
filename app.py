from flask import Flask, redirect, render_template, request, make_response, abort
import facebook,insta,github,reddit,soundCloud,twitter
app = Flask(__name__)
app.config.from_object(__name__)

import os
@app.route('/js/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('js', "."))

@app.route('/',methods=["GET","POST"])

#@app.route('/<user>',methods=["GET","POST"])
def display(user=None):
	if request.method=="GET":
		return render_template("index.html")
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
	if not user:
		return render_template("index.html")
	if d["IG"][0]:
		d["IG"]+=[insta.getAll(d["IG"][1])]

	if d["FB"][0]:
		d["FB"]+=[facebook.getAll(d["FB"][1])]
	
	if d["T"][0]:
		d["T"]+=[twitter.getAll(d["T"][1])]
	
	if d["SC"][0]:
		d["SC"]+=[soundCloud.getAll(d["SC"][1])]
	
	if d["GH"][0]:
		d["GH"]+=[github.getAll(d["GH"][1])]
	
	if d["RI"][0]:
		d["RI"]+=[reddit.getAll(d["RI"][1])]
				
	if user:
		return render_template("Kaylee.html",user=user,dic=d)


@app.route('/help',methods=["GET","POST"])
def help():
	print "hey"
	d={}

	d["IG"]=[len(request.form["IG"])>1,request.form["IG"]]
	print "yo"
	d["FB"]=[request.form["FB"]!=None,request.form["FB"]]
	d["T"]=[len(request.form["T"])>1,request.form["T"]]
	d["SC"]=[len(request.form["SC"])>1,request.form["SC"]]
	d["GH"]=[len(request.form["GH"]),request.form["GH"]]
	d["RI"]=[len(request.form["RI"])>1,request.form["RI"]]
	for key in d:
		if d[key][0]:
			user=d[key][1]
			break
	if not user:
		return render_template("index.html")
	if d["IG"][0]:
		d["IG"]+=[insta.getAll(d["IG"][1])]

	if d["FB"][0]:
		d["FB"]+=[facebook.getAll(d["FB"][1])]
	
	if d["T"][0]:
		d["T"]+=[twitter.getAll(d["T"][1])]
	
	if d["SC"][0]:
		d["SC"]+=[soundCloud.getAll(d["SC"][1])]
	
	if d["GH"][0]:
		d["GH"]+=[github.getAll(d["GH"][1])]
	
	if d["RI"][0]:
		d["RI"]+=[reddit.getAll(d["RI"][1])]
	return render_template("Kaylee.html",user=user,dic=d)


	
if __name__ == "__main__":
    app.debug=True
    app.run()