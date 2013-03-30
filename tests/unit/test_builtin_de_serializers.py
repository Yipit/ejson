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

import datetime
import decimal

import ejson
import ejson.serializers


def test_tzinfo_helper():
    # Given that I wanna handle basic time zone information in my datetime
    # serializers
    obj = datetime.datetime(
        2013, 03, 30, 12, 12, 12, 123456,
        ejson.serializers.TZInfoHelper(60*3, "America/Sao_Paulo"))

    # Then I see that my time zone informatino was properly set on my datetime
    # object.
    obj.tzname().should.equal('America/Sao_Paulo')
    obj.isoformat().should.equal('2013-03-30T12:12:12.123456+03:00')
    obj.dst().should.equal(datetime.timedelta(0))


def test_datetime():
    # Given that I have an instance of the datetime object that must be
    # serialized
    obj = datetime.datetime(2013, 03, 30, 12, 12, 12)

    # When I serialize it
    serialized = ejson.dumps(obj)

    # Then I see the proper representation of the instance that will allow us
    # to deserialize it later
    serialized.should.equal(
        '{"__class__": "datetime.datetime",'
        ' "__value__": "2013-03-30T12:12:12"}')

    # When I try to deserialize, Then I see that it also works!
    ejson.loads(serialized).should.equal(obj)


def test_datetime_with_microseconds():
    # Given that I have an instance of the datetime object with timezone
    # information, must be serialized
    obj = datetime.datetime(
        2013, 03, 30, 12, 12, 12, 123456,
        ejson.serializers.TZInfoHelper(60*3, "America/Sao_Paulo"))

    # When I serialize it
    serialized = ejson.dumps(obj)

    # Then I see the proper representation of the instance that will allow us
    # to deserialize it later
    serialized.should.equal(
        '{"__class__": "datetime.datetime",'
        ' "__value__": "2013-03-30T12:12:12.123456+03:00"}')

    # When I try to deserialize, Then I see it works again
    ejson.loads(serialized).should.equal(obj)


def test_date():
    # Given that I have an instance of the date object that must be serialized
    obj = datetime.date(2013, 03, 30)

    # When I serialize it
    serialized = ejson.dumps(obj)

    # Then I see the proper representation of the instance that will allow us
    # to deserialize it later
    serialized.should.equal(
        '{"__class__": "datetime.date", "__value__": "2013-03-30"}')

    # When I try to load this info again, Then I see that it also works
    ejson.loads(serialized).should.equal(obj)


def test_time():
    # Given that I have a time object to serialize
    obj = datetime.time(1, 12, 50, 123)

    # When I serialize it
    serialized = ejson.dumps(obj)

    # Then I see that it was correctly serialized
    serialized.should.equal(
        '{"__class__": "datetime.time", "__value__": "01:12:50.000123"}')

    # When I try to deserialize, I see that it also works
    ejson.loads(serialized).should.equal(obj)


def test_time_with_timezone():
    # Given that I have a time object to serialize
    obj = datetime.time(
        1, 12, 50, 123,
        ejson.serializers.TZInfoHelper(-120, "FNT"))

    # When I serialize it
    serialized = ejson.dumps(obj)

    # Then I see that it was correctly serialized
    serialized.should.equal(
        '{"__class__": "datetime.time", "__value__": "01:12:50.000123-02:00"}')

    # When I try to deserialize, I see that it also works
    ejson.loads(serialized).should.equal(obj)


def test_decimal():
    # Given that I have a decimal object
    obj = decimal.Decimal("0.14285714285714285")

    # When I try to serialize it
    serialized = ejson.dumps(obj)

    # Then I see the proper string description of the object
    serialized.should.equal(
        '{"__class__": "decimal.Decimal", "__value__": "0.14285714285714285"}')

    # When I try to deserialize, I see that it also works
    ejson.loads(serialized).should.equal(obj)
