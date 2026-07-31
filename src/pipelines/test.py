import dlib

print("Dlib version:", dlib.__version__)

detector = dlib.get_frontal_face_detector()
print("Detector loaded successfully!")
import face_recognition
print('face_recognition imported successfully')"