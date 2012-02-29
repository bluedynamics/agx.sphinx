# -*- coding: utf-8 -*-
# Copyright BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2

from sphinx.ext.graphviz import (
    Graphviz,
    graphviz,
)
from util import AGXInfo

class ConfigGraph(Graphviz, AGXInfo):

    def run(self):
        dotcode = self.dotcode()
        if not dotcode.strip():
            return [self.state_machine.reporter.warning(
                'Ignoring "graphviz" directive without content.',
                line=self.lineno)]
        node = graphviz()
        node['code'] = dotcode
        node['options'] = []
        return [node]

    def dotcode(self):
        self.load_agx_config()
        agx_defs = self.read_agx()
        defs = self._defs()
        connections = self._connections()
        ret = list()
        
        ret.append('digraph agxconfig {')

        ret.append('size = "20,30"')
        ret.append('page = "20,30"')
        
        ret.append('ratio = "fill"')

        ret.append('ranksep = "0.2 equal"')
        ret.append('nodesep = "0.2 equal"')
        
        ret.append('rankdir = "LR"')
        
        body = connections + defs
        body.sort()
        ret += body
        
        ret.append('}')
        
        return '\n'.join(ret)

    def _defs(self):
        agx_defs = self.read_agx()
        defs = set()
        for transform in agx_defs:
            id = transform['name']
            label = self._t_name(id)
            def_ = self._graph_def_line(id, label, 0)
            defs.add(def_)
            for generator in transform['generators']:
                id = generator['name']
                label = self._g_name(id)
                def_ = self._graph_def_line(id, label, 1)
                defs.add(def_)
                targethandler = generator['targethandler']
                id = '%s.%s' % (targethandler.__module__,
                                targethandler.__class__.__name__)
                label = self._th_name(id)
                def_ = self._graph_def_line(id, label, 4)
                defs.add(def_)
                for handler in generator['handler']:
                    id = handler['name']
                    label = self._h_name(id)
                    name = handler['name'][handler['name'].rfind('.') + 1:]
                    def_ = self._graph_def_line(id, label, 2)
                    defs.add(def_)
                    if handler['scope']:
                        id = handler['scope']['name']
                        name = handler['scope']['class'].__name__
                        label = self._s_name(id, name)
                        def_ = self._graph_def_line(id, label, 3)
                        defs.add(def_)
        return list(defs)

    def _connections(self):
        agx_defs = self.read_agx()
        connections = set()
        for transform in agx_defs:
            tr = transform['name']
            for generator in transform['generators']:
                gen = generator['name']
                connections.add(self._graph_conn_line(tr, gen,
                                                      arrowhead='none'))
                th = '%s.%s' % (generator['targethandler'].__module__,
                                generator['targethandler'].__class__.__name__)
                conn = self._graph_conn_line(th, gen,
                                             dir='back',
                                             style='dotted',
                                             arrowtail='none')
                connections.add(conn)
                for handler in generator['handler']:
                    han = handler['name']
                    connections.add(self._graph_conn_line(gen, han,
                                                          arrowhead='none'))
                    if handler['scope']:
                        sc = handler['scope']['name']
                        conn = self._graph_conn_line(han, sc,
                                                     style='dotted',
                                                     arrowhead='none')
                        connections.add(conn)
        return list(connections)

    _colors = {
        0: 'lightskyblue3',
        1: 'pink2',
        2: 'palegreen3',
        3: 'yellow2',
        4: 'tan2',
    }

    def _t_name(self, name):
        return '%s' % name.capitalize()

    def _g_name(self, name):
        return '%s' % name[name.rfind('.') + 1:].capitalize()

    def _h_name(self, name):
        return '%s' % name[name.rfind('.') + 1:].capitalize()

    def _s_name(self, name, impl):
        #return '%s::%s' % (name, impl)
        return '%s' % name

    def _th_name(self, name):
        return '%s' % name

    def _graph_def_line(self, id, label, level):
        label = "%s |" % label
        ret = '"%s" [style="filled",fillcolor="%s",label="%s",shape="Mrecord"]'
        return ret % (id, self._colors[level], label)

    def _graph_conn_line(self, a, b, **kw):
        opts = ','.join(['%s=%s' % (key, value) for key, value in kw.items()])
        if not opts:
            return '"%s" -> "%s"' % (a, b)
        else:
            return '"%s" -> "%s" [%s]' % (a, b, opts)