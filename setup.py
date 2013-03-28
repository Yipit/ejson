# ejson - Extensible json serializer/deserializer library
#
# Copyright (c) 2012-2013  Lincoln Clarete <lincoln@comum.org>
# Copyright (c) 2012-2013  Yipit, Inc <coders@yipit.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(
        name="ejson",
        license="GPL",
        version='0.1.0',
        description=u'Extensible json serializer/deserializer library',
        long_description=open('README.md').read(),
        author=u'Lincoln de Sousa',
        author_email=u'lincoln@comum.org',
        url='https://github.com/Yipit/ejson',
        packages=filter(lambda n: not n.startswith('tests'), find_packages()),
        classifiers=(
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Natural Language :: English',
            'Operating System :: Microsoft',
            'Operating System :: POSIX',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
        )
    )
