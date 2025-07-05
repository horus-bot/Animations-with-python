from PIL import Image

import sys 

def animations():
    images=[]
    for arg in sys.argv[1:]:
        image=Image.open(arg)
        images.append(image)

    images[0].save(
        "animations.gif",
        save_all=True,
        append_images=[images[1]],
        duration=200,
        loop=0
    ) 

def main():
    if len(sys.argv)==1:
        sys.exit("please mention .gif files to be compiled ")
    else :
        animations()

if __name__=="__main__":
    main()

