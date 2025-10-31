import unittest
from unittest.mock import patch, MagicMock
from employee_repository import EmpRepo

class EmpRepoTest(unittest.TestCase):

    @patch("employee_repository.requests.get")
    def test_fetch_ok(self, mock_get):
        m = MagicMock()
        m.status_code = 200
        m.json.return_value = [
            {"id": 3, "name": "Alice", "position": "Developer"},
            {"id": 1, "name": "Bob", "position": "Manager"},
            {"id": 2, "name": "Charlie", "position": "Designer"}
        ]
        mock_get.return_value = m
        e = EmpRepo()
        res = e.fetch()
        self.assertEqual(res[0]["id"], 1)
        self.assertEqual(res[-1]["id"], 3)
        self.assertEqual(len(res), 3)

    @patch("employee_repository.requests.get")
    def test_ordering(self, mock_get):
        r = MagicMock()
        r.status_code = 200
        r.json.return_value = [
            {"id": 5, "name": "C"},
            {"id": 2, "name": "A"},
            {"id": 3, "name": "B"}
        ]
        mock_get.return_value = r
        out = EmpRepo().fetch()
        ids = [x["id"] for x in out]
        self.assertEqual(ids, sorted(ids))

    @patch("employee_repository.requests.get")
    def test_bad_status(self, mock_get):
        r = MagicMock()
        r.status_code = 500
        mock_get.return_value = r
        with self.assertRaises(Exception):
            EmpRepo().fetch()

if __name__ == "__main__":
    unittest.main()
