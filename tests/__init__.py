import os
import sys

sys.path.extend(
    [
        os.path.join(os.getcwd(),"src"),
        os.path.join(os.getcwd(), "src", "demo_package_lavajuno"),
    ]
)

from . import test_demo
