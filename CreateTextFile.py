import os

currDest = os.path.dirname(os.path.abspath(__file__))

dest = os.path.join(currDest, 'img')

files = os.listdir(dest)
files.sort()

def createFile():
    f = open(dest+"/files.txt", "a")
    for i in range(0, 4):
        j = 0
        while j<10:
              f.write("file "+str(dest+'/'+files[j])+'\n')
              j+=2
        j=9
        while j>-1:
            f.write("file "+str(dest+'/'+files[j])+'\n')
            j-=2

    f.close()
    f = open(dest+"/files.txt", "r")
    print(f.read())
    f.close()

createFile()

# ffmpeg -r 20 -f concat -safe 0 -i files.txt -c:v libx264 -pix_fmt yuv420p out.mp4
