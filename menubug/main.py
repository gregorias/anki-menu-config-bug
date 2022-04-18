# -*- coding: utf-8 -*-
"""A trivial plugin showcasing a bug."""

import aqt  # type: ignore
from aqt import mw  # type: ignore

def setup_menu():
    def configure():
        pass

    print("Configuring buttons.")
    mw.form.menuTools.addAction(
        aqt.qt.QAction("Configure This Plugin", mw, triggered=configure))
    mw.form.menuTools.addAction(
        aqt.qt.QAction("C", mw, triggered=configure))
    mw.form.menuTools.addAction(
        aqt.qt.QAction("Configur", mw, triggered=configure))
    mw.form.menuTools.addAction(
        aqt.qt.QAction("Con", mw, triggered=configure))
    mw.form.menuTools.addAction(
        aqt.qt.QAction("Configu", mw, triggered=configure))
    mw.form.menuTools.addAction(
        aqt.qt.QAction("Conf", mw, triggered=configure))
    mw.form.menuTools.addAction(
        aqt.qt.QAction("Config", mw, triggered=configure))
    mw.form.menuTools.addAction(
        aqt.qt.QAction("Confi", mw, triggered=configure))
    mw.form.menuTools.addAction(
        aqt.qt.QAction("Just a random text", mw, triggered=configure))

setup_menu()
