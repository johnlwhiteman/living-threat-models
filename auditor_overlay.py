import sys
import json
import unittest.mock

import dffml

from auditor import audit as untyped_audit
from parser import parse


@dffml.op
def audit(ltm: str) -> list:
    return untyped_audit(parse(ltm))


AUDITOR_OVERLAY = dffml.DataFlow(*dffml.opimp_in(sys.modules[__name__]))
