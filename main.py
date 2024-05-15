from flask import Flask, request, jsonify, Blueprint
import psycopg2
from psycopg2.extras import RealDictCursor
import random


app = Flask(__name__)


def connectDB():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="dogukanince",
            password="admin",
            host="localhost",
            port="5433"
        )
        print("Connected to the database")
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database:", e)

@app.route("/", methods=["GET"])
def Index():
    # Optionally return a response here
    return "Welcome to the index page"

'''
students Endpoints
'''
@app.route("/students", methods=["GET"])
def list_students():
    conn = connectDB()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM students")
        students = cur.fetchall()
        return jsonify(students)
    except psycopg2.Error as e:
        print("Error fetching students:", e)
        return jsonify({"error": "Unable to fetch students"}), 500
    finally:
        cur.close()
        conn.close()

@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    conn = connectDB()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM students WHERE student_id = %s", (id,))
        student = cur.fetchone()
        if student:
            return jsonify(student)
        else:
            return jsonify({"message": "Student not found"}), 404
    except psycopg2.Error as e:
        print("Error fetching student:", e)
        return jsonify({"error": "Unable to fetch student"}), 500
    finally:
        cur.close()
        conn.close()
        
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    with app.app_context():
        new_student_number = input("Enter student's number: ")
        new_firstname = input("Enter student's firstname: ")
        new_lastname = input("Enter student's lastname: ")
        new_major = input("Enter student's major: ")
        new_email = input("Enter student's email: ")
        
        conn = connectDB()  # Reuse the database connection
        cur = conn.cursor()
        
        try:
            cur.execute("""
                UPDATE students 
                SET student_number = %s, firstname = %s, lastname = %s, major = %s, email = %s
                WHERE student_id = %s
            """, (new_student_number, new_firstname, new_lastname, new_major, new_email, id))
            conn.commit()
            return jsonify({"message": "Student updated successfully"})
        except psycopg2.Error as e:
            conn.rollback()
            print("Error updating student:", e)
            return jsonify({"error": "Unable to update student"}), 500
        finally:
            cur.close()
            conn.close()

