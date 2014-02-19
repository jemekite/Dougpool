import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack

nets = dict(
    ###Neisklar: IMPORTANT!!!!!!!!!!!!!1111!!11einself
    ###          The SUBSIDY_FUNC is NOT correctly in terms of keeping the minimum 1 QRK
    ###          Reward for the end of the regular mining period. Means: it will work now
    ###          and some time in the future. I think a simple max(..., 1) around it will fix it
    ###          Maybe the dust threshold should also be rised somewhat, since we only have 5 decimals...
    Dougcoin=math.Object(
        P2P_PREFIX='fea503dd'.decode('hex'),
        P2P_PORT=10087,
        ADDRESS_VERSION=7,
        RPC_PORT=6968,
	RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'dougcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 10240*100000000 >> (height + 1)//86400,
        BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('quark_hash').getPoWHash(data)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('quark_hash').getPoWHash(data)),
        BLOCK_PERIOD=30, # s
        SYMBOL='DOUG',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Dougcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Dougcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.Dougcoin'), 'Dougcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://dougexplorer.lowend.fm/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://dougexplorer.lowend.fm/address/',
        ### Neisklar: normally 2**24 should be 2**20 BUT the quark enabled minerd is coded so that it only detects hashes below 0x000000xxxxxxx
        ###           and 2*20 would be 0x00000FFFF, maybe changing that in the miner  would be a good idea for slower ones... 
		### Update:   the minerd is (at least in GitHub) updated so that it would also detect targets below 2**24 (0x000000xxxx..), (Quarkcoins starts with 2**20 (0x00000xxxx...))
		###           maybe for new standalone p2pools it's a good choice at the beginning, but ONLY when new hashing power is gradually added...
        #SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**24 - 1), 
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1), 
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    )
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
