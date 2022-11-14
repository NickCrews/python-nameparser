Release Log
===========
* 1.1.2 - November 13, 2022
    - Add support for attributes in constructor (#140)
* 1.1.1 - January 28, 2022
    - Fix bug in is_suffix handling of lists (#129)
* 1.1.0 - January 3, 2022
    - Add initials support (#128)
    - Add more titles and prefixes (#120, #127, #128, #119)
* 1.0.6 - February 8, 2020
    - Fix Python 3.8 syntax error (#104)
* 1.0.5 - Dec 12, 2019
    - Fix suffix parsing bug in comma parts (#98)
    - Fix deprecation warning on Python 3.7 (#94)
    - Improved capitalization support of mixed case names (#90)
    - Remove "elder" from titles (#96)
    - Add post-nominal list from Wikipedia to suffixes (#93)
* 1.0.4 - June 26, 2019
    - Better nickname handling of multiple single quotes (#86)
    - full_name attribute now returns formatted string output instead of original string (#87)
* 1.0.3 - April 18, 2019
    - fix sys.stdin usage when stdin doesn't exist (#82)
    - support for escaping log entry arguments (#84)
* 1.0.2 - Oct 26, 2018
    - Fix handling of only nickname and last name (#78)
* 1.0.1 - August 30, 2018
    - Fix overzealous regex for "Ph. D." (#43)
    - Add `surnames` attribute as aggregate of middle and last names
* 1.0.0 - August 30, 2018
    - Fix support for nicknames in single quotes (#74)
    - Change prefix handling to support prefixes on first names (#60)
    - Fix prefix capitalization when not part of lastname (#70)
    - Handle erroneous space in "Ph. D." (#43)
* 0.5.8 - August 19, 2018
    - Add "Junior" to suffixes (#76)
    - Add "dra" and "srta" to titles (#77)
* 0.5.7 - June 16, 2018
    - Fix doc link (#73)
    - Fix handling of "do" and "dos" Portuguese prefixes (#71, #72)
* 0.5.6 - January 15, 2018
    - Fix python version check (#64)
* 0.5.5 - January 10, 2018
    - Support J.D. as suffix and Wm. as title
* 0.5.4 - December 10, 2017
    - Add Dr to suffixes (#62)
    - Add the full set of Italian derivatives from "di" (#59)
    - Add parameter to specify the encoding of strings added to constants, use 'UTF-8' as fallback (#67)
    - Fix handling of names composed entirely of conjunctions (#66)
* 0.5.3 - June 27, 2017
    - Remove emojis from initial string by default with option to include emojis (#58)
* 0.5.2 - March 19, 2017
    - Added names scrapped from VIAF data, thanks daryanypl (#57)
* 0.5.1 - August 12, 2016
    - Fix error for names that end with conjunction (#54)
* 0.5.0 - August 4, 2016
    - Refactor join_on_conjunctions(), fix #53
* 0.4.1 - July 25, 2016
    - Remove "bishop" from titles because it also could be a first name
    - Fix handling of lastname prefixes with periods, e.g. "Jane St. John" (#50)
* 0.4.0 - June 2, 2016
    - Remove "CONSTANTS.suffixes", replaced by "suffix_acronyms" and "suffix_not_acronyms" (#49)
    - Add "du" to prefixes
    - Add "sheikh" variations to titles
    - Add parameter to force capitalization of mixed case strings
* 0.3.16 - March 24, 2016
    - Clarify LGPL licence version (#47)
    - Skip pickle tests if pickle not installed (#48)
* 0.3.15 - March 21, 2016
    - Fix string format when `empty_attribute_default = None` (#45)
    - Include tests in release source tarball (#46)
* 0.3.14 - March 18, 2016
    - Add `CONSTANTS.empty_attribute_default` to customize value returned for empty attributes (#44)
* 0.3.13 - March 14, 2016
    - Improve string format handling (#41)
* 0.3.12 - March 13, 2016
    - Fix first name clash with suffixes (#42)
    - Fix encoding of constants added via the python shell
    - Add "MSC" to suffixes, fix #41
* 0.3.11 - October 17, 2015
    - Fix bug capitalization exceptions (#39)
* 0.3.10 - September 19, 2015
    - Fix encoding of byte strings on python 2.x (#37)
* 0.3.9 - September 5, 2015
    - Separate suffixes that are acronyms to handle periods differently, fixes #29, #21
    - Don't find titles after first name is filled, fixes (#27)
    - Add "chair" titles (#37)
* 0.3.8 - September 2, 2015
    - Use regex to check for roman numerals at end of name (#36)
    - Add DVM to suffixes
* 0.3.7 - August 30, 2015
    - Speed improvement, 3x faster
    - Make HumanName instances pickleable
* 0.3.6 - August 6, 2015
    - Fix strings that start with conjunctions (#20)
    - handle assigning lists of names to a name attribute
    - support dictionary-like assignment of name attributes
* 0.3.5 - August 4, 2015
    - Fix handling of string encoding in python 2.x (#34)
    - Add support for dictionary key access, e.g. name['first']
    - add 'santa' to prefixes, add 'cpa', 'csm', 'phr', 'pmp' to suffixes (#35)
    - Fix prefixes before multi-part last names (#23)
    - Fix capitalization bug (#30)
* 0.3.4 - March 1, 2015
    - Fix #24, handle first name also a prefix
    - Fix #26, last name comma format when lastname is also a title
* 0.3.3 - Aug 4, 2014
    - Allow suffixes to be chained (#8)
    - Handle trailing suffix in last name comma format (#3). Removes support for titles
      with periods but no spaces in them, e.g. "Lt.Gen.". (#21)
* 0.3.2 - July 16, 2014
    - Retain original string in "original" attribute.
    - Collapse white space when using custom string format.
    - Fix #19, single comma name format may have trailing suffix
* 0.3.1 - July 5, 2014
    - Fix Pypi package, include new config module.
* 0.3.0 - July 4, 2014
    - Refactor configuration to simplify modifications to constants (backwards incompatible)
    - use unicode_literals to simplify Python 2 & 3 support.
    - Generate documentation using sphinx and host on readthedocs.
* 0.2.10 - May 6, 2014
    - If name is only a title and one part, assume it's a last name instead of a first name, with exceptions for some titles like 'Sir'. (`#7 <https://github.com/derek73/python-nameparser/issues/7>`_).
    - Add some judicial and other common titles. (#9)
* 0.2.9 - Apr 1, 2014
    - Add a new nickname attribute containing anything in parenthesis or double quotes (`Issue 33 <https://code.google.com/p/python-nameparser/issues/detail?id=33>`_).
* 0.2.8 - Oct 25, 2013
    - Add support for Python 3.3+. Thanks to @corbinbs.
* 0.2.7 - Feb 13, 2013
    - Fix bug with multiple conjunctions in title
    - add legal and crown titles
* 0.2.6 - Feb 12, 2013
    - Fix python 2.6 import error on logging.NullHandler
* 0.2.5 - Feb 11, 2013
    - Set logging handler to NullHandler
    - Remove 'ben' from PREFIXES because it's more common as a name than a prefix.
    - Deprecate BlankHumanNameError. Do not raise exceptions if full_name is empty string.
* 0.2.4 - Feb 10, 2013
    - Adjust logging, don't set basicConfig. Fix `Issue 10 <https://code.google.com/p/python-nameparser/issues/detail?id=10>`_ and `Issue 26 <https://code.google.com/p/python-nameparser/issues/detail?id=26>`_.
    - Fix handling of single lower case initials that are also conjunctions, e.g. "john e smith". Re `Issue 11 <https://code.google.com/p/python-nameparser/issues/detail?id=11>`_.
    - Fix handling of initials with no space separation, e.g. "E.T. Jones". Fix #11.
    - Do not remove period from first name, when present.
    - Remove 'e' from PREFIXES because it is handled as a conjunction.
    - Python 2.7+ required to run the tests. Mark known failures.
    - tests/test.py can now take an optional name argument that will return repr() for that name.
* 0.2.3 - Fix overzealous "Mac" regex
* 0.2.2 - Fix parsing error
* 0.2.0
    - Significant refactor of parsing logic. Handle conjunctions and prefixes before
      parsing into attribute buckets.
    - Support attribute overriding by assignment.
    - Support multiple titles.
    - Lowercase titles constants to fix bug with comparison.
    - Move documentation to README.rst, add release log.
* 0.1.4 - Use set() in constants for improved speed. setuptools compatibility - sketerpot
* 0.1.3 - Add capitalization feature - twotwo
* 0.1.2 - Add slice support

