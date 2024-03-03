# Generated by Django 5.0.2 on 2024-03-03 12:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_name', models.CharField(choices=[('BTC', 'BTC'), ('ETH', 'ETH'), ('BNB', 'BNB'), ('BCC', 'BCC'), ('NEO', 'NEO'), ('LTC', 'LTC'), ('QTUM', 'QTUM'), ('ADA', 'ADA'), ('XRP', 'XRP'), ('EOS', 'EOS'), ('TUSD', 'TUSD'), ('IOTA', 'IOTA'), ('XLM', 'XLM'), ('ONT', 'ONT'), ('TRX', 'TRX'), ('ETC', 'ETC'), ('ICX', 'ICX'), ('VEN', 'VEN'), ('NULS', 'NULS'), ('VET', 'VET'), ('PAX', 'PAX'), ('BCHABC', 'BCHABC'), ('BCHSV', 'BCHSV'), ('USDC', 'USDC'), ('LINK', 'LINK'), ('WAVES', 'WAVES'), ('BTT', 'BTT'), ('USDS', 'USDS'), ('ONG', 'ONG'), ('HOT', 'HOT'), ('ZIL', 'ZIL'), ('ZRX', 'ZRX'), ('FET', 'FET'), ('BAT', 'BAT'), ('XMR', 'XMR'), ('ZEC', 'ZEC'), ('IOST', 'IOST'), ('CELR', 'CELR'), ('DASH', 'DASH'), ('NANO', 'NANO'), ('OMG', 'OMG'), ('THETA', 'THETA'), ('ENJ', 'ENJ'), ('MITH', 'MITH'), ('MATIC', 'MATIC'), ('ATOM', 'ATOM'), ('TFUEL', 'TFUEL'), ('ONE', 'ONE'), ('FTM', 'FTM'), ('ALGO', 'ALGO'), ('USDSB', 'USDSB'), ('GTO', 'GTO'), ('ERD', 'ERD'), ('DOGE', 'DOGE'), ('DUSK', 'DUSK'), ('ANKR', 'ANKR'), ('WIN', 'WIN'), ('COS', 'COS'), ('NPXS', 'NPXS'), ('COCOS', 'COCOS'), ('MTL', 'MTL'), ('TOMO', 'TOMO'), ('PERL', 'PERL'), ('DENT', 'DENT'), ('MFT', 'MFT'), ('KEY', 'KEY'), ('STORM', 'STORM'), ('DOCK', 'DOCK'), ('WAN', 'WAN'), ('FUN', 'FUN'), ('CVC', 'CVC'), ('CHZ', 'CHZ'), ('BAND', 'BAND'), ('BUSD', 'BUSD'), ('BEAM', 'BEAM'), ('XTZ', 'XTZ'), ('REN', 'REN'), ('RVN', 'RVN'), ('HC', 'HC'), ('HBAR', 'HBAR'), ('NKN', 'NKN'), ('STX', 'STX'), ('KAVA', 'KAVA'), ('ARPA', 'ARPA'), ('IOTX', 'IOTX'), ('RLC', 'RLC'), ('MCO', 'MCO'), ('CTXC', 'CTXC'), ('BCH', 'BCH'), ('TROY', 'TROY'), ('VITE', 'VITE'), ('FTT', 'FTT'), ('EUR', 'EUR'), ('OGN', 'OGN'), ('DREP', 'DREP'), ('BULL', 'BULL'), ('BEAR', 'BEAR'), ('ETHBULL', 'ETHBULL'), ('ETHBEAR', 'ETHBEAR'), ('TCT', 'TCT'), ('WRX', 'WRX'), ('BTS', 'BTS'), ('LSK', 'LSK'), ('BNT', 'BNT'), ('LTO', 'LTO'), ('EOSBULL', 'EOSBULL'), ('EOSBEAR', 'EOSBEAR'), ('XRPBULL', 'XRPBULL'), ('XRPBEAR', 'XRPBEAR'), ('STRAT', 'STRAT'), ('AION', 'AION'), ('MBL', 'MBL'), ('COTI', 'COTI'), ('BNBBULL', 'BNBBULL'), ('BNBBEAR', 'BNBBEAR'), ('STPT', 'STPT'), ('WTC', 'WTC'), ('DATA', 'DATA'), ('XZC', 'XZC'), ('SOL', 'SOL'), ('CTSI', 'CTSI'), ('HIVE', 'HIVE'), ('CHR', 'CHR'), ('BTCUP', 'BTCUP'), ('BTCDOWN', 'BTCDOWN'), ('GXS', 'GXS'), ('ARDR', 'ARDR'), ('LEND', 'LEND'), ('MDT', 'MDT'), ('STMX', 'STMX'), ('KNC', 'KNC'), ('REP', 'REP'), ('LRC', 'LRC'), ('PNT', 'PNT'), ('COMP', 'COMP'), ('BKRW', 'BKRW'), ('SC', 'SC'), ('ZEN', 'ZEN'), ('SNX', 'SNX'), ('ETHUP', 'ETHUP'), ('ETHDOWN', 'ETHDOWN'), ('ADAUP', 'ADAUP'), ('ADADOWN', 'ADADOWN'), ('LINKUP', 'LINKUP'), ('LINKDOWN', 'LINKDOWN'), ('VTHO', 'VTHO'), ('DGB', 'DGB'), ('GBP', 'GBP'), ('SXP', 'SXP'), ('MKR', 'MKR'), ('DAI', 'DAI'), ('DCR', 'DCR'), ('STORJ', 'STORJ'), ('BNBUP', 'BNBUP'), ('BNBDOWN', 'BNBDOWN'), ('XTZUP', 'XTZUP'), ('XTZDOWN', 'XTZDOWN'), ('MANA', 'MANA'), ('AUD', 'AUD'), ('YFI', 'YFI'), ('BAL', 'BAL'), ('BLZ', 'BLZ'), ('IRIS', 'IRIS'), ('KMD', 'KMD'), ('JST', 'JST'), ('SRM', 'SRM'), ('ANT', 'ANT'), ('CRV', 'CRV'), ('SAND', 'SAND'), ('OCEAN', 'OCEAN'), ('NMR', 'NMR'), ('DOT', 'DOT'), ('LUNA', 'LUNA'), ('RSR', 'RSR'), ('PAXG', 'PAXG'), ('WNXM', 'WNXM'), ('TRB', 'TRB'), ('BZRX', 'BZRX'), ('SUSHI', 'SUSHI'), ('YFII', 'YFII'), ('KSM', 'KSM'), ('EGLD', 'EGLD'), ('DIA', 'DIA'), ('RUNE', 'RUNE'), ('FIO', 'FIO'), ('UMA', 'UMA'), ('EOSUP', 'EOSUP'), ('EOSDOWN', 'EOSDOWN'), ('TRXUP', 'TRXUP'), ('TRXDOWN', 'TRXDOWN'), ('XRPUP', 'XRPUP'), ('XRPDOWN', 'XRPDOWN'), ('DOTUP', 'DOTUP'), ('DOTDOWN', 'DOTDOWN'), ('BEL', 'BEL'), ('WING', 'WING'), ('LTCUP', 'LTCUP'), ('LTCDOWN', 'LTCDOWN'), ('UNI', 'UNI'), ('NBS', 'NBS'), ('OXT', 'OXT'), ('SUN', 'SUN'), ('AVAX', 'AVAX'), ('HNT', 'HNT'), ('FLM', 'FLM'), ('UNIUP', 'UNIUP'), ('UNIDOWN', 'UNIDOWN'), ('ORN', 'ORN'), ('UTK', 'UTK'), ('XVS', 'XVS'), ('ALPHA', 'ALPHA'), ('AAVE', 'AAVE'), ('NEAR', 'NEAR'), ('SXPUP', 'SXPUP'), ('SXPDOWN', 'SXPDOWN'), ('FIL', 'FIL'), ('FILUP', 'FILUP'), ('FILDOWN', 'FILDOWN'), ('YFIUP', 'YFIUP'), ('YFIDOWN', 'YFIDOWN'), ('INJ', 'INJ'), ('AUDIO', 'AUDIO'), ('CTK', 'CTK'), ('BCHUP', 'BCHUP'), ('BCHDOWN', 'BCHDOWN'), ('AKRO', 'AKRO'), ('AXS', 'AXS'), ('HARD', 'HARD'), ('DNT', 'DNT'), ('STRAX', 'STRAX'), ('UNFI', 'UNFI'), ('ROSE', 'ROSE'), ('AVA', 'AVA'), ('XEM', 'XEM'), ('AAVEUP', 'AAVEUP'), ('AAVEDOWN', 'AAVEDOWN'), ('SKL', 'SKL'), ('SUSD', 'SUSD'), ('SUSHIUP', 'SUSHIUP'), ('SUSHIDOWN', 'SUSHIDOWN'), ('XLMUP', 'XLMUP'), ('XLMDOWN', 'XLMDOWN'), ('GRT', 'GRT'), ('JUV', 'JUV'), ('PSG', 'PSG'), ('1INCH', '1INCH'), ('REEF', 'REEF'), ('OG', 'OG'), ('ATM', 'ATM'), ('ASR', 'ASR'), ('CELO', 'CELO'), ('RIF', 'RIF'), ('BTCST', 'BTCST'), ('TRU', 'TRU'), ('CKB', 'CKB'), ('TWT', 'TWT'), ('FIRO', 'FIRO'), ('LIT', 'LIT'), ('SFP', 'SFP'), ('DODO', 'DODO'), ('CAKE', 'CAKE'), ('ACM', 'ACM'), ('BADGER', 'BADGER'), ('FIS', 'FIS'), ('OM', 'OM'), ('POND', 'POND'), ('DEGO', 'DEGO'), ('ALICE', 'ALICE'), ('LINA', 'LINA'), ('PERP', 'PERP'), ('RAMP', 'RAMP'), ('SUPER', 'SUPER'), ('CFX', 'CFX'), ('EPS', 'EPS'), ('AUTO', 'AUTO'), ('TKO', 'TKO'), ('PUNDIX', 'PUNDIX'), ('TLM', 'TLM'), ('1INCHUP', '1INCHUP'), ('1INCHDOWN', '1INCHDOWN'), ('BTG', 'BTG'), ('MIR', 'MIR'), ('BAR', 'BAR'), ('FORTH', 'FORTH'), ('BAKE', 'BAKE'), ('BURGER', 'BURGER'), ('SLP', 'SLP'), ('SHIB', 'SHIB'), ('ICP', 'ICP'), ('AR', 'AR'), ('POLS', 'POLS'), ('MDX', 'MDX'), ('MASK', 'MASK'), ('LPT', 'LPT'), ('NU', 'NU'), ('XVG', 'XVG'), ('ATA', 'ATA'), ('GTC', 'GTC'), ('TORN', 'TORN'), ('KEEP', 'KEEP'), ('ERN', 'ERN'), ('KLAY', 'KLAY'), ('PHA', 'PHA'), ('BOND', 'BOND'), ('MLN', 'MLN'), ('DEXE', 'DEXE'), ('C98', 'C98'), ('CLV', 'CLV'), ('QNT', 'QNT'), ('FLOW', 'FLOW'), ('TVK', 'TVK'), ('MINA', 'MINA'), ('RAY', 'RAY'), ('FARM', 'FARM'), ('ALPACA', 'ALPACA'), ('QUICK', 'QUICK'), ('MBOX', 'MBOX'), ('FOR', 'FOR'), ('REQ', 'REQ'), ('GHST', 'GHST'), ('WAXP', 'WAXP'), ('TRIBE', 'TRIBE'), ('GNO', 'GNO'), ('XEC', 'XEC'), ('ELF', 'ELF'), ('DYDX', 'DYDX'), ('POLY', 'POLY'), ('IDEX', 'IDEX'), ('VIDT', 'VIDT'), ('USDP', 'USDP'), ('GALA', 'GALA'), ('ILV', 'ILV'), ('YGG', 'YGG'), ('SYS', 'SYS'), ('DF', 'DF'), ('FIDA', 'FIDA'), ('FRONT', 'FRONT'), ('CVP', 'CVP'), ('AGLD', 'AGLD'), ('RAD', 'RAD'), ('BETA', 'BETA'), ('RARE', 'RARE'), ('LAZIO', 'LAZIO'), ('CHESS', 'CHESS'), ('ADX', 'ADX'), ('AUCTION', 'AUCTION'), ('DAR', 'DAR'), ('BNX', 'BNX'), ('RGT', 'RGT'), ('MOVR', 'MOVR'), ('CITY', 'CITY'), ('ENS', 'ENS'), ('KP3R', 'KP3R'), ('QI', 'QI'), ('PORTO', 'PORTO'), ('POWR', 'POWR'), ('VGX', 'VGX'), ('JASMY', 'JASMY'), ('AMP', 'AMP'), ('PLA', 'PLA'), ('PYR', 'PYR'), ('RNDR', 'RNDR'), ('ALCX', 'ALCX'), ('SANTOS', 'SANTOS'), ('MC', 'MC'), ('ANY', 'ANY'), ('BICO', 'BICO'), ('FLUX', 'FLUX'), ('FXS', 'FXS'), ('VOXEL', 'VOXEL'), ('HIGH', 'HIGH'), ('CVX', 'CVX'), ('PEOPLE', 'PEOPLE'), ('OOKI', 'OOKI'), ('SPELL', 'SPELL'), ('UST', 'UST'), ('JOE', 'JOE'), ('ACH', 'ACH'), ('IMX', 'IMX'), ('GLMR', 'GLMR'), ('LOKA', 'LOKA'), ('SCRT', 'SCRT'), ('API3', 'API3'), ('BTTC', 'BTTC'), ('ACA', 'ACA'), ('ANC', 'ANC'), ('XNO', 'XNO'), ('WOO', 'WOO'), ('ALPINE', 'ALPINE'), ('T', 'T'), ('ASTR', 'ASTR'), ('NBT', 'NBT'), ('GMT', 'GMT'), ('KDA', 'KDA'), ('APE', 'APE'), ('BSW', 'BSW'), ('BIFI', 'BIFI'), ('MULTI', 'MULTI'), ('STEEM', 'STEEM'), ('MOB', 'MOB'), ('NEXO', 'NEXO'), ('REI', 'REI'), ('GAL', 'GAL'), ('LDO', 'LDO'), ('EPX', 'EPX'), ('OP', 'OP'), ('LEVER', 'LEVER'), ('STG', 'STG'), ('LUNC', 'LUNC'), ('GMX', 'GMX'), ('NEBL', 'NEBL'), ('POLYX', 'POLYX'), ('APT', 'APT'), ('OSMO', 'OSMO'), ('HFT', 'HFT'), ('PHB', 'PHB'), ('HOOK', 'HOOK'), ('MAGIC', 'MAGIC'), ('HIFI', 'HIFI'), ('RPL', 'RPL'), ('PROS', 'PROS'), ('AGIX', 'AGIX'), ('GNS', 'GNS'), ('SYN', 'SYN'), ('VIB', 'VIB'), ('SSV', 'SSV'), ('LQTY', 'LQTY'), ('AMB', 'AMB'), ('BETH', 'BETH'), ('USTC', 'USTC'), ('GAS', 'GAS'), ('GLM', 'GLM'), ('PROM', 'PROM'), ('QKC', 'QKC'), ('UFT', 'UFT'), ('ID', 'ID'), ('ARB', 'ARB'), ('LOOM', 'LOOM'), ('OAX', 'OAX'), ('RDNT', 'RDNT'), ('WBTC', 'WBTC'), ('EDU', 'EDU'), ('SUI', 'SUI'), ('AERGO', 'AERGO'), ('PEPE', 'PEPE'), ('FLOKI', 'FLOKI'), ('AST', 'AST'), ('SNT', 'SNT'), ('COMBO', 'COMBO'), ('MAV', 'MAV'), ('PENDLE', 'PENDLE'), ('ARKM', 'ARKM'), ('WBETH', 'WBETH'), ('WLD', 'WLD'), ('FDUSD', 'FDUSD'), ('SEI', 'SEI'), ('CYBER', 'CYBER'), ('ARK', 'ARK'), ('CREAM', 'CREAM'), ('GFT', 'GFT'), ('IQ', 'IQ'), ('NTRN', 'NTRN'), ('TIA', 'TIA'), ('MEME', 'MEME'), ('ORDI', 'ORDI'), ('BEAMX', 'BEAMX'), ('PIVX', 'PIVX'), ('VIC', 'VIC'), ('BLUR', 'BLUR'), ('VANRY', 'VANRY'), ('AEUR', 'AEUR'), ('JTO', 'JTO'), ('1000SATS', '1000SATS'), ('BONK', 'BONK'), ('ACE', 'ACE'), ('NFP', 'NFP'), ('AI', 'AI'), ('XAI', 'XAI'), ('MANTA', 'MANTA'), ('ALT', 'ALT'), ('JUP', 'JUP'), ('PYTH', 'PYTH'), ('RONIN', 'RONIN'), ('DYM', 'DYM'), ('PIXEL', 'PIXEL'), ('STRK', 'STRK'), ('PORTAL', 'PORTAL'), ('PDA', 'PDA'), ('AXL', 'AXL')], max_length=100)),
                ('token_amount', models.FloatField()),
                ('accepted', models.BooleanField(default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
