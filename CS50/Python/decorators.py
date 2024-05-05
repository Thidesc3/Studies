def announce(f):
    def wrapper():
        print("run the function...")
        f()
        print("")