# -*- coding: utf-8; -*-
"""
Copyright (C) 2007-2013 Guake authors

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
Boston, MA 02110-1301 USA
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import logging.config

try:
    from colorlog import ColoredFormatter
except ImportError as ie:
    ColoredFormatter = None

log = logging.getLogger(__name__)


def setupLogging(debug_mode):
    if debug_mode:
        base_logging_level = logging.DEBUG
    else:
        base_logging_level = logging.INFO

    if ColoredFormatter:
        logging.config.dictConfig({
            'version': 1,
            'disable_existing_loggers': False,
            'loggers': {
                '': {
                    'handlers': ['default'],
                    'level': 'DEBUG',
                    'propagate': True
                },
            },
            'handlers': {
                'default': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': "default",
                },
            },
            'formatters': {
                'default': {
                    '()': 'colorlog.ColoredFormatter',
                    'format': "%(log_color)s%(levelname)-8s%(reset)s %(message)s",
                    'log_colors': {
                        'DEBUG': 'cyan',
                        'INFO': 'green',
                        'WARNING': 'yellow',
                        'ERROR': 'red',
                        'CRITICAL': 'red,bg_white',
                    },
                }
            },
        })
    else:
        logging.basicConfig(level=base_logging_level)
    log.setLevel(base_logging_level)
    log.info("Logging configuration complete")
    log.debug("Debug mode enabled")
