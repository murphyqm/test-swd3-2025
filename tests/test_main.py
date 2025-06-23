import amazing_project as ap

def test_hello_world(capsys):
    ap.hello_world()
    captured = capsys.readouterr()
    assert captured[0] == "Hello World\n"

def test_speak(capsys):
    test_input = "wow!"
    ap.speak(test_input)
    captured = capsys.readouterr()
    assert captured[0] == "wow!\n"

# def test_shout(input):
#     print(f"{input}!!!")