from repeating_word import RepeatingWord

class TestClass:
    # def test_one(self):
    #     x = "this"
    #     assert "h" in x

    # def test_two(self):
    #     x = "hello"
    #     assert hasattr(x, "check")
    
    def test_three(self):
        rw = RepeatingWord()
        result = rw.Find_repeated()
        assert result