Generic:

Dougcoin
Python >=2.6
Twisted >=10.0.0
python-argparse (for Python =2.6)

Linux:

sudo apt-get install python-zope.interface python-twisted python-twisted-web
sudo apt-get install python-argparse # if on Python 2.6

Windows:

Install Python 2.7: http://www.python.org/getit/
Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
Unzip the files into C:\Python27\Lib\site-packages

Running P2Pool:

To use P2Pool, you must be running your own local dougcoind. For standard configurations, using P2Pool should be as simple as:

python setup.py

python run_p2pool.py --net dougcoin --fee 1 --give-author 0 --bitcoind-rpc-port 6968 rpcuser rpcpass

If you are behind a NAT, you should enable TCP port forwarding on your router.

Run for additional options.

python run_p2pool.py --help
