import pytest
from unittest.mock import MagicMock

from github_pr_comment import GithubPrManager, RequestManager

class TestClass:
    def test_one(self):
        rm = RequestManager('test/demo', 'no-token')
        rm.get_comments = MagicMock(return_value=[])
        rm.delete_comment = MagicMock(return_value=None)
        rm.post_comment = MagicMock(return_value=[])

        g = GithubPrManager(rm)

        assert len(g.split_content("hello world")) == 1

        assert len(g.split_content("A " * (GithubPrManager.GITHUB_COMMENT_MAX_CHARS + 100))) == 2
