import dlib

SP = dlib.shape_predictor('/tmp/shape_predictor_68_face_landmarks.dat')
FACEREC = dlib.face_recognition_model_v1('/tmp/dlib_face_recognition_resnet_model_v1.dat')
DETECTOR = dlib.get_frontal_face_detector()
