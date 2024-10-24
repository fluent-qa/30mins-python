
import os
import sys

from spells.iceshell.tools.SelfCheck import SelfCheck
from spells.logs.iprint import iPrintLog

sys.path.append("..")



unready = SelfCheck.LibCheckNative()

if len(unready) == 0:
    iPrintLog("Nothing to download", "Downlib", "Main", "warning")
    exit(0)

iPrintLog("Ready to download", "Downlib", "Main", "info")
for lib in unready:
    os.system("pip install "+lib)
    iPrintLog(lib + " download!", "Downlib", "Main", "success")

iPrintLog("Download Finish!", "Downlib", "Main", "success")
