import agx.core
import zope.component
from zope.component import getUtility
from zope.configuration.xmlconfig import XMLConfig
from agx.core.interfaces import (
    IConfLoader,
    ITransform,
    IScope,
    ITargetHandler,
)
from agx.core import (
    Processor,
    Dispatcher,
)


class AGXInfo(object):

    @property
    def confloader(self):
        return getUtility(IConfLoader)

    def load_agx_config(self):
        import agx.core.loader
        XMLConfig('meta.zcml', zope.component)()
        XMLConfig('configure.zcml', agx.core)()
        confloader = self.confloader
        confloader()

    def read_agx(self):
        ret = list()
        transforms = self.confloader.transforms
        for name in transforms:
            transform = getUtility(ITransform, name=name)
            transform_dict = dict()
            transform_dict['name'] = transform.name
            transform_dict['transform'] = transform
            transform_dict['generators'] = list()
            ret.append(transform_dict)
            generators = Processor(transform.name).lookup_generators()
            for generator in generators:
                generator_dict = dict()
                generator_dict['name'] = generator.name
                generator_dict['description'] = generator.description
                generator_dict['handler'] = list()
                targethandler = getUtility(ITargetHandler, name=generator.name)
                generator_dict['targethandler'] = targethandler
                transform_dict['generators'].append(generator_dict)
                handlers = Dispatcher(generator.name).lookup_handlers()
                for handler in handlers:
                    handler_dict = dict()
                    handler_dict['name'] = handler.name
                    handler_dict['order'] = handler.order
                    if handler.scope:
                        scopename = '%s.%s' % (transform_dict['name'],
                                               handler.scope)
                        scope = getUtility(IScope, name=scopename)
                        handler_dict['scope'] = {
                            'name': scopename,
                            'class': scope.__class__
                        }
                    else:
                        handler_dict['scope'] = None
                    package_path = [handler._callfunc.__module__,
                                    handler._callfunc.func_code.co_name]
                    package_path = '.'.join(package_path)
                    handler_dict['package_path'] = package_path
                    generator_dict['handler'].append(handler_dict)
        return ret
