NzScore,NzSuperOver,NzFour=int(input()),int(input()),int(input())
EngScore,EngSuperOver,EngFour=int(input()),int(input()),int(input())

if NzScore>EngScore:
    print('New Zealend')
elif NzScore<EngScore:
    print('England')
elif NzSuperOver>EngSuperOver:
    print('New Zealand')
elif NzSuperOver<EngSuperOver:
    print('England')
elif NzFour>EngFour:
    print('New Zealand')
elif NzFour<EngFour:
    print('England')