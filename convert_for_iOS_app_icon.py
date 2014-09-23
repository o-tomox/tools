# -*- coding: utf-8 -*-


import os
import Image
from optparse import OptionParser


def prepare_options():
    usage = "usage: %prog [options] filename"

    parser = OptionParser(usage)

    # iPhone用
    parser.add_option(
        "--iPhone",
        action="append_const",
        const="iPhone",
        dest="devices",
        help="make icon for iPhone app"
    )

    # iPad用
    parser.add_option(
        "--iPad",
        action="append_const",
        const="iPad",
        dest="devices",
        help="make icon for iPad app"
    )

    # iOS7用
    parser.add_option(
        "--iOS7",
        action="append_const",
        const="iOS7",
        dest="versions",
        help="make icon for iOS 7 and later"
    )

    # iOS6用
    parser.add_option(
        "--iOS6",
        action="append_const",
        const="iOS6",
        dest="versions",
        help="make icon for iOS 5 or iOS 6 and earlier"
    )

    # アプリアイコン用
    parser.add_option(
        "--AppIcon",
        action="append_const",
        const="AppIcon",
        dest="icons",
        help="make app icon"
    )

    # 設定用
    parser.add_option(
        "--Settings",
        action="append_const",
        const="Settings",
        dest="icons",
        help="make icon for settings"
    )

    # スポットライト用
    parser.add_option(
        "--Spotlight",
        action="append_const",
        const="Spotlight",
        dest="icons",
        help="make icon for spotlight"
    )

    # Artwork用
    parser.add_option(
        "--Artwork",
        action="append_const",
        const="Artwork",
        dest="icons",
        help="make appicon for setting and spotlight"
    )

    # 低解像度用
    parser.add_option(
        "--low",
        action="append_const",
        const="low",
        dest="resolutions",
        help="make low-resolution icon"
    )

    # 高解像度用
    parser.add_option(
        "--high",
        action="append_const",
        const="high",
        dest="resolutions",
        help="make high-resolution icon"
    )

    (options, args) = parser.parse_args()

    if not args:
        parser.error("requires filename")

    if not options.devices:
        devices = ["iPhone", "iPad"]
    else:
        devices = options.devices

    if not options.versions:
        versions = ["iOS6", "iOS7"]
    else:
        versions = options.versions

    if not options.icons:
        icons = ["AppIcon", "Settings", "Spotlight", "Artwork"]
    else:
        icons = options.icons

    if not options.resolutions:
        resolutions = ["low", "high"]
    else:
        resolutions = options.resolutions

    return (args[0], devices, versions, icons, resolutions)


def make_icon(filename, devices, versions, icons, resolutions):
    filedatas = {"iPhone-iOS6-AppIcon": ("Icon", 57, 57),
                 "iPhone-iOS6-Settings": ("Icon-Small", 29, 29),
                 "iPhone-iOS6-Spotlight": ("Icon-Small", 29, 29),
                 "iPhone-iOS7-AppIcon": ("Icon-60", 60, 60),
                 "iPhone-iOS7-Settings": ("Icon-Small", 29, 29),
                 "iPhone-iOS7-Spotlight": ("Icon-Small-40", 40, 40),
                 "iPad-iOS6-AppIcon": ("Icon-72", 72, 72),
                 "iPad-iOS6-Settings": ("Icon-Small-50", 50, 50),
                 "iPad-iOS6-Spotlight": ("Icon-Small-50", 50, 50),
                 "iPad-iOS7-AppIcon": ("Icon-76", 76, 76),
                 "iPad-iOS7-Settings": ("Icon-Small", 29, 29), 
                 "iPad-iOS7-Spotlight": ("Icon-Small-40", 40, 40)
                }

    original = Image.open(filename)

    for icon in icons:
        resized_filename = []

        if icon != "Artwork":
            for device in devices:
                for version in versions:
                    filedata = filedatas["-".join([device, version, icon])]
                    new_filename = filedata[0]
                    width = filedata[1]
                    height = filedata[2]

                    if new_filename in resized_filename:
                        continue

                    for resolution in resolutions:
                        if resolution == "high":
                            new_filename += "@2x"
                            width *= 2
                            height *= 2
                        resize_icon(original, new_filename, width, height)
                        resized_filename.append(new_filename)
        else:
            new_filename = "iTunesArtwork"
            width = 512
            height = 512

            for resolution in resolutions:
                if resolution == "high":
                    new_filename += "@2x"
                    width *= 2
                    height *= 2
                resize_icon(original, new_filename, width, height, extension="")


def resize_icon(original, new_filename, width, height, extension=".png"):
    copy_icon = original.copy()
    copy_icon.resize((width, height), Image.ANTIALIAS).save(new_filename + extension, "PNG")
    print "resized icon - {0} ({1} x {2})".format(new_filename + extension, width, height)


if __name__ == '__main__':
    (filename, devices, versions, icons, resolutions) = prepare_options()
    make_icon(filename, devices, versions, icons, resolutions)






