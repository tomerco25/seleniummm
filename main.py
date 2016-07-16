
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
        return "this is srt def"


def main():
    child1=stuffchild()
    child1.apple("8768768768")
    print child1
    child1()
    print ("-----------------------")
    alwaysruncall=stuff()
    print alwaysruncall.normalvalue
    #print alwaysruncall.__hidevalue
    alwaysruncall()
    alwaysruninit=stuff()
    alwaysruninit()
    xx=stuff()
    yy=stuff()
    xx.apple('vvvvvvvvvv')
    yy.apple('ttttttttt')
if __name__ == '__main__':
    main()