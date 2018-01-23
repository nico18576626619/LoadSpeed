import  subprocess
import os
def PullVideoFile():

    videoFileName = ""

    p = subprocess.Popen('adb shell ls /sdcard/DCIM/Camera/', shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    picfiles = p.stdout.readlines()
    picfiles.reverse()

    for line in picfiles:
        if line.find(".mp4")!= False:
            videoFileName = line
            break

    if videoFileName != "":
        videoFileName = "".join(videoFileName.split())


        filedir = "../result/video/" + videoFileName.strip(".mp4")
        if os.path.exists(filedir) == False:
            os.makedirs(filedir)
        subprocess.call("adb pull /sdcard/DCIM/Camera/" + videoFileName + " " + filedir)
    else:
        print "error:can not find video file"



if __name__=='__main__':
    PullVideoFile()