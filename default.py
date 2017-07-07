################################################################################
#      This file is part of OpenELEC - http://www.openelec.tv
#      Copyright (C) 2009-2012 Stephan Raue (stephan@openelec.tv)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with OpenELEC.tv; see the file COPYING.  If not, write to
#  the Free Software Foundation, 51 Franklin Street, Suite 500, Boston, MA 02110, USA.
#  http://www.gnu.org/copyleft/gpl.html
################################################################################
import xbmc,xbmcaddon,xbmcgui
import os

dialog = xbmcgui.Dialog()
if dialog.yesno('This is addon runs from within Tvheadend', 'Add your zap2it/screener/tvguide login info in the addon configuration.  Then reboot and setup the grabber channels in tvheadend before enabling the other options.', 'Would you like to open the addon settings?'):
    xbmcaddon.Addon().openSettings()
if dialog.yesno('Clear the listings cache', 'Would you like to clear the listings cache?', 'This might be needed to download updated "favorite" channels.'):
    scandirs = xbmc.translatePath(
    'special://home/addons/script.module.zap2xml/cache'
    )
    path = scandirs
    exts = ('html.gz')
    if os.path.exists(scandirs):
        for root, dirs, files in os.walk(path):
            for currentFile in files:
                if any(currentFile.lower().endswith(exts) for ext in exts):
                    os.remove(os.path.join(root, currentFile))
