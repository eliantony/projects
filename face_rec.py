import face_recognition

picture_of_me = face_recognition.load_image_file("eli.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)
print(len(my_face_encoding))

face1 = my_face_encoding[0]

unknown_picture = face_recognition.load_image_file("test3.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)

print(len(unknown_face_encoding))
face2 = unknown_face_encoding[0]

results = face_recognition.compare_faces([face1], face2)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")
