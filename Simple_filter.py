import cv2

# Baca gambar
img = cv2.imread('nama_gambar.jpg')

# Buat Cascade Classifier untuk deteksi wajah
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Konversi ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Deteksi wajah pada gambar
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Loop melalui setiap wajah yang terdeteksi
for (x, y, w, h) in faces:
    # Ambil wilayah wajah dari gambar
    face_roi = img[y:y+h, x:x+w]

    # Konversi wilayah wajah ke grayscale
    face_gray = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)

    # Terapkan Gaussian Blur pada wilayah wajah
    face_blur = cv2.GaussianBlur(face_gray, (15, 15), 0)

    # Terapkan filter unsharp mask pada wilayah wajah
    face_usm = cv2.addWeighted(face_gray, 1.5, face_blur, -0.5, 0)

    # Masukkan kembali wilayah wajah yang telah diberi filter ke gambar
    img[y:y+h, x:x+w] = face_usm

# Tampilkan hasil
cv2.imshow('Hasil', img)
cv2.waitKey(0)
