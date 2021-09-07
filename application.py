from types import new_class
from flask import Flask,render_template,request,redirect,url_for
from enumclass import ProjectAchievement
from database import db, init_db
from models import Data, MasterKosen

# アプリケーションの初期化を行います
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret"
    db_uri = 'sqlite:///data.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    init_db(app)

    return app

app = create_app()

#トップページ
@app.route('/',methods=['GET','POST'])
def index():
  if request.method=="GET":
    posts=Data.query.all()
    kosen_list=MasterKosen.get_school_list()
    return render_template('index.html',posts=posts,menue=ProjectAchievement,kosen_list=kosen_list)

#登録フォーム
@app.route('/entry', methods=['GET','POST'])
def entry():
  if request.method=="POST":
    classification = request.form.get("classification")
    author = request.form.get("author")
    title = request.form.get("title")
    contents = request.form.get("contents")
    #辞書で渡す
    return render_template('entry2.html',classification=classification,author=author,title=title,contents=contents)
  else:
    return render_template("entry.html")

#トップページからの変更フォーム
@app.route('/entry/<int:id>', methods=['GET','POST'])
def entry3(id):
  post=Data.query.get(id)
  return render_template("entry3.html",post=post)
  
#登録処理
@app.route('/regist',methods=["POST"])
def regist():
  classification = request.form.get("classification")
  author = request.form.get("author")
  title = request.form.get("title")
  contents = request.form.get("contents")
  new_post=Data(classification=classification,author=author,title=title,contents=contents)

  db.session.add(new_post)
  db.session.commit()
  return render_template('detail2.html',classification=classification,author=author,title=title,contents=contents)

#登録確認画面
@app.route('/confirm',methods=['POST'])
def confirm():
  classification = request.form.get("classification")
  author = request.form.get("author")
  title = request.form.get("title")
  contents = request.form.get("contents")
  return render_template('confirm.html',classification=classification,author=author,title=title,contents=contents)

#トップページからの詳細画面
@app.route('/detail/<int:id>',methods=["GET","POST"])
def detail(id):
  post=Data.query.get(id)
  return render_template('detail.html',post=post)

@app.route('/delete/<int:id>')
def delete(id):
    post=Data.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
