from schemoji import parse

def run():
    program = "👉👌 👉define r 10👈 👉* pi 👉* r r👈👈👈"
    print(parse(program))


if __name__ == '__main__':
    run()