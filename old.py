import platform,os
os.system("git pull")
bit = platform.architecture()[0]
if bit == '64bit':
    import old
elif bit == '32bit':
    import old