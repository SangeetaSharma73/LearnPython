l,w,length,width = int(input()),int(input()),int(input()),int(input())
if length>l and width>w:
    print('Upload')
elif length<l:
    print('Increase Length')
elif width<w:
    print('Increase Width')