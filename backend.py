# from flask import Flask, request, jsonify, render_template

# import mysql.connector

# app = Flask(__name__)

# # Connect to MySQL database
# conn = mysql.connector.connect(
#     host='database-1',
#     user='seshu',
#     password='seshureddy',
#     database='pavan'
# )
# cursor = conn.cursor()

# # Create a table to store student data if not exists
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS students (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         firstname VARCHAR(255),
#         middlename VARCHAR(255),
#         lastname VARCHAR(255),
#         rollnumber VARCHAR(255),
#         course VARCHAR(255),
#         year VARCHAR(255),
#         gender VARCHAR(255),
#         age INT
#     )
# ''')
# conn.commit()

# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')

# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     data = request.form
#     firstname = data['firstname']
#     middlename = data['middlename']
#     lastname = data['lastname']
#     rollnumber = data['rollnumber']
#     course = data['course']
#     year = data['year']
#     gender = data['gender']
#     age = data['age']
    
#     # Insert the form data into the database
#     cursor.execute('''
#         INSERT INTO students (firstname, middlename, lastname, rollnumber, course, year, gender, age)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#     ''', (firstname, middlename, lastname, rollnumber, course, year, gender, age))
#     conn.commit()
    
#     return jsonify({'message': 'Form submitted successfully'})

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='seshu',
    password='seshureddy',
    database='database-1'
)
cursor = conn.cursor()

# Create a table to store student data if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        firstname VARCHAR(255),
        middlename VARCHAR(255),
        lastname VARCHAR(255),
        rollnumber VARCHAR(255),
        course VARCHAR(255),
        year VARCHAR(255),
        gender VARCHAR(255),
        age INT
    )
''')
conn.commit()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        data = request.form
        firstname = data['firstname']
        middlename = data['middlename']
        lastname = data['lastname']
        rollnumber = data['rollnumber']
        course = data['course']
        year = data['year']
        gender = data['gender']
        age = data['age']
        
        # Insert the form data into the database
        cursor.execute('''
            INSERT INTO students (firstname, middlename, lastname, rollnumber, course, year, gender, age)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (firstname, middlename, lastname, rollnumber, course, year, gender, age))
        conn.commit()
        
        return jsonify({'message': 'Form submitted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

















