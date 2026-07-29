import sys

from metomi.rose.upgrade import MacroUpgrade  # noqa: F401

from .version31_32 import *


class UpgradeError(Exception):
    """Exception created when an upgrade fails."""

    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        sys.tracebacklimit = 0
        return self.msg

    __str__ = __repr__


class vn32_t669(MacroUpgrade):
    """Upgrade macro for ticket #669 by John Rostron."""

    BEFORE_TAG = "vn3.2"
    AFTER_TAG = "vn3.2_t669"

    def upgrade(self, config, meta_config=None):
        # Commands From: rose-meta/um-convection
        # Set default value to previous constant values
        self.add_setting(config, ["namelist:convection", "eff_dcff"], "3.0")
        self.add_setting(config, ["namelist:convection", "eff_dcfl"], "1.0")

        return config, self.reports
