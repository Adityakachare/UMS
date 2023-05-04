from flask import Flask, render_template, request, redirect, url_for, session
import os
import smtplib
import ssl
import mysql.connector
from email.message import EmailMessage


# MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aditya@27",
    database="registration",
    auth_plugin='caching_sha2_password'
)
mycursor = mydb.cursor()

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/staff')
def staff():
    return render_template('staff.html')

@app.route("/login")
def login1():
    return render_template("login.html")


# login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        mail = request.form["mail"]
        pwd = request.form["pwd"]

        # query the appropriate tables
        mycursor.execute("SELECT * FROM new_teacher WHERE mail=%s AND pwd=%s", (mail, pwd))
        teacher = mycursor.fetchone()
        mycursor.execute("SELECT * FROM new_student WHERE mail=%s AND pwd=%s", (mail, pwd))
        student = mycursor.fetchone()
        mycursor.execute("SELECT * FROM principle WHERE mail=%s AND pwd=%s", (mail, pwd))
        principal = mycursor.fetchone()

        # if user exists, set up a session
        if teacher:
            session["mail"] = mail
            session["role"] = "teacher"
            return redirect("/teacher")
        elif student:
            session["mail"] = mail
            session["role"] = "student"
            return redirect("/student")
        elif principal:
            session["mail"] = mail
            session["role"] = "principal"
            return redirect("/principal")

    return render_template("login.html")

# teacher route
@app.route("/teacher")
def teacher():
    if "mail" in session and session["role"] == "teacher":
        mail = session["mail"]
        mycursor.execute("SELECT name FROM new_teacher WHERE mail=%s", (mail,))
        name = mycursor.fetchone()[0]
        return render_template("teacher/thome.html", name=name, mail=mail)
    else:
        return redirect("/login")

# student route
@app.route("/student")
def student():
    if "mail" in session and session["role"] == "student":
        mail = session["mail"]
        mycursor.execute("SELECT name FROM new_student WHERE mail=%s", (mail,))
        name = mycursor.fetchone()[0]
        return render_template("student/sthome.html", name=name, mail=mail)
    else:
        return redirect("/login")
    

    
#principal route
@app.route("/principal")
def principal():
    if "mail" in session and session["role"] == "principal":
        mail = session["mail"]
        mycursor.execute("SELECT name FROM principle WHERE mail=%s", (mail,))
        name = mycursor.fetchone()[0]
        return render_template("principal/phome.html", name=name, mail=mail)
    else:
        return redirect("/login")
    
@app.route('/pprofile')
def pprofile():
    if "mail" in session and session["role"] == "principal":
        mail = session["mail"]
        mycursor.execute("SELECT name,eid,addr,phn,dob FROM principle WHERE mail=%s", (mail,))
        result = mycursor.fetchone()
        if result:
            name,eid,addr,phn,dob = result
            return render_template("principal/pprofile.html", name=name, mail=mail, eid=eid, addr=addr, phn=phn, dob=dob)
        else:
            return redirect("/login")
        
@app.route('/tprofile')
def tprofile():
    if "mail" in session and session["role"] == "teacher":
        mail = session["mail"]
        mycursor.execute("SELECT name,eid,addr,phn,dob,field,branch FROM new_teacher WHERE mail=%s", (mail,))
        result = mycursor.fetchone()
        if result:
            name,eid,addr,phn,dob,branch,field = result
            return render_template("teacher/tprofile.html", name=name, mail=mail, eid=eid, addr=addr, phn=phn, dob=dob,branch=branch,field=field)
        else:
            return redirect("/login")
        
@app.route('/stprofile')
def stprofile():
    if "mail" in session and session["role"] == "student":
        mail = session["mail"]
        mycursor.execute("SELECT name,rno,addr,phn,dob,field,branch FROM new_student WHERE mail=%s", (mail,))
        result = mycursor.fetchone()
        if result:
            name,rno,addr,phn,dob,branch,field = result
            return render_template("student/stprofile.html", name=name, mail=mail, rno=rno, addr=addr, phn=phn, dob=dob,branch=branch,field=field)
        else:
            return redirect("/login")
        
