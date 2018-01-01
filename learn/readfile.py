def read_in_chunks(filepath, chun_size=1024):
    try:
        file = open(filepath)
    except FileNotFoundError:
        print("file not found")
        while True:
            data = file.read(chun_size)
            if not data:
                break
            yield data


if __name__ == '__main__':

    filepath = './readfile.py'

    for f in read_in_chunks(filepath):
        print(f)