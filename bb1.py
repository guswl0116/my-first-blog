name = 'ola'
if name == 'ola':
    print('Hey ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')
volume = 88
if volume < 20:
    print("It's kinda quiet.")
elif 20<=volume<40:
    print("It's nice for background music")
elif 40<=volume<60:
    print("Perfect, I can hear all the details")
elif 60<=volume<80:
    print("Nice for parties!")
else:
    print("My ears are hurting! :(")

if volume < 20 or volume > 80:
    volume = 10
    print("That's better")
    print(volume)
