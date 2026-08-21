# AttendX – AI-Powered Smart Attendance System

AttendX is an AI-powered attendance management system built with Python and Streamlit. It uses face recognition and voice recognition technologies to automate student identification and attendance tracking, while Supabase provides the backend database for managing students, teachers, subjects, and attendance records.

## 🚀 Features

- 👤 **Face Recognition Attendance**
  - Detects and recognizes students using facial embeddings.
  - Uses Dlib and face-recognition models for face detection and recognition.
  - Uses an SVM classifier for student identification.

- 🎙️ **Voice Recognition**
  - Uses voice embeddings to support student identification.
  - Resemblyzer and Librosa are used for audio processing and voice feature extraction.

- 👨‍🏫 **Teacher Dashboard**
  - Create and manage subjects.
  - View enrolled students.
  - Track attendance sessions.
  - Share subject enrollment codes.

- 👨‍🎓 **Student Dashboard**
  - View enrolled subjects.
  - Enroll in subjects using a subject code.
  - View attendance statistics.
  - Unenroll from subjects.

- 📸 **Multiple Attendance Images**
  - Capture classroom images using the camera.
  - Upload multiple classroom photographs.
  - Process classroom images for face recognition.

- 📊 **Attendance Management**
  - Records attendance sessions.
  - Tracks total classes and attended classes.
  - Maintains student attendance records.

- 🔐 **Authentication**
  - Separate teacher and student workflows.
  - Password authentication using bcrypt.

- 🗄️ **Supabase Backend**
  - Stores student information.
  - Stores teacher information.
  - Stores subjects and enrollments.
  - Stores attendance logs.

- 📱 **Streamlit Interface**
  - Interactive web-based interface.
  - Responsive teacher and student dashboards.
  - Dialogs, cards, metrics, QR codes and interactive controls.

---

## 🧠 How AttendX Works

### Face Recognition Pipeline

```text
Classroom Image
       ↓
Face Detection
       ↓
Facial Landmark Detection
       ↓
128-D Face Embedding
       ↓
SVM Classifier
       ↓
Student Identification
       ↓
Attendance Record