@app.route('/pupdate', methods=['GET', 'POST'])
def pupdate():
    if "mail" in session and session["role"] == "principal":
        mail = session["mail"]
        if request.method == 'POST':
            name = request.form['name']
            addr = request.form['addr']
            phn = request.form['phn']
            dob = request.form['dob']
            email = request.form["email"]
            mycursor.execute("UPDATE principle SET name=%s, mail=%s, addr=%s, phn=%s, dob=%s WHERE mail=%s", (name, email, addr, phn, dob,mail,))
            mydb.commit()
            return redirect(url_for('pprofile'))
        else:
            mycursor.execute("SELECT eid,name FROM principle WHERE mail=%s", (mail,))
            result = mycursor.fetchone()
            if result:
                eid,name = result
            return render_template("principal/pupdate.html", name=name, eid=eid)
    else:
        return redirect("/login")
    
@app.route('/tupdate',methods=['GET','POST'])
def tupdate():
    if "mail" in session and session["role"] == "teacher":
        mail = session["mail"]
        if request.method == 'POST':
            name = request.form['name']
            addr = request.form['addr']
            phn = request.form['phn']
            dob = request.form['dob']
            email = request.form["mail"]
            mycursor.execute("UPDATE new_teacher SET name=%s, mail=%s, addr=%s, phn=%s, dob=%s WHERE mail=%s", (name, email, addr, phn, dob,mail,))
            mydb.commit()
            return redirect(url_for('tprofile'))
        else:
            mycursor.execute("SELECT eid,name,field,branch FROM new_teacher WHERE mail=%s", (mail,))
            result = mycursor.fetchone()
            if result:
                eid,name,field,branch = result
            return render_template("teacher/tupdate.html", name=name, eid=eid, branch=branch, field=field)
    else:
        return redirect("/login")
    
@app.route('/stupdate',methods=['GET','POST'])
def stupdate():
    if "mail" in session and session["role"] == "student":
        mail = session["mail"]
        if request.method == 'POST':
            name = request.form['name']
            addr = request.form['addr']
            phn = request.form['phn']
            dob = request.form['dob']
            email = request.form["mail"]
            mycursor.execute("UPDATE new_student SET name=%s, mail=%s, addr=%s, phn=%s, dob=%s WHERE mail=%s", (name, email, addr, phn, dob,mail,))
            mydb.commit()
            return redirect(url_for('stprofile'))
        else:
            mycursor.execute("SELECT rno,name,field,branch FROM new_student WHERE mail=%s", (mail,))
            result = mycursor.fetchone()
            if result:
                rno,name,field,branch = result
            return render_template("student/stupdate.html", name=name, rno=rno, branch=branch, field=field)
    else:
        return redirect("/login")
    

    
@app.route('/ps')
def ps():
    if "mail" in session and session["role"] == "principal":
        mycursor.execute("SELECT rno, name, mail, addr, field, branch, phn, dob, perc from new_student")
        result1 = mycursor.fetchall()
        mycursor.execute("SELECT * FROM principle")
        result2 = mycursor.fetchall()
        name = result2[0][1] 
        if result1:
            return render_template("misc/ps.html", result=result1, principle=result2, name=name)
        else:
            return redirect("/login")
        
@app.route('/ts')
def ts():
    if "mail" in session and session["role"] == "teacher":
        mycursor.execute("SELECT rno, name, mail, addr, field, branch, phn, dob, perc from new_student")
        result1 = mycursor.fetchall()
        mycursor.execute("SELECT * FROM new_teacher")
        result2 = mycursor.fetchall()
        name = result2[0][1] 
        if result1:
            return render_template("teacher/ts.html", result=result1, new_teacher=result2, name=name)
        else:
            return redirect("/login")
        
@app.route('/pt')
def pt():
    if "mail" in session and session["role"] == "principal":
        mycursor.execute("SELECT eid, name, mail, addr, field, branch, phn, dob, qual from new_teacher")
        result1 = mycursor.fetchall()
        mycursor.execute("SELECT * FROM principle")
        result2 = mycursor.fetchall()
        name = result2[0][1] 
        if result1:
            return render_template("misc/pt.html", result=result1, principle=result2, name=name)
        else:
            return redirect("/login")

           


