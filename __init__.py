#!/usr/bin/python3
__all__=["init2"]
__NAME="Gomoku"
__AUTHOR="SUpQuark"
__LICENSE="GPLv3"

if __name__ == "__main__":
    print("%s\nby %s\n%s Licensed."%(__NAME,__AUTHOR,__LICENSE) )
    import print_map
    import init2
    print(init2())
    exit()
    __PLAYING_MODE_LIST=(
            {'num':0,'mean':'PVE Player First'},
            {'num':1,'mean':'PVE Computer First'}
        )
    while True:
        #try:
            for i in __PLAYING_MODE_LIST:
                print("%d %s"%(i['num'],i['mean']) )
            __PLAYING_MODE=int(input("Choose a playing mode: "))
        #except:
        #break
    
    
    #try:
        init.init()
    #except:

    #try:
        if(__PLAYING_MODE%2==0):
            user_input()
            __PLAYING_MODE
    while True:
        
