import asyncio
import pytest

enable_visual_inspection = False

class Visualize:

    def wait(time):
        if enable_visual_inspection == True:
            asyncio.sleep(time)
