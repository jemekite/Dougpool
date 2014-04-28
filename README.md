Requirements:
-------------------------
Generic:
* [Dougcoin]
* Python 
* Twisted
* python-argparse (for Python =2.6)
* quarkcoin-hash-python

Linux:
```sh
sudo apt-get install python-zope.interface python-twisted python-twisted-web
```


Install module:
-------------------------

```sh
sudo apt-get install libboost1.48-all-dev python-devda -y
git clone https://github.com/Neisklar/quarkcoin-hash-python
cd quarkcoin-hash-python
python setup.py install
```

Running Dougcoin P2Pool:
-------------------------
To use P2Pool, you must be running your own local Dougcoind. For standard
configurations, using P2Pool should be as simple as:

     python run_p2pool.py --net Dougcoin
    
Then run your miner program, connecting to 127.0.0.1 on port 7977 with any
username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 7977 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help


Official wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool

[Dougcoin]:http://dougcoin.org

