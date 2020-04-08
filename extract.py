import sys, cv2, os, io, progressbar, random
import numpy as np
from zipfile import ZipFile

########## Modify Parameters Here If You Want ##########
FPS = 1  # downsample fps to
MAX_NUM = 1000  # maximum photo number
########################################################




########## Don't Change the Settings Hereafter ##########
video_file_folder = sys.argv[1]
video_files_list = os.listdir(video_file_folder)
video_files = []
for v in video_files_list:
    f_path = f'./{video_file_folder}/{v}'
    try:
        cap = cv2.VideoCapture(f_path)
        if not cap.isOpened():
            raise NameError(f'{f_path} is not a video file')
    except:
        continue
    video_files.append(f_path)

##### Detect Face #####
def Detect(image, cascade_file = "./lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))
    return faces

##### Detect faces from video #####
def Detect_Faces(video_files, zip_obj):
    number = len(video_files)

    try:
        os.mkdir('./temp_faces')
    except:
        os.system('rm -r ./temp_faces')
        os.mkdir('./temp_faces')

    for n in range(number):
        video = cv2.VideoCapture(video_files[n])
        status = True
        length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = video.get(cv2.CAP_PROP_FPS)
        downsample_rate = int(fps / FPS)
 
        widgets=[
        f'Video {n + 1} of {number}:', progressbar.Percentage(), ' (',
        progressbar.Counter(), f' of {length}) ',
        progressbar.Bar(),
        ' [', progressbar.ETA(), '] ',]
 
        for k in progressbar.progressbar(range(length), widgets=widgets):
            status, img = video.read()
            if not status:
                break
            if k % downsample_rate != 0:
                continue
 
            faces = Detect(img)
            count = 0
            for (x, y, w, h) in faces:
                xx = int(max(0, x - w / 4))
                yy = int(max(0, y - h / 4))
                ww = int(w * 1.5)
                hh = int(h * 1.5)
                img_crop = img[y: y + h, x: x + w]
                cv2.imwrite(f'./temp_faces/face_{n}_{k}_{count}.jpg', img_crop)
                count += 1
    face_files_all = os.listdir('./temp_faces/')
    face_files_all = ['./temp_faces/' + v for v in face_files_all]
    face_files = []
    for v in face_files_all:
        if os.stat(v).st_size >= 20480:
            face_files.append(v)
    selected = random.sample(face_files, min(MAX_NUM, len(face_files)))
    for face in selected:
        zip_obj.write(face)
    os.system('rm -r ./temp_faces')

##### Work Place #####
video_file_folder = sys.argv[1]
video_files_list = os.listdir(video_file_folder)
video_files = []
for v in video_files_list:
    f_path = f'./{video_file_folder}/{v}'
    try:
        cap = cv2.VideoCapture(f_path)
        if not cap.isOpened():
            raise NameError(f'{f_path} is not a video file')
    except:
        continue
    video_files.append(f_path)

zip_obj = ZipFile(f'{video_file_folder}_faces.zip', 'w')
faces = Detect_Faces(video_files, zip_obj)
zip_obj.close()

