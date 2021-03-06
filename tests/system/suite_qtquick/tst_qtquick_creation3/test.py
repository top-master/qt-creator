############################################################################
#
# Copyright (C) 2016 The Qt Company Ltd.
# Contact: https://www.qt.io/licensing/
#
# This file is part of Qt Creator.
#
# Commercial License Usage
# Licensees holding valid commercial Qt licenses may use this file in
# accordance with the commercial license agreement provided with the
# Software or, alternatively, in accordance with the terms contained in
# a written agreement between you and The Qt Company. For licensing terms
# and conditions see https://www.qt.io/terms-conditions. For further
# information use the contact form at https://www.qt.io/contact-us.
#
# GNU General Public License Usage
# Alternatively, this file may be used under the terms of the GNU
# General Public License version 3 as published by the Free Software
# Foundation with exceptions as appearing in the file LICENSE.GPL3-EXCEPT
# included in the packaging of this file. Please review the following
# information to ensure the GNU General Public License requirements will
# be met: https://www.gnu.org/licenses/gpl-3.0.html.
#
############################################################################

source("../../shared/qtcreator.py")

def main():
    startApplication("qtcreator" + SettingsPath)
    if not startedWithoutPluginError():
        return
    available = ["5.6"]

    for qtVersion in available:
        # using a temporary directory won't mess up a potentially existing
        workingDir = tempDir()
        projectName = createNewQtQuickUI(workingDir, qtVersion)
        kit = Targets.getStringForTarget(Targets.DESKTOP_5_6_1_DEFAULT)
        if addAndActivateKit(Targets.DESKTOP_5_6_1_DEFAULT):
            quick = "2.6"
        else:
            test.fatal("Failed to activate kit %s" % kit)
            continue
        test.log("Running project Qt Quick UI Prototype (%s)" % kit)
        qmlViewer = modifyRunSettingsForHookIntoQtQuickUI(2, 1, workingDir, projectName, 11223, quick)
        if qmlViewer!=None:
            qmlViewerPath = os.path.dirname(qmlViewer)
            qmlViewer = os.path.basename(qmlViewer)
            result = addExecutableAsAttachableAUT(qmlViewer, 11223)
            allowAppThroughWinFW(qmlViewerPath, qmlViewer, None)
            if result:
                result = runAndCloseApp(True, qmlViewer, 11223, sType=SubprocessType.QT_QUICK_UI, quickVersion=quick)
            else:
                result = runAndCloseApp(sType=SubprocessType.QT_QUICK_UI)
            removeExecutableAsAttachableAUT(qmlViewer, 11223)
            deleteAppFromWinFW(qmlViewerPath, qmlViewer)
        else:
            result = runAndCloseApp(sType=SubprocessType.QT_QUICK_UI)
        if result == None:
            checkCompile()
        else:
            appOutput = logApplicationOutput()
            test.verify(not ("untitled.qml" in appOutput or "MainForm.ui.qml" in appOutput),
                        "Does the Application Output indicate QML errors?")
        invokeMenuItem("File", "Close All Projects and Editors")
    invokeMenuItem("File", "Exit")
