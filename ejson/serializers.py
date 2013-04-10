# ejson - Copyright (c) 2013  Lincoln de Sousa <lincoln@comum.org>
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

"""Generic {de,}serializers that are usually useful

If you need them, I suggest you to either import this file or to call the
`ejson.load_default_handlers()`.
"""

import datetime
import decimal
from dateutil import parser
from . import register_serializer, register_deserializer


class TZInfoHelper(datetime.tzinfo):
    def __init__(self, offset, name):
        self.offset = datetime.timedelta(minutes=offset)
        self.name = name

    def utcoffset(self, dt):
        return self.offset

    def tzname(self, dt):
        return self.name

    def dst(self, dt):
        return datetime.timedelta(0)


@register_serializer(datetime.datetime)
def serialize_datetime(instance):
    """Return the string representation of a datetime instance"""
    return instance.isoformat()


@register_serializer(datetime.date)
def serialize_date(instance):
    """Return the string representation of a date object"""
    return instance.isoformat()


@register_serializer(datetime.time)
def serialize_time(instance):
    """Return the string representation of a time object"""
    return instance.isoformat()


@register_deserializer(datetime.datetime)
def deserialize_datetime(data):
    """Return a datetime instance based on the values of the data param"""
    return parser.parse(data)


@register_deserializer(datetime.date)
def deserialize_date(data):
    """Return a date instance based on the values of the data param"""
    return parser.parse(data).date()


@register_deserializer(datetime.time)
def deserialize_time(data):
    """Return a time instance based on the values of the data param"""
    parsed = parser.parse(data)
    return parsed.time().replace(tzinfo=parsed.tzinfo)


@register_serializer(decimal.Decimal)
def serialize_decimal(instance):
    """Convert decimal instances to strings, not to integers"""
    return str(instance)


@register_deserializer(decimal.Decimal)
def deserialize_decimal(data):
    """Convert decimal instances to strings, not to integers"""
    return decimal.Decimal(data)