@app.route("/students", methods=["POST"])
def create_student():
    with app.app_context():
        # Parse the request body to extract student data
        student_id = random.randint(200,100000)
        str(student_id)
        # Connect to the database
        conn = connectDB()
        cur = conn.cursor()
        new_student_number = input("Enter student's number: ")
        new_firstname = input("Enter student's firstname: ")
        new_lastname = input("Enter student's lastname: ")
        new_major = input("Enter student's major: ")
        new_email = input("Enter student's email: ")

        try:
            # Insert the new student into the database
            cur.execute("""
                INSERT INTO students (student_id, student_number, firstname, lastname, major, email)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (student_id, new_student_number, new_firstname, new_lastname, new_major, new_email))
            conn.commit()

            # Close the cursor and connection
            cur.close()
            conn.close()

            # Return a success response
            return jsonify({"message": "Student created successfully"}), 201
        except psycopg2.Error as e:
            # Handle database errors
            print("Error creating student:", e)
            return jsonify({"error": "Unable to create student"}), 500

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    with app.app_context():
        conn = connectDB()  # Reuse the database connection
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE student_id = %s", (id,))
        conn.commit()
        cur.close()
        return jsonify({"message": "Student deleted successfully"})

'''
instructors Endpoints
'''
@app.route("/instructors", methods=["GET"])
def list_instructors():
    conn = connectDB()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM instructors")
        instructors = cur.fetchall()
        return jsonify(instructors)
    except psycopg2.Error as e:
        print("Error fetching instructors:", e)
        return jsonify({"error": "Unable to fetch instructors"}), 500
    finally:
        cur.close()
        conn.close()

@app.route("/instructors/<int:id>", methods=["GET"])
def get_instructor(id):
    conn = connectDB()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM instructors WHERE instructor_id = %s", (id,))
        instructor = cur.fetchone()
        if instructor:
            return jsonify(instructor)
        else:
            return jsonify({"message": "instructor not found"}), 404
    except psycopg2.Error as e:
        print("Error fetching instructor:", e)
        return jsonify({"error": "Unable to fetch instructor"}), 500
    finally:
        cur.close()
        conn.close()
        
@app.route("/instructors/<int:id>", methods=["PUT"])
def update_instructor(id):
    with app.app_context():
        new_firstname = input("Enter instructor's firstname: ")
        new_lastname = input("Enter instructor's lastname: ")
        new_title = input("Enter instructor's title: ")
        new_email = input("Enter instructor's email: ")
        new_office_phone = input("Enter instructor's office phone: ")
        
        
        conn = connectDB()  # Reuse the database connection
        cur = conn.cursor()
        
        try:
            cur.execute("""
                UPDATE instructors 
                SET  firstname = %s, lastname = %s, title = %s, email = %s, office_phone = %s
                WHERE instructor_id = %s
            """, (new_firstname, new_lastname, new_title, new_email, new_office_phone, id))
            conn.commit()
            return jsonify({"message": "instructor updated successfully"})
        except psycopg2.Error as e:
            conn.rollback()
            print("Error updating instructor:", e)
            return jsonify({"error": "Unable to update instructor"}), 500
        finally:
            cur.close()
            conn.close()

@app.route("/instructors", methods=["POST"])
def create_instructor():
    with app.app_context():
        # Parse the request body to extract instructor data
        instructor_id = random.randint(200,100000)
        str(instructor_id)
        # Connect to the database
        conn = connectDB()
        cur = conn.cursor()
        new_firstname = input("Enter instructor's firstname: ")
        new_lastname = input("Enter instructor's lastname: ")
        new_title = input("Enter instructor's title: ")
        new_email = input("Enter instructor's email: ")
        new_office_phone = input("Enter instructor's office phone: ")

        try:
            # Insert the new instructor into the database
            cur.execute("""
                INSERT INTO instructors (instructor_id, firstname, lastname, title, email, office_phone)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (instructor_id, new_firstname, new_lastname, new_title, new_email, new_office_phone))
            conn.commit()

            # Close the cursor and connection
            cur.close()
            conn.close()

            # Return a success response
            return jsonify({"message": "instructor created successfully"}), 201
        except psycopg2.Error as e:
            # Handle database errors
            print("Error creating instructor:", e)
            return jsonify({"error": "Unable to create instructor"}), 500

@app.route("/instructors/<int:id>", methods=["DELETE"])
def delete_instructor(id):
    with app.app_context():
        conn = connectDB()  # Reuse the database connection
        cur = conn.cursor()
        cur.execute("DELETE FROM instructors WHERE instructor_id = %s", (id,))
        conn.commit()
        cur.close()
        return jsonify({"message": "instructor deleted successfully"})

'''
classroom Endpoints
'''
@app.route("/classroom", methods=["GET"])
def list_classroom():
    conn = connectDB()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM classroom")
        classroom = cur.fetchall()
        return jsonify(classroom)
    except psycopg2.Error as e:
        print("Error fetching classroom:", e)
        return jsonify({"error": "Unable to fetch classroom"}), 500
    finally:
        cur.close()
        conn.close()

@app.route("/classroom/<int:id>", methods=["GET"])
def get_classroom(id):
    conn = connectDB()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM classroom WHERE classroom_id = %s", (id,))
        classroom = cur.fetchone()
        if classroom:
            return jsonify(classroom)
        else:
            return jsonify({"message": "classroom not found"}), 404
    except psycopg2.Error as e:
        print("Error fetching classroom:", e)
        return jsonify({"error": "Unable to fetch classroom"}), 500
    finally:
        cur.close()
        conn.close()
        
@app.route("/classroom/<int:id>", methods=["PUT"])
def update_classroom(id):
    with app.app_context():
        new_capacity = input("Enter classroom's capacity: ")
        new_blackboard_capacity = input("Enter blackboard capacity: ")
        new_whiteboard_capacity = input("Enter whiteboard capacity: ")
        new_smartboard_capacity = input("Enter smartboard capacity: ")
        new_projector_capacity = input("Enter smartboard capacity: ")
    
        conn = connectDB()  # Reuse the database connection
        cur = conn.cursor()
        
        try:
            cur.execute("""
                UPDATE classroom 
                SET  classroom_capacity = %s, blackboard_capacity = %s, whiteboard_capacity = %s, smartboard_capacity = %s, projector_capacity = %s
                WHERE classroom_id = %s
            """, (new_capacity, new_blackboard_capacity, new_whiteboard_capacity, new_smartboard_capacity, new_projector_capacity, id))
            conn.commit()
            return jsonify({"message": "classroom updated successfully"})
        except psycopg2.Error as e:
            conn.rollback()
            print("Error updating classroom:", e)
            return jsonify({"error": "Unable to update classroom"}), 500
        finally:
            cur.close()
            conn.close()

