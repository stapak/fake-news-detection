"""
Main file containg the backend of the module.
"""

from flask import Flask,render_template,Blueprint,request
from scraper import get_content,purifier
from flask_login import login_required,logout_user,login_user
from MLmodel import news_testing

app=Flask(__name__)
app.secret_key='asdofiqwoefroiqwejro231'

@app.route('/')
def home():
    return render_template('frontview.html')

@login_required
@app.route('/search',methods=["POST"])
def search():
    """
    Function used to get the link and call the api to collect json data.
    """
    link=request.form.get('link2')
    try:
        content=get_content(link)
    except Exception as e:
        return render_template('linknotsupported.html')
   
    try:
        result=news_testing(content)
    except Exception as e:
        print("Error:",e)
        return render_template('erroratbackend.html',Error=e)
    else:
        if result==1:
            return render_template('rightnews.html')
        else:
            return render_template('fakenews.html')


if __name__=='__main__':
    app.run(debug=True)
    #server.run()