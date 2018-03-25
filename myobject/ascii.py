from PIL import Image
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('-width',type=int,default=80)
parser.add_argument('-height',type=int,default=80)
args=parser.parse_args()

class character():
    def __init__(self):
        self.IMG=args.file
        self.WIDTH=args.width
        self.HEIGHT=args.height
        self.OUTPUT=args.output
        self.ascii_char=list("~!@<>?:'{|}\#$%^&*()_+-=QWETYUIAPOLSKDJHFGZXVCBNM<>?1234567098")
        self.txt=''


    def get_char(self,r,g,b,alpha=256):
        if alpha==0:
            return ' '
        length=len(self.ascii_char)
        gray=int(0.2126*r+0.7152*g+0.0722*b)
        unit=(256.0+1)/length
        return self.ascii_char[int(gray/unit)]

    def convert(self):
        im=Image.open(self.IMG)
        im=im.resize((self.WIDTH,self.HEIGHT),Image.NEAREST)
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                self.txt+=self.get_char(*im.getpixel((j,i)))
            self.txt+='\n'

    def save(self):
        if self.OUTPUT:
            with open(self.OUTPUT,'w') as f:
                f.write(self.txt)

        else:
            with open("output.txt",'w') as f:
                f.write(self.txt)

    def start(self):
        self.convert()
        self.save()

if __name__=='__main__':
    c=character()
    c.start()







