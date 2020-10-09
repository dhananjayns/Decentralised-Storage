from pydub import AudioSegment
audio=[]
def split_audio(file):
    sound = AudioSegment.from_mp3(file)

    halfway_point=len(sound)/2
    quarter_point = len(sound) / 4
    first_quarter=sound[0:quarter_point]
    second_quarter = sound[quarter_point+1:halfway_point]
    third_quarter=sound[halfway_point+1:3*quarter_point]
    fourth_quarter=sound[3*quarter_point:]

    # first_quarter.export('1.mp3')
    # second_quarter.export('2.mp3')
    # third_quarter.export('3.mp3')
    # fourth_quarter.export('4.mp3')
    audio.append(first_quarter)
    audio.append(second_quarter)
    audio.append(third_quarter)
    audio.append(fourth_quarter)
    return audio
split_audio("Ed_Sheeran_-_Shape_of_You_[Official_Video](256k).mp3")
def join_audio(audio):
    full=AudioSegment.empty()
    for i in audio:
        full=full+i
    return full.export("file.mp3",format="mp3")
join_audio(audio)
