from history import History


class TestHistory:
    def test_empty(self):
        h = History()
        assert h.show() == []
        assert len(h) == 0

    def test_add_and_show(self):
        h = History()
        h.add("2 + 3", 5)
        h.add("10 / 2", 5.0)
        assert len(h) == 2
        assert h.show() == [("2 + 3", 5), ("10 / 2", 5.0)]

    def test_show_limit(self):
        h = History()
        for i in range(20):
            h.add(f"expr{i}", i)
        assert len(h.show(5)) == 5
        assert h.show(5)[0] == ("expr15", 15)

    def test_clear(self):
        h = History()
        h.add("1 + 1", 2)
        h.clear()
        assert h.show() == []
        assert len(h) == 0
