from src.database.config import supabase

import bcrypt

def check_teacher_exists(username):
  # Check if a teacher with the given username exists in the database
  response = supabase.table("teachers").select("username").eq("username", username).execute()
  return len(response.data) > 0


def hashed_password(password):
  # Hash the password using bcrypt
  salt = bcrypt.gensalt()
  hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
  return hashed.decode('utf-8')


def check_password(password, hashed):
  # Check if the provided password matches the hashed password
  return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def create_teacher(username, password, name):

  data = {
    "username": username,
    "password": hashed_password(password),
    "name": name
    }
  
  # Insert the new teacher into the database
  response = supabase.table("teachers").insert(data).execute()
  return response.data


def teacher_login(username, password):
  # Retrieve the teacher's record from the database
  response = supabase.table("teachers").select("*").eq("username", username).execute()
  if response.data:
    teacher = response.data[0]
    if check_password(password, teacher["password"]):
      return teacher

  return None



def get_all_students():
  # Retrieve all student records from the database
  response = supabase.table("students").select("*").execute()
  return response.data 


def create_student(new_name, face_embedding=None, voice_embedding=None):
  data = {'name': new_name, 'face_embedding': face_embedding, 'voice_embedding': voice_embedding}
  response = supabase.table('students').insert(data).execute()
  return response.data


def create_subject(sub_code, sub_name, section, teacher_id):
  data = {
    "subject_code": sub_code,
    "name": sub_name,
    "section": section,
    "teacher_id": teacher_id
  }
  response = supabase.table("subjects").insert(data).execute()
  return response.data

"""
def get_teacher_subjects(teacher_id):
  # Retrieve subjects for a specific teacher from the database
  response = (
    supabase.table("subjects")
    .select(
        "*, attendence_logs(timestamp), subject_students(count)",
        count="exact"
    )
    .eq("teacher_id", teacher_id)
    .execute()
  )
  subjects = response.data
  #print(subjects)

  for subject in subjects:
    subject["total_students"] = len(subject.get("subject_students", []))
 
    attendence = subject.get("attendence_logs", [])
    unique_sessions = len(set(log["timestamp"] for log in attendence))
    subject["total_classes"] = unique_sessions

    subject.pop("subject_students", None)
    subject.pop("attendence_logs", None)
  return subjects
"""


def get_teacher_subjects(teacher_id):
    response = (
        supabase.table("subjects")
        .select("*, subject_students(*), attendence_logs(timestamp)")
        .eq("teacher_id", teacher_id)
        .execute()
    )

    subjects = response.data

    for subject in subjects:
        # Count the number of students enrolled
        subject["total_students"] = len(subject.get("subject_students", []))

        # Count unique attendance sessions
        attendance = subject.get("attendence_logs", [])
        unique_sessions = len(set(log["timestamp"] for log in attendance))
        subject["total_classes"] = unique_sessions

        # Remove nested data before returning
        subject.pop("subject_students", None)
        subject.pop("attendence_logs", None)

    return subjects


def enroll_student_to_subject(student_id, subject_id):
    data = {
        "student_id": student_id,
        "subject_id": subject_id
    }
    response = supabase.table("subject_students").insert(data).execute()
    return response.data

def unenroll_student_from_subject(student_id, subject_id):
    response = supabase.table("subject_students").delete().eq("student_id", student_id).eq("subject_id", subject_id).execute()
    return response.data


def get_student_subjects(student_id):
    response = (
        supabase.table("subject_students")
        .select("*, subjects(*)")
        .eq("student_id", student_id)
        .execute()
    )
    return response.data

def get_student_attendance_logs(student_id):
    response = (
        supabase.table("attendence_logs")
        .select("*")
        .eq("student_id", student_id)
        .execute()
    )
    return response.data


def create_attendance(logs):
  response = supabase.table('attendence_logs').insert(logs).execute()
  return response.data