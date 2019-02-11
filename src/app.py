# -*- coding: utf-8 -*-

from flask import Flask,render_template,request  
import search_engine                                     
app = Flask(__name__, template_folder='templates') 

@app.route('/',methods=["GET","POST"])   # link 127.0.0.1:5000/ 
def search(): 
	result=[]   
	word =""
	if request.method == "POST":  
		word = request.form.get("search")  
		index, graph = search_engine.crawl_web('http://www.hurriyet.com.tr/')  #crawl fonction index
		ranks = search_engine.compute_ranks(graph) #compute url ranks
		result = search_engine.keyword_search(index, ranks, str(word)) 
		if result :
			pass
		else:
			result=[]
	return render_template("search.html",result=result,word=word)  

if __name__ == '__main__':
   app.run(debug=True)