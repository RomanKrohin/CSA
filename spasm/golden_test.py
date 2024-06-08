import contextlib
import io
import logging
import os
import tempfile
from datetime import datetime

import pytest
from Start import start_work

from cpu.machine import Machine
from translate.parser import run


@pytest.mark.golden_test("golden/*.yml")
def test_machine_cat(golden,caplog):

    with tempfile.TemporaryDirectory() as tmpdirname:
        caplog.set_level(logging.INFO)
        source = os.path.join(tmpdirname, "source.SPASM")
        input_text = os.path.join(tmpdirname, "input.txt")

        with open(source, "w", encoding="utf-8") as file:
            file.write(golden["in_source"])
        with open(input_text, "w", encoding="utf-8") as file:
            file.write(golden["in_stdin"])
            
        start_work(source, input_text)
        
        assert golden.out["out_log"] == caplog.text
        
        os.remove(source)
        os.remove(input_text)
