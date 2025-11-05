import tempfile
import pytest
from pathlib import Path


@pytest.fixture
def tmp_folder():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


