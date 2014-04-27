from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(

    ###Neisklar: BOOTSTRAP_ADDRS need to be set for a real p2pool network
    ###          PERSIST=True for a p2pool network.
    ###          the settings now are for a solo node, acting as pool
    ###          dunno if these share values needs some tweaking
    ###          The two SPREAD values should definatly be a higher value for such fast coin
    ###          with a relativly low difficulty, so maybe 60, which when we assume the pool 
    ###          gets every third block it's around 90 minutes, means a better distribution of
    ###          earnings, but newer miners will take some time to build up the income.
    Dougcoin=math.Object(
        PARENT=networks.nets['Dougcoin'],
        SHARE_PERIOD=15, # seconds
        NEW_SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=50, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=30, # blocks
        NEW_SPREAD=30, # blocks
        IDENTIFIER='fc70135c7a81bc6f'.decode('hex'),
        PREFIX='9472ef181efcd37b'.decode('hex'),
        P2P_PORT=10087,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=7977,
        BOOTSTRAP_ADDRS='23.226.130.190'.split(' '),
        #ANNOUNCE_CHANNEL='#p2pool',
        VERSION_CHECK=lambda v: True,
    )
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
