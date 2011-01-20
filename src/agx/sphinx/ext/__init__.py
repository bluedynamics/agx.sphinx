# -*- coding: utf-8 -*-
# Copyright BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2

from configgraph import ConfigGraph
from handlerdoc import HandlerDoc

def setup(app):
    app.add_directive('agxconfiggraph', ConfigGraph)
    app.add_directive('agxhandlerdoc', HandlerDoc)