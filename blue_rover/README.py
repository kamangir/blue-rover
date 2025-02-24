import os

from blue_objects import file, README

from blue_rover import NAME, VERSION, ICON, REPO_NAME


items = README.Items(
    [
        {
            "name": "blue-rover",
            "marquee": "https://github.com/waveshareteam/ugv_rpi/raw/main/media/UGV-Rover-details-23.jpg",
            "description": "[UGV Beast PI ROS2](https://www.waveshare.com/wiki/UGV_Beast_PI_ROS2).",
        },
        {
            "name": "blue-donkey",
            "marquee": "https://github.com/kamangir/blue-bracket/raw/main/images/blue-donkey-2.jpg",
            "description": "based on [Donkey Car](https://docs.donkeycar.com/).",
            "url": "https://github.com/kamangir/blue-bracket/blob/main/designs/blue-donkey.md",
        },
        {
            "name": "skateboard",
            "marquee": "https://github.com/kamangir/blue-bracket/raw/main/images/skateboard-1.jpg",
            "description": "self-driving electric skateboard (concept)",
            "url": "https://github.com/kamangir/blue-bracket/blob/main/designs/skateboard.md",
        },
    ]
)


def build():
    return README.build(
        items=items,
        path=os.path.join(file.path(__file__), ".."),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    )