@app.route('/contact_new')
def home():
    return render_template('contact_new.html')

@app.route('/tupload')
def tupload():
    return render_template('teacher/tupload.html')


@app.route('/sresult')
def sresult():
    return render_template('teacher/sresult.html')



@app.route('/thome')
def thome():
    return render_template('teacher/thome.html')


@app.route('/sapply_leave', methods=['POST', 'GET'])
def sapply_leave():
    if "mail" in session and session["role"] == "student":
        mail = session["mail"]
        if request.method == 'POST':
            date = request.form['date']
            duration = request.form['duration']
            reason = request.form['reason']
            mycursor.execute("SELECT name FROM new_student WHERE mail=%s", (mail,))
            name = mycursor.fetchone()[0]
            sql = "INSERT INTO sleave (name, mail, date, duration, reason) VALUES (%s, %s, %s, %s, %s)"
            val = (name, mail, date, duration, reason)
            mycursor.execute(sql, val)
            mydb.commit()
            email_sender = 'sparkuniv2023@gmail.com'
            email_password = 'dkqpsgpcossymumg'
            email_receiver = mail
            subject = f"Leave Application"
            body = f"Greetings {name}, we have received your leave application with the following parameters:\n\nDate: {date}\n\nDuration: {duration}\n\nReason: {reason}\n\nWe will process your leave request soon...\n\nRegards,\nSpark University"

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver, email_sender
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            return render_template("student/sthome.html", name=name)
        else:
            return render_template("student/sapply_leave.html")
    else:
        return redirect('sthome')
    
@app.route('/tapply_leave', methods=['POST', 'GET'])
def tapply_leave():
    if "mail" in session and session["role"] == "teacher":
        mail = session["mail"]
        if request.method == 'POST':
            date = request.form['date']
            duration = request.form['duration']
            reason = request.form['reason']
            mycursor.execute("SELECT name FROM new_teacher WHERE mail=%s", (mail,))
            name = mycursor.fetchone()[0]
            sql = "INSERT INTO tleave (name, mail, date, duration, reason) VALUES (%s, %s, %s, %s, %s)"
            val = (name, mail, date, duration, reason)
            mycursor.execute(sql, val)
            mydb.commit()
            email_sender = 'sparkuniv2023@gmail.com'
            email_password = 'dkqpsgpcossymumg'
            email_receiver = mail
            subject = f"Leave Application"
            body = f"Greetings {name}, we have received your leave application with the following parameters:\n\nDate: {date}\n\nDuration: {duration}\n\nReason: {reason}\n\nWe will process your leave request soon...\n\nRegards,\nSpark University"

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver, email_sender
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            return render_template("teacher/thome.html", name=name)
        else:
            return render_template("teacher/tapply_leave.html")
    else:
        return redirect('thome')


@app.route('/sthome')
def sthome():
    return render_template('student/sthome.html')


@app.route('/pprofile')
def pp():
    return render_template('principal/pprofile.html')


@app.route('/pexamsch')
def pexamsch():
    return render_template('principal/pexamsch.html')


@app.route('/ptupdate')
def ptupdate():
    return render_template('ptupdate.html')

@app.route('/ptt')
def ptt():
    return render_template('ptt.html')


@app.route('/fee_structure')
def fee_structure():
    return render_template('fee_structure.html')


