from configgraph import ConfigGraph
from handlerdoc import HandlerDoc


def setup(app):
    app.add_directive('agxconfiggraph', ConfigGraph)
    app.add_directive('agxhandlerdoc', HandlerDoc)