@app.route("/classroom", methods=["POST"])
def create_classroom():
    with app.app_context():
        # Parse the request body to extract classroom data
        classroom_id = random.randint(200,100000)
        str(classroom_id)
        # Connect to the database
        conn = connectDB()
        cur = conn.cursor()
        new_capacity = input("Enter classroom's capacity: ")
        new_blackboard_capacity = input("Enter blackboard capacity: ")
        new_whiteboard_capacity = input("Enter whiteboard capacity: ")
        new_smartboard_capacity = input("Enter smartboard capacity: ")
        new_projector_capacity = input("Enter smartboard capacity: ")

        try:
            # Insert the new classroom into the database
            cur.execute("""
                INSERT INTO classroom (classroom_id, classroom_capacity, blackboard_capacity, whiteboard_capacity, smartboard_capacity, projector_capacity)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (classroom_id, new_capacity, new_blackboard_capacity, new_whiteboard_capacity, new_smartboard_capacity, new_projector_capacity))
            conn.commit()

            # Close the cursor and connection
            cur.close()
            conn.close()

            # Return a success response
            return jsonify({"message": "classroom created successfully"}), 201
        except psycopg2.Error as e:
            # Handle database errors
            print("Error creating classroom:", e)
            return jsonify({"error": "Unable to create classroom"}), 500

@app.route("/classroom/<int:id>", methods=["DELETE"])
def delete_classroom(id):
    with app.app_context():
        conn = connectDB()  # Reuse the database connection
        cur = conn.cursor()
        cur.execute("DELETE FROM classroom WHERE classroom_id = %s", (id,))
        conn.commit()
        cur.close()
        return jsonify({"message": "classroom deleted successfully"})


'''
course Endpoints
'''
@app.route("/course", methods=["GET"])
def list_course():
    conn = connectDB()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM courses")
        course = cur.fetchall()
        return jsonify(course)
    except psycopg2.Error as e:
        print("Error fetching course:", e)
        return jsonify({"error": "Unable to fetch course"}), 500
    finally:
        cur.close()
        conn.close()

@app.route("/course/<int:id>", methods=["GET"])
def get_course(id):
    conn = connectDB()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM courses WHERE course_id = %s", (id,))
        course = cur.fetchone()
        if course:
            return jsonify(course)
        else:
            return jsonify({"message": "course not found"}), 404
    except psycopg2.Error as e:
        print("Error fetching course:", e)
        return jsonify({"error": "Unable to fetch course"}), 500
    finally:
        cur.close()
        conn.close()
        
@app.route("/course/<int:id>", methods=["PUT"])
def update_course(id):
    with app.app_context():
        new_name = input("Enter course's name: ")
        new_department = input("Enter course's department: ")
        new_description = input("Enter course's description: ")
        new_credits = input("Enter course's credits: ")
        instructor_id = input("Enter course's instructor ID: ")
    
        conn = connectDB()  # Reuse the database connection
        cur = conn.cursor()
        
        try:
            cur.execute("""
                UPDATE courses
                SET  course_name = %s, department = %s, description = %s, credits = %s, instructor_id = %s
                WHERE course_id = %s
            """, (new_name, new_department, new_description, new_credits, instructor_id, id))
            conn.commit()
            return jsonify({"message": "course updated successfully"})
        except psycopg2.Error as e:
            conn.rollback()
            print("Error updating course:", e)
            return jsonify({"error": "Unable to update course"}), 500
        finally:
            cur.close()
            conn.close()

@app.route("/course", methods=["POST"])
def create_course():
    with app.app_context():
        # Parse the request body to extract course data
        course_id = random.randint(200,100000)
        str(course_id)
        # Connect to the database
        conn = connectDB()
        cur = conn.cursor()
        new_name = input("Enter course's name: ")
        new_department = input("Enter course's department: ")
        new_description = input("Enter course's description: ")
        new_credits = input("Enter course's credits: ")
        instructor_id = input("Enter course's instructor ID: ")

        try:
            # Insert the new course into the database
            cur.execute("""
                INSERT INTO courses (course_id, course_name, department, description, credits, instructor_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (course_id, new_name, new_department, new_description, new_credits, instructor_id))
            conn.commit()

            # Close the cursor and connection
            cur.close()
            conn.close()

            # Return a success response
            return jsonify({"message": "course created successfully"}), 201
        except psycopg2.Error as e:
            # Handle database errors
            print("Error creating course:", e)
            return jsonify({"error": "Unable to create course"}), 500

@app.route("/course/<int:id>", methods=["DELETE"])
def delete_course(id):
    with app.app_context():
        conn = connectDB()  # Reuse the database connection
        cur = conn.cursor()
        cur.execute("DELETE FROM courses WHERE course_id = %s", (id,))
        conn.commit()
        cur.close()
        return jsonify({"message": "course deleted successfully"})

'''
section Endpoints
'''
@app.route("/section", methods=["GET"])
def list_section():
    conn = connectDB()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM sections")
        section = cur.fetchall()
        return jsonify(section)
    except psycopg2.Error as e:
        print("Error fetching section:", e)
        return jsonify({"error": "Unable to fetch section"}), 500
    finally:
        cur.close()
        conn.close()

@app.route("/section/<int:id>", methods=["GET"])
def get_section(id):
    conn = connectDB()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM sections WHERE section_id = %s", (id,))
        section = cur.fetchone()
        if section:
            return jsonify(section)
        else:
            return jsonify({"message": "section not found"}), 404
    except psycopg2.Error as e:
        print("Error fetching section:", e)
        return jsonify({"error": "Unable to fetch section"}), 500
    finally:
        cur.close()
        conn.close()
        
@app.route("/section/<int:id>", methods=["PUT"])
def update_section(id):
    with app.app_context():
        new_course_id = input("Enter section's course ID: ")
        new_semester = input("Enter section's semester: ")
        new_capacity = input("Enter section's capacity: ")
        new_instructor_id = input("Enter section's instructor ID: ")
        new_course_time = input("Enter section's course time: ")
        new_classroom_id = input("Enter section's classroom ID: ")
    
        conn = connectDB()  # Reuse the database connection
        cur = conn.cursor()
        
        try:
            cur.execute("""
                UPDATE sections
                SET  course_id = %s, semester = %s, capacity = %s, instructor_id = %s, course_time = %s, classroom_id = %s 
                WHERE section_id = %s
            """, (new_course_id, new_semester, new_capacity, new_instructor_id, new_course_time, xwnew_classroom_id, id))
            conn.commit()
            return jsonify({"message": "section updated successfully"})
        except psycopg2.Error as e:
            conn.rollback()
            print("Error updating section:", e)
            return jsonify({"error": "Unable to update section"}), 500
        finally:
            cur.close()
            conn.close()

@app.route("/section", methods=["POST"])
def create_section():
    with app.app_context():
        # Parse the request body to extract section data
        section_id = random.randint(200,100000)
        str(section_id)
        # Connect to the database
        conn = connectDB()
        cur = conn.cursor()
        new_course_id = input("Enter section's course ID: ")
        new_semester = input("Enter section's semester: ")
        new_capacity = input("Enter section's capacity: ")
        new_instructor_id = input("Enter section's instructor ID: ")
        new_course_time = input("Enter section's course time: ")
        new_classroom_id = input("Enter section's classroom ID: ")

        try:
            # Insert the new section into the database
            cur.execute("""
                INSERT INTO sections (section_id, course_id, semester, capacity, instructor_id, course_time, classroom_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (section_id, new_course_id, new_semester, new_capacity, new_instructor_id, new_course_time, new_classroom_id))
            conn.commit()

            # Close the cursor and connection
            cur.close()
            conn.close()

            # Return a success response
            return jsonify({"message": "section created successfully"}), 201
        except psycopg2.Error as e:
            # Handle database errors
            print("Error creating section:", e)
            return jsonify({"error": "Unable to create section"}), 500

@app.route("/section/<int:id>", methods=["DELETE"])
def delete_section(id):
    with app.app_context():
        conn = connectDB()  # Reuse the database connection
        cur = conn.cursor()
        cur.execute("DELETE FROM sections WHERE section_id = %s", (id,))
        conn.commit()
        cur.close()
        return jsonify({"message": "section deleted successfully"})


'''
enrollment Endpoints
'''
@app.route("/enrollment", methods=["GET"])
def list_enrollment():
    conn = connectDB()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM enrollments")
        enrollment = cur.fetchall()
        return jsonify(enrollment)
    except psycopg2.Error as e:
        print("Error fetching enrollment:", e)
        return jsonify({"error": "Unable to fetch enrollment"}), 500
    finally:
        cur.close()
        conn.close()

@app.route("/enrollment/<int:id>", methods=["GET"])
def get_enrollment(id):
    conn = connectDB()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM enrollments WHERE enrollment_id = %s", (id,))
        enrollment = cur.fetchone()
        if enrollment:
            return jsonify(enrollment)
        else:
            return jsonify({"message": "enrollment not found"}), 404
    except psycopg2.Error as e:
        print("Error fetching enrollment:", e)
        return jsonify({"error": "Unable to fetch enrollment"}), 500
    finally:
        cur.close()
        conn.close()
        
@app.route("/enrollment/<int:id>", methods=["PUT"])
def update_enrollment(id):
    with app.app_context():
        new_student_id = input("Enter enrollment's student ID: ")
        new_section_id = input("Enter enrollment's section ID: ")
        new_grade = input("Enter enrollment's grade: ")
        new_capacity = input("Enter enrollment's capacity: ")

        conn = connectDB()  # Reuse the database connection
        cur = conn.cursor()
        
        try:
            cur.execute("""
                UPDATE enrollments
                SET  student_id = %s, section_id = %s, grade = %s, capacity = %s 
                WHERE enrollment_id = %s
            """, (new_student_id, new_section_id, new_grade, new_capacity, id))
            conn.commit()
            return jsonify({"message": "enrollment updated successfully"})
        except psycopg2.Error as e:
            conn.rollback()
            print("Error updating enrollment:", e)
            return jsonify({"error": "Unable to update enrollment"}), 500
        finally:
            cur.close()
            conn.close()

@app.route("/enrollment", methods=["POST"])
def create_enrollment():
    with app.app_context():
        # Parse the request body to extract enrollment data
        enrollment_id = random.randint(200,100000)
        str(enrollment_id)
        # Connect to the database
        conn = connectDB()
        cur = conn.cursor()
        new_student_id = input("Enter enrollment's student ID: ")
        new_section_id = input("Enter enrollment's section ID: ")
        new_grade = input("Enter enrollment's grade: ")
        new_capacity = input("Enter enrollment's capacity: ")

        try:
            # Insert the new enrollment into the database
            cur.execute("""
                INSERT INTO enrollments (enrollment_id, student_id, section_id, grade, capacity)
                VALUES (%s, %s, %s, %s, %s)
            """, (enrollment_id, new_student_id, new_section_id, new_grade, new_capacity))
            conn.commit()

            # Close the cursor and connection
            cur.close()
            conn.close()

            # Return a success response
            return jsonify({"message": "enrollment created successfully"}), 201
        except psycopg2.Error as e:
            # Handle database errors
            print("Error creating enrollment:", e)
            return jsonify({"error": "Unable to create enrollment"}), 500

@app.route("/enrollment/<int:id>", methods=["DELETE"])
def delete_enrollment(id):
    with app.app_context():
        conn = connectDB()  # Reuse the database connection
        cur = conn.cursor()
        cur.execute("DELETE FROM enrollments WHERE enrollment_id = %s", (id,))
        conn.commit()
        cur.close()
        return jsonify({"message": "enrollment deleted successfully"})



def list_tables():
    print("Tables:")
    print("1. Students")
    print("2. Instructors")
    print("3. Classroom")
    print("4. Courses")
    print("5. Sections")
    print("6. Enrollments")
    
if __name__ == "__main__":
    app.run(debug=True, port=5434)
    