import unittest

from multi_model import build_payload, task_id


class MultiModelTests(unittest.TestCase):
    def test_chat_payload(self):
        path, payload = build_payload("chat", "model-a", "hello")
        self.assertEqual(path, "/chat/completions")
        self.assertEqual(payload["messages"][0]["content"], "hello")

    def test_video_payload(self):
        path, payload = build_payload("video", "video-a", "waves", 8)
        self.assertEqual(path, "/videos/generations")
        self.assertEqual(payload["duration"], 8)

    def test_nested_task_id(self):
        self.assertEqual(task_id({"data": {"task_id": "abc"}}), "abc")


if __name__ == "__main__":
    unittest.main()
