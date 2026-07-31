import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st


from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():
  detector = dlib.get_frontal_face_detector()

  sp = dlib.shape_predictor(face_recognition_models.pose_predictor_model_location())


  face_rec = dlib.face_recognition_model_v1(face_recognition_models.face_recognition_model_location())

  return detector, sp, face_rec


def get_face_embeddings(image_np):
  detector, sp, face_rec = load_dlib_models()
  faces = detector(image_np, 1)
  encodings = []
  for face in faces:
    shape = sp(image_np, face)
    face_descriptor = face_rec.compute_face_descriptor(image_np, shape,1) #128 embeddings

    encodings.append(np.array(face_descriptor))
  return encodings


def get_trained_model():
  students = get_all_students()
  X = []
  y = []

  if not students:
    return None  # No students found in the database
  for student in students:
    embedding = student.get('face_embedding')
    if embedding:
      X.append(np.array(embedding))
      y.append(student.get('student_id'))  # Assuming 'student_id' is the unique identifier for the student

  if len(X) == 0:
    return None  # No data to train on

  clf = SVC(kernel='linear', probability=True, class_weight='balanced')
  try:
    clf.fit(X, y)
  except ValueError as e:
    pass

  return {'clf': clf, 'X': X, 'y': y}  # Return the trained model and the training data

def train_classifier():
  st.cache_resource.clear()
  model_data = get_trained_model()
  return bool(model_data)  # Return True if model is trained, False otherwise


def predict_attendence(class_img_np):
  encodings = get_face_embeddings(class_img_np)

  detected_student = {}

  model_data = get_trained_model()

  if not model_data:
    return detected_student, [], len(encodings)  # Return empty results if model is not trained

  clf = model_data['clf']
  X_train = model_data['X']
  y_train = model_data['y']


  all_students = sorted(list(set(y_train)))  # Get unique student IDs from the training data

  for encoding in encodings:
    if len(all_students) <= 2:
      predicted_id = int(clf.predict([encoding])[0])
    else:
      predicted_id = int(all_students[0])

    student_embedding = X_train[y_train.index(predicted_id)]

    best_match_score = np.linalg(student_embedding - encoding)

    resemblance_threshold = 0.6

    if best_match_score <= resemblance_threshold:
      detected_student[predicted_id] = True

    return detected_student, all_students, len(encoding)