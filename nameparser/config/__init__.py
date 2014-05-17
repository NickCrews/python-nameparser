# -*- coding: utf-8 -*-
"""
The :py:mod:`nameparser.config` module manages the configuration of the
nameparser. 

A module-level instance of :py:class:`~nameparser.config.Constants` is created
and used by default for all HumanName instances. You can adjust the entire module's
configuration by importing this instance and changing it.

::

    >>> from nameparser.config import constants
    >>> constants.titles.remove('hon').add('chemistry','dean')

You can also adjust the configuration of individual instances by passing
``None`` as the second argument upon instantiation.

::

    >>> from nameparser import HumanName
    >>> hn = HumanName("Dean Robert Johns", None)
    >>> hn.C.titles.add('dean')
    >>> hn.parse_full_name() # need to run this again after config changes

**Potential Gotcha**: If you do not pass ``None`` as the second argument,
``hn.C`` will be a reference to the module config, possibly yielding 
unexpected results. See `Customizing the Parser <customize.html>`_.
"""
from __future__ import unicode_literals
import collections

from nameparser.util import lc
from nameparser.config.prefixes import PREFIXES
from nameparser.config.capitalization import CAPITALIZATION_EXCEPTIONS
from nameparser.config.conjunctions import CONJUNCTIONS
from nameparser.config.suffixes import SUFFIXES
from nameparser.config.titles import TITLES
from nameparser.config.titles import FIRST_NAME_TITLES
from nameparser.config.regexes import REGEXES

class SetManager(collections.Set):
    '''
    Easily add and remove config variables per module or instance.
    
    Only special functionality beyond that provided by set() is
    to normalize constants for comparison (lower case, no periods)
    when they are add()ed and remove()d and allow passing multiple 
    string arguments to the :py:func:`add()` and :py:func:`remove()` methods.
    
    '''
    def __init__(self, elements):
        self.elements = set(elements)
    
    def __call__(self):
        return self.elements
    
    def __repr__(self):
        return "SetManager({})".format(self.elements) # used for docs
    
    def __iter__(self):
        return iter(self.elements)
    
    def __contains__(self, value):
        return value in self.elements
    
    def __len__(self):
        return len(self.elements)
    
    def next(self):
        return self.__next__()

    def __next__(self):
        if self.count >= len(self.elements):
            self.count = 0
            raise StopIteration
        else:
            c = self.count
            self.count = c + 1
            return getattr(self, self.elements[c]) or next(self)
    
    def add(self, *strings):
        """
        Add the lower case and no-period version of the string arguments to the set.
        Return's ``self`` for chaining.
        """
        [self.elements.add(lc(s)) for s in strings]
        return self
    
    def remove(self, *strings):
        """
        Remove the lower case and no-period version of the string arguments from the set.
        Return's ``self`` for chaining.
        """
        [self.elements.remove(lc(s)) for s in strings if lc(s) in self.elements]
        return self


class TupleManager(dict):
    '''
    A dictionary with dot.notation access. Subclass of ``dict``. Makes the tuple constants 
    more friendly.
    '''
    def __getattr__(self, attr):
        return self.get(attr)
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__


class Constants(object):
    """
    This class is used to hold all of the configuration for the parser.
    An instance of this class is available via 
    ``from nameparser.config import constants`` or on the
    ``C`` attribute of a :py:class:`~nameparser.parser.HumanName` instance, e.g. ``hn.C``.

    :param set prefixes: 
        :py:attr:`prefixes` wrapped with :py:class:`SetManager`.
        
        Parts that come before last names, e.g. 'del' or 'van'. 
      
    :param set titles: 
        :py:attr:`titles` wrapped with :py:class:`SetManager`.
        
        Parts that come before the first names. Any strings included in
        here will never be considered a first name, so use with care.
      
    :param set first_name_titles: 
        :py:attr:`first_name_titles` wrapped with :py:class:`SetManager`.
        
        When these titles appear with a single other name, that name is a first name, e.g.
        "Sir John", "Sister Mary", "Queen Elizabeth".
      
    :param set suffixes: 
        :py:attr:`suffixes`  wrapped with :py:class:`SetManager`.
        
        Parts that appear after the last name, e.g. "Jr." or "MD".
      
    :param set conjunctions: 
        :py:attr:`conjunctions`  wrapped with :py:class:`SetManager`.
        
        Parts that are used to join names together, e.g. "and", "y" and "&".
        "of" and "the" are also include to facilitate joining multiple titles,
        e.g. "President of the United States".
      
    :param capitalization_exceptions: 
        :py:attr:`capitalization_exceptions` wrapped with :py:class:`TupleManager`.
        
        Most parts should be capitalized by capitalizing the first letter.
        There are some exceptions, such as roman numbers used for suffixes.
        You can update this with a dictionary or a tuple. 
    :type capitalization_exceptions: tuple or dict
        
    :param regexes: 
        :py:attr:`regexes`  wrapped with :py:class:`TupleManager`.
        
        Contains all the various regular expressions used in the parser.
    :type regexes: tuple or dict
    """
    def __init__(self, 
                    prefixes=PREFIXES, 
                    suffixes=SUFFIXES,
                    titles=TITLES,
                    first_name_titles=FIRST_NAME_TITLES,
                    conjunctions=CONJUNCTIONS,
                    capitalization_exceptions=CAPITALIZATION_EXCEPTIONS,
                    regexes=REGEXES
                ):
        self.prefixes          = SetManager(prefixes)
        self.suffixes          = SetManager(suffixes)
        self.titles            = SetManager(titles)
        self.first_name_titles = SetManager(first_name_titles)
        self.conjunctions      = SetManager(conjunctions)
        self.capitalization_exceptions = TupleManager(capitalization_exceptions)
        self.regexes                = TupleManager(regexes)
    
    @property
    def suffixes_prefixes_titles(self):
        return self.prefixes | self.suffixes | self.titles
    
    def __repr__(self):
        return "<Constants() instance>"

#: A module-level instance of the :py:class:`Constants()` class. 
#: Provides a common instance for the module to share
#: to easily adjust configuration for the entire module.
#: See `Customizing the Parser with Your Own Configuration <customize.html>`_.
CONSTANTS = Constants()
