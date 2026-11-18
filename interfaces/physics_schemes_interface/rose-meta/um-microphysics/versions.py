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


class vn32_t925(MacroUpgrade):
    # Upgrade macro for #925 by John Rostron

    BEFORE_TAG = "vn3.2"
    AFTER_TAG = "vn3.2_t925"

    def upgrade(self, config, meta_config=None):
        # Set default values to previous hard-coded values
        self.add_setting(config, ["namelist:microphysics", "ar"], "1.0")
        self.add_setting(
            config, ["namelist:microphysics", "mp_tau_lim"], "1200.0"
        )
        self.add_setting(config, ["namelist:microphysics", "x1r"], "0.22")
        return config, self.reports
