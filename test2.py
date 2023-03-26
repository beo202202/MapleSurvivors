import sounddevice as sd
import soundfile as sf
import threading


def play_music(file_path, volume, status):
    # 음악 파일 읽기
    data, fs = sf.read(file_path, dtype='float32')

    # 음량 조절
    data *= volume

    # 재생
    stream = sd.play(data, fs, blocking=False)
    sd.wait()

    return stream


def get_user_input(stream):
    while True:
        user_input = input("명령어 입력: ")

        if user_input == "일시정지":
            sd.stop()
        elif user_input == "재생":
            status = stream.get_status()
            sd.play(start=int(status['stop'] -
                    status['current']), blocking=False)
        elif user_input == "중지":
            sd.stop()
            break
        elif user_input.startswith("볼륨조절"):
            volume = float(user_input.split()[-1])
            stream.set_volume(volume)
        elif user_input.startswith("바꾸기"):
            filename = user_input.split()[-1]
            stream.stop()
            stream = play_music(filename, volume, status)

    return stream


if __name__ == "__main__":
    # 파일 경로와 볼륨 크기를 지정하여 재생
    file_path = "./sounds/Old_Main_Title.mp3"
    volume = 0.05  # 0.0 ~ 1.0

    # 음악 재생
    stream = play_music(file_path, volume, None)

    # 사용자 입력 스레드 시작
    input_thread = threading.Thread(target=get_user_input, args=(stream,))
    input_thread.start()

    # 재생이 끝나기 전까지 대기
    input_thread.join()

    # 스트림 종료
    stream.stop()
