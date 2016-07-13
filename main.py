
class stuff():

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

def main():
    alwaysruncall=stuff()
    alwaysruncall()
    alwaysruninit=stuff()
    alwaysruninit()
    xx=stuff()
    yy=stuff()
    xx.apple('vvvvvvvvvv')
    yy.apple('ttttttttt')
if __name__ == '__main__':
    main()