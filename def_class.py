class stuff():
    __hidevalue=20
    normalvalue=20
    def __init__(self):
        print "i am init"
    def apple(self,aa):
        print aa
        self.aa=aa
        print self.aa
    def returnname(self):
        return self.aa*2
    def __call__(self):
        print "i am call"
class stuffchild(stuff):
    def __init__(self):
        pass
    def __str__(self):
        return "this is srt def- it's print always me when use print-classname"

def main():
    child1=stuffchild()
    print ("-----")
    child1.apple("8768768768")
    print ("1-----")
    print child1
    print ("2-----")
    child1()
    print ("3-----")
    alwaysruncall=stuff()
    print ("4-----")
    print alwaysruncall.normalvalue
    print ("5-----")
    #print alwaysruncall.__hidevalue
    alwaysruncall()
    print ("6-----")
    alwaysruninit=stuff()
    print ("7-----")
    alwaysruninit()
    print ("8-----")
    xx=stuff()
    print ("9-----")
    yy=stuff()
    print ("10-----")
    xx.apple('vvvvvvvvvv')
    yy.apple('ttttttttt')
if __name__ == '__main__':
    main()