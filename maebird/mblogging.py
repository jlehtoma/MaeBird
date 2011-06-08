#!/usr/bin/python
# coding=utf-8

# Copyright (c) 2010 Rafa Muñoz Cárdenas
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#   * Neither the name of Pioneers of the Inevitable, Songbird, nor the names
#     of its contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import traceback
import logging.config
from types import IntType, BooleanType
import inspect

from config import __LOGGING__

# TODO: logging.ini should live outside source folder
if os.path.exists(__LOGGING__):
    log_config = __LOGGING__
else:
    raise IOError('No logging.ini file found')

# TODO: args[0] approach in the following decorators is not safe

def addLineNo(logFunction):
    def wrapper(self, *args, **kwargs):
        lineno = inspect.currentframe().f_back.f_lineno
        linemsg = 'line %s: ' % lineno
        msg = linemsg + str(args[0])
        logFunction(self, msg)
    return wrapper

def addStack(logFunction):
    def wrapper(self, *args, **kwargs):
        msg = args[0]
        if self.gui:
            stackmsg = ''.join(traceback.format_exc())
            msg += stackmsg
        logFunction(self, msg)
    return wrapper

class Singleton(object):
    """
    Singleton interface:
    http://www.python.org/download/releases/2.2.3/descrintro/#__new__
    """
    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        pass

class LoggerManager(Singleton):
    """
    Logger Manager.
    Handles all logging files.
    """
    def __init__(self, loggingdir='~'):
        # Set up default log file location
        logging.config.fileConfig(log_config, defaults={'logdir': loggingdir})
        self.logger = logging.getLogger()
        self.__gui = False
        
    def _get_gui(self):
        return self.__gui
    
    def _set_gui(self, value):
        assert type(value) is BooleanType or type(value) is IntType, \
               'GUI toggle value cannot be evaluated as boolean'
               
        if value:
            self.__gui = True
        else:
            self.__gui = False
        
    def debug(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        self.logger.debug(msg)

    def error(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        self.logger.error(msg)
        
    def exception(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        self.logger.exception(msg)

    def info(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        self.logger.info(msg)

    def warning(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        self.logger.warning(msg)
        
    _gui = property(_get_gui, _set_gui, None, '')

class Logger(object):
    """
    Logger object.
    """
    def __init__(self, loggername="root", loggingdir='~', debugging=False):
        self.lm = LoggerManager(loggingdir) # LoggerManager instance
        self.loggername = loggername # logger name
        self.__debugging = debugging
        # TODO: strings should be replaced with ints form LOG
        self.levels = {'debug': self.debug, 'info': self.info, 
                       'warning': self.warning, 'error': self.error,
                       'exception': self.exception}
        # List holds arbitrary history information that can be stored (pickled)
        self._results = []
        
    def get_debugging(self):
        return self.__debugging
        
    def set_debugging(self, value):
        assert type(value) is BooleanType or type(value) is IntType, \
               'Debug toggle value must be evaluated as boolean'
        if value:
            self.__debugging = True
        else:
            self.__debugging = False

    def get_gui(self):
        return self.lm._gui
    
    def set_gui(self, value):
        assert type(value) is BooleanType or type(value) is IntType, \
               'GUI toggle value cannot be evaluated as boolean'
               
        if value:
            self.lm._gui = True
        else:
            self.lm._gui = False

    @addLineNo
    def debug(self, msg):
        if self.debugging:
            self.lm.debug(self.loggername, msg)

    @addLineNo
    def error(self, msg):
        self.lm.error(self.loggername, msg)
        
    @addLineNo
    def exception(self, msg):
        self.lm.exception(self.loggername, msg)

    def info(self, msg):
        self.lm.info(self.loggername, msg)

    def warning(self, msg):
        self.lm.warning(self.loggername, msg)
        
    debugging = property(get_debugging, set_debugging, None, '')
    gui = property(get_gui, set_gui, None, '')  
        
if __name__ == '__main__':
    logger = Logger('root')
    logger.debug('Debugging')
    logger.info('Infoing')
    obj = {'foo': 'bar', 'spam': 'eggs'}
    logger.info('More info with an object')
    logger.warning('Warning!')
    logger.error('Error!!!')
#    try:
#        raise StandardError
#    except StandardError, e:
#        logger.exception('Oh dear, an exception occurred: %s.' % e)