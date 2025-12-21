def main():
    musics = getFile("Music.txt")
    users = getFile("Users.txt")

    musicTypes = []
    songDict = {}

    for i in range(len(musics)):
   
        for j in range(2, len(musics[i])):
            genre = musics[i][j].strip()
            if genre not in musicTypes:
                musicTypes.append(genre)

 
    for k in musicTypes:
        tempDict = {k: []}
        songDict.update(tempDict)

    for i in range(len(musics)):
        song_name = musics[i][0].strip()
        for j in range(2, len(musics[i])):
            genre = musics[i][j].strip()
            if song_name not in songDict[genre]:
                songDict[genre].append(song_name)

    
    userSum(users, songDict)


def getFile(name: str):
    infile = None
    content = []
    try:
        infile = open(name, "r")
        for line in infile:
            line = line.rstrip()
            if line.strip() == "":
                continue         
            content.append(line.split(";"))
    except IOError:
        print("File could not opened")
    finally:
        if infile:
            infile.close()
            print("Reading operation has been done successfuly")
        else:
            print("Reading operation has not been done successfuly")
        if not content:
            print("File has processed")

    return content


def userSum(users: list, songList: dict):
    for i in range(len(users)):
        name = users[i][0].strip()
        userSongs = []

        for j in range(1, len(users[i])):
            genre = users[i][j].strip()
            if genre in songList:
                for song in songList[genre]:
                    if song not in userSongs:   
                        userSongs.append(song)

        numSongs = len(userSongs)
        print(f'\n{name} (N of songs: {numSongs}):')
        for s in userSongs:
            print(f'- {s}')
        print


main()
