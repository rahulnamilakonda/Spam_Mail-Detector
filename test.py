server=1
def func():
    global server
    server=2
    print(server)
func()
print(server)