@app.route('/contact_new', methods=['POST'])
def contact_new():
    email_sender = 'sparkuniv2023@gmail.com'
    email_password = 'dkqpsgpcossymumg'
    email_receiver = request.form['email']
    subject = f"Spark University 2023"
    body = f"Greetings {request.form['name']}, we have received the following message from you:\n\n{request.form['msg']}\n\nWe will get in touch with you soon. \n\nRegards,\nSpark University"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver, email_sender
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    return """
    <script>
    alert('Email sent successfully!');
    window.location.href='/';
    </script>
    """


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Get form data
        rno = request.form['rno']
        name = request.form['name']
        mail = request.form['mail']
        addr = request.form['addr']
        field = request.form['field']
        branch = request.form['branch']
        phn = request.form['phn']
        dob = request.form['dob']
        perc = request.form['perc']
        pwd = request.form['pwd']
        role = "student"
        sql = "INSERT INTO new_student (rno, name, mail, addr, field, branch, phn, dob, perc, pwd, role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (rno, name, mail, addr, field,
               branch, phn, dob, perc, pwd, role)
        mycursor.execute(sql, val)
        mydb.commit()

    email_sender = 'sparkuniv2023@gmail.com'
    email_password = 'dkqpsgpcossymumg'
    email_receiver = request.form['mail']
    subject = f"Account Created Successfully"
    body = f"Dear {request.form['name']},\n\nYour account creation process has been successful.You will be able to LOGIN once the principal approves your request!\n\nRegards,\nSpark University."

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver, email_sender
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

        return '''
        <script>
            alert("Registration successful!");
            window.location.href = "/login";
        </script>
        '''

# Define a route for the registration page


@app.route('/register')
def registration():

    # Fetch the latest value of rno from the database and increment it by 1
    mycursor = mydb.cursor()
    mycursor.execute("SELECT rno FROM new_student ORDER BY rno DESC LIMIT 1")
    result = mycursor.fetchone()
    rno = 1 if result is None else result[0] + 1

    # Render the registration page with the incremented value of rno
    return render_template('register.html', rno=rno)

# @app.route('/about')
# def aboutnum():
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT COUNT(*) FROM new_student")
#     student_count = mycursor.fetchone()

#     mycursor.execute("SELECT COUNT(*) FROM new_teacher WHERE status = 'approved'")
#     teacher_count = mycursor.fetchone()

#     return render_template('about.html', student_count=student_count, teacher_count=teacher_count)


@app.route('/sampleregister', methods=['POST'])
def sampleregister():
    if request.method == 'POST':
        # Get form data
        eid = request.form['eid']
        name = request.form['name']
        mail = request.form['mail']
        addr = request.form['addr']
        field = request.form['field']
        branch = request.form['branch']
        phn = request.form['phn']
        dob = request.form['dob']
        qual = request.form['qual']
        pwd = request.form['pwd']
        role = "teacher"

        sql = "INSERT INTO new_teacher (eid, name, mail, addr, field, branch, phn, dob, qual, pwd, role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (eid, name, mail, addr, field,
               branch, phn, dob, qual, pwd,role)
        mycursor.execute(sql, val)
        mydb.commit()

    email_sender = 'sparkuniv2023@gmail.com'
    email_password = 'dkqpsgpcossymumg'
    email_receiver = request.form['mail']
    subject = f"Account Created Successfully"
    body = f"Dear {request.form['name']},\n\nYour account creation process has been successful.You will be able to LOGIN once the principal approves your request. \n\nRegards,\nSpark University."

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver, email_sender
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

        return '''
        <script>
            alert("Registration successful!");
            window.location.href = "/index";
        </script>
        '''

# Define a route for the registration page


@app.route('/sampleregister')
def sampleregistration():

    # Fetch the latest value of eid from the database and increment it by 1
    mycursor = mydb.cursor()
    mycursor.execute("SELECT eid FROM new_teacher ORDER BY eid DESC LIMIT 1")
    result = mycursor.fetchone()
    eid = 1 if result is None else result[0] + 1

    # Render the registration page with the incremented value of eid

    return render_template('sampleregister.html', eid=eid)




@app.route('/ps')
def psdisp():
    mycursor.execute("SELECT * FROM new_student")
    result = mycursor.fetchall()
    return render_template("ps.html", result=result)



# @app.route('/pt')
# def ptdisp():
#     mycursor.execute("SELECT * FROM new_teacher")
#     result = mycursor.fetchall()
#     return render_template('misc/pt.html', result=result)

@app.route('/phome')
def phome():
    return render_template('principal/phome.html')

@app.route('/phome')
def pnoti():
    mycursor.execute("SELECT * FROM new_student")
    notis = mycursor.fetchall()
    return render_template("ps.html", notis=notis)


if __name__ == '__main__':
    app.run(debug=True)

