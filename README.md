# Clone of bitcoin-arbitrage - opportunity detector and automated trading

Cloned [@maxme](http://github.com/maxme)'s [bitcoin-arbitrage](http://github.com/maxme/bitcoin-arbitrage) project and added a customer Observer that writes to a Queue, so that a RESTful API can expose the opportunities currently available across bitcoin exchanges.

# System

Works together with:
* https://github.com/lmartinho/bitcoin-arbitrage-service
* https://github.com/Sjors/ng-bitcoin-arbitrage

# Installation And Configuration

    cp arbitrage/config.py-example arbitrage/config.py

Then edit config.py file to setup your preferences: watched markets
and observers

You need Python3 to run this program.

To install on Debian, Ubuntu, or variants of them, use:

    $ sudo apt-get install python3 python3-pip python-nose

To install on Mac, use:
    
    $ brew install python3
    $ sudo pip3 install nose pymongo

# Run

To run the opportunity watcher with the Queuer observer:

    $ python3 arbitrage/arbitrage.py -o Queuer

# LICENSE

MIT

Copyright (c) 2013 Maxime Biais <firstname.lastname@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
