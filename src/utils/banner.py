banner_path = "../resources/banner.txt"

def print_banner() :
    with open(banner_path, 'r', encoding='ascii', errors='ignore') as file:
        lines = file.readlines()
        line = ''
        for line in lines:
            print(line, end='')
