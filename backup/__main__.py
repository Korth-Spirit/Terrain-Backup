# Copyright (c) 2021-2022 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from korth_spirit import Instance
from korth_spirit.coords import Coordinates
from korth_spirit.query import QueryEnum

from utilities import append_to_file, on_each

with Instance(name=input("Bot Name: ")) as bot:
    try:
        bot.login(
            citizen_number=(int(input("Citizen Number: "))),
            password=input("Password: ")
        ).enter_world(
            input("World: ")
        ).move_to(
            Coordinates(0, 0, 0)
        )

        on_each(
            bot.query(QueryEnum.TERRAIN),
            lambda terrain: append_to_file(
                "terrain.json",
                terrain
            )
        )
    except Exception as e:
        print("An error occurred:", e)
