import dropbox, time, random, cv2
startTime = time.time()
def takeSnapshot():
    number = random.randint(0,100)

    #initialising cv2
    image_capture = cv2.VideoCapture(0)

    result = True

    while(result):
        ret,frame =image_capture.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name,frame)
        result = False

    return image_name
    print("Snapshot Taken Successfully")

    image_capture.release()
    cv2.destroyAllWindows()

def uploadFile(image_name):
    access_token = "sl.BBjr-OWxkCFIrL4mwYRIzLKcRil0_AR6H-54C6Ndek-rFWDIA95Typb3fAEC-2yIhxYkCg-gBkh7jHTx683zNLSMFmonKv6zU0JCke3rOvIJU5I6TKne_qhARBYR9K-6PLcKPrsB2SaV"
    file = image_name
    fileFrom = file
    fileTo = "/Snapshots/" + (image_name)
    dbx = dropbox.Dropbox(access_token)
    with open(fileFrom,'rb') as s:
        dbx.files_upload(s.read(), fileTo, mode = dropbox.files.WriteMode.overwrite)
        print("Snapshot Uploaded Successfully")

def main():
    while(True):
        if((time.time()- startTime)>= 5 ):
            name = takeSnapshot()
            uploadFile(name)


main()