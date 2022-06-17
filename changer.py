import os
import sched, time

directoryName = "D:\\20220617PM"
filePath = os.path.abspath(directoryName)
filePathWithSlash = filePath + "\\"

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    for counter, filename in enumerate(os.listdir(directoryName)):
        
        srcfilenameWithPath = os.path.join(filePathWithSlash, filename)
        neofilename = filename[0:17]
        dstfilenameWithPath = os.path.join(filePathWithSlash, neofilename + '.mp4')
        print(filename, '->', neofilename + '.mp4')
        os.rename(srcfilenameWithPath, dstfilenameWithPath )
    sc.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()
