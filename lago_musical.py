songs = [
    ["brr", "fiu", "cric-cric", "brrah"],
    ["pep", "birip", "trri-trri", "croac"],
    ["bri-bri", "plop", "cric-cric", "brrah"]
]

def searchNextSoundsFromSong(sound):
    for song in songs:
        if sound in song:
            index = song.index(sound)
            if (index + 1) == len(song):
                return ""
            return ", " .join(song[index+ 1:])
    return ""

def Program():
    while True:
        inputSound = input('Enter a sound (or "exit" to quit): ')
        if inputSound.lower() == 'exit':
            print('Exiting...')
            break
        else:
            sounds = searchNextSoundsFromSong(inputSound)
            if sounds:
                print('Remaining sounds: ', sounds)
            else:
                print('No remaining sounds or the sound was not found.') 

Program()