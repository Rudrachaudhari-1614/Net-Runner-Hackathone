from flask import Flask, render_template, request, flash, session, redirect
from fileinput import filename 
from werkzeug.utils import secure_filename
import os.path
import database
import time
import math


app = Flask(__name__)
app.secret_key = 'abcdefghi#123'

@app.route('/')
def home():
    return render_template('index.html')

UPLOAD_FOLDER = "resumes/"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg','docx', 'tiff', 'tex'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/file_upload', methods=['POST'])
def file_upload():
    if request.method == 'POST':   
        exts = ['txt', 'pdf', 'png', 'jpg', 'jpeg','docx', 'tiff', 'tex']

        name = request.form['Name']
        email = request.form['Email']

        if 'file' not in request.files:
            flash('No file part')
            return redirect('/')
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect('/')
        if file:
            x = file.filename[file.filename.index('.'):]
            filename = secure_filename(file.filename)
            x = x[::-1]
            x = file.filename[(len(file.filename)-x.index('.')-1):]
            """if x not in exts:
                flash('Please upload document of specified formats: .txt,.pdf,.png,.jpg,.jpeg','error')
                return redirect('/')"""

            res_path = f"resumes/{name}{x}" 
            
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], f"{name}{x}")) 
          
            
    
        database.input(name,email,res_path,file.filename)
        return render_template('Thanks.html')
@app.route('/applicant/<email>/<name>')
def applicant(email, name):
    emaill = str(email)
    file1 = open(f"llm_answer/{name}-0.txt", 'r')
    file2 = open(f"llm_answer/{name}-1.txt", 'r')
    file3 = open(f"llm_answer/{name}-2.txt", 'r')
    file4 = open(f"llm_answer/{name}-3.txt", 'r')
    file5 = open(f"llm_answer/{name}-4.txt", 'r')
    edu = file1.read()
    wex = file2.read()
    proj = file3.read()
    ct = file4.read()
    jt = file5.read()
    
    data = database.Database_common_operations.run_query_and_return_all_data(f"select * from Master where email = '{email}';")

    return render_template('applicant.html', edu = edu, wex = wex, proj = proj, ct = ct, jt = jt, data = data[0])

@app.route('/job_applicants/<j_id>')
def job_applicants(j_id):
    print(j_id)
    data = database.Database_common_operations.run_query_and_return_all_data("select * from Master;")
    print(data)
    return render_template('job_ap.html', data = data)

@app.route('/add_job')
def add_job():
    return render_template('add_job.html')

@app.route('/add_job_action', methods=['POST'])
def add_job_action():
    if request.method == "POST":
        jname = request.form['jobName']
        jdes = request.form['jobDes']
        s_id = database.add_job(jname,jdes,'-')
        data = database.get_all_skills()
        return render_template('add_skills.html', s_id = s_id, data = data)
        

@app.route('/add_skill_action', methods=['POST'])
def add_skill_action():
    skillss = request.form.getlist('skills')
    str_f = ""
    for i in skillss:
        str_f = f"{str_f},{i}"
    print(str_f)
    j_id = request.form.get('j_id')
    print(skillss)
    database.Database_common_operations.run_query(f"UPDATE Job set Req = '{str_f}' where JobId = '{j_id}';")
    return redirect('/admin')

@app.route('/add_new_skill', methods=['POST'])
def add_new_skill():
    print("hello there!!")
    if request.method == 'POST':
        skill = request.form['skilll']
        database.add_skill(skill)
        j_id = request.form.get('j_idd')
        data = database.get_all_skills()
        return render_template('add_skills.html', s_id = j_id, data = data)

@app.route('/delete_job/<j_id>')
def delete_job(j_id):
    database.Database_common_operations.run_query(f"delete from Job where JobID = '{j_id}';")
    return redirect('/admin')

@app.route('/admin')
def admin():
    data = database.get_jobs()
    return render_template('admin.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)