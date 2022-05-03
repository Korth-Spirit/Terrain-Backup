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
import json
from typing import Iterable, Union

from korth_spirit.data import TerrainNodeData


def append_to_file(file_name: str, data: Union[TerrainNodeData, str]) -> None:
    """
    Appends the data to the file.

    Args:
        file_name (str): The name of the file to append to.
        data (Union[AWObject, str]): The data to append.
    """
    if type(data) == TerrainNodeData:
        data = json.dumps(data.__dict__)
    
    with open(file_name, "a") as f:
        f.write(f"{data}\n")


def on_each(iterable: Iterable, callback: callable) -> None:
    """
    Iterates over all objects in the world.

    Args:
        callback (callable): The callback to call for each object.
    """
    for each in iterable:
        callback(each)
