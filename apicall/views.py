from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
import face_recognition
import cv2
import numpy as np
import urllib.request
import firebase_admin
from firebase_admin import credentials , firestore

cre=credentials.Certificate("fire.json")
d_app=firebase_admin.initialize_app(cre)
db = firestore.client()


def get_encoded_faces():
    encoded = {}
    collections=db.collection("reportPerson").stream()
    for collection in collections:
        response1 = urllib.request.urlopen(collection.to_dict()['imageURI'])
        image = face_recognition.load_image_file(response1)
        encoding = face_recognition.face_encodings(image)[0]
        encoded[collection.id] = encoding
    return encoded

def get_url_by_id(id):
    return db.collection("realTimeRequest").document(id).get().to_dict()['imageURL']

def classify_face(id):
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())
    url=get_url_by_id(id)
    req = urllib.request.urlopen(url)
    image = np.asarray(bytearray(req.read()), dtype="uint8")
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)

    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
    return face_names

@api_view(['GET', 'POST'])
def api_request(request):
    return JsonResponse({"result":classify_face(request.query_params['id'])})

@api_view(['GET', 'POST'])
def api_test(request):
    return JsonResponse({"result":request.query_params['id']})

