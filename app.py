from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import boto3
from werkzeug.utils import secure_filename
 #source env/Scripts/activate  -- 
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'
 
db=SQLAlchemy(app)

BUCKET_NAME='srujansflaskbucket'
s3 = boto3.client('s3',
                    aws_access_key_id='ASIAYPIF54RQHC6QVCUL',
                    aws_secret_access_key= "ieA5jlhtaTFe0FWUfLQKFW8Dk8DML+TwO8gK3NNd",
                    aws_session_token="IQoJb3JpZ2luX2VjEBoaCmFwLXNvdXRoLTEiSDBGAiEAks07AxZKqC29aiyzw5MOQrZIhamVfeEvBRwvJUHojToCIQDosN7TQJ1/W5SHZgMqYwHb2kjG2jYZmitvxDrTJYzrlCr0AQij//////////8BEAAaDDU4MjUxNzM4NDI4OCIMN8/sOlBvM2OILze6KsgBKprIeB51ZoXmoE3jENdxjhSFzU7Iwj/vl5b+if9A966W550xca53x/707/ZIi68DBDx0/R9PAzhiUj8md5mT+WsRk+QC/396gjxL02qvPQqgKAFbzhy+c3OlXDlg4F8Kt7wtouvM8mDPKenRioFFep3zccYXR+LLDcj+5/RSq6jzGXD2HVNwKw7E6dFZm7KRZj/6QdvYh0ChRtSeg5sHqqqaGXsYvhBzHTxItiFpmCr39LsdEGI31Bi77u3HRkDdgi2f6CUpNY0w7Z+YnwY6lwHeS2CN1jG2frAh5ruoK4AkCdlgZ4bObNldEA0+/NBViz+ZDxV73untJUZlroLEl6sxndfLkmPdPTjneJf4sYJk7BwqifiYLxzLlYxM+p4AYOsab3+IfdyEKu+ZNems2hg9oknNkULKKty0PTGElcvDrMA4qFpFixqm7O5gZgWb0Qlf8UAJp3ps5SO6gqP3AzKvXqs5h4eN"
                     )  
 
@app.route('/')
def index():
  return render_template('index.html')
 


@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "File Uploaded  !"

    return render_template("index.html",msg =msg)
  
@app.route('/zipupload',methods=['post'])
def zip_upload():
    if request.method == 'POST':
        img = request.files.getlist('file')
        for file in img:
            if img:
                    filename = secure_filename(file.filename)
                    file.save(filename)
                    s3.upload_file(
                        Bucket = BUCKET_NAME,
                        Filename=filename,
                        Key = filename
                    )
                    zmsg = "Zip File Upload Done ! "

        return render_template("index.html",zmsg =zmsg)  
  
 

 
if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
 