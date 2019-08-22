# out-of-time-scaner
Analyze the tron blockchain to get the out of time of the super representative


### Requirements

- python2.7+ installed

- virtualenv installed
    ```
     $pip install virtualenv
    ```
- init the virtual environment
    ```
    $virtualenv venv
    
    $source venv/bin/activate
    
    $pip install -r requirements.txt 
    ```
    
### Usage

#### step 1: Parsing block
```
$ python scaner.py parse --start=11971381 --end=11975000
[ Scaner ]: parsing Blocks from trongrid, from 11971381 to 11975000...
100%|██████████| 3620/3620 [00:00<00:00, 54016.27blocks/s]
```

#### step 2: Show all status
```
$ python scaner.py status

Start Block: 11960000
  End Block: 11975000

SR Address                                    SR NAME                                  OutOfTime Txs                  Total Blocks
4167e39013be3cdd3814bed152d7439fb5b6791409    http://cryptochain.network               107                            558       
41f70386347e689e6308e4172ed7319c49c0f66e0b    http://tronone.com                       1                              558       
41e40302d6b5e889bfbd395ed884638d7f03ee3f87    https://tronlink.org                     2                              558       
41c189fa6fc9ed7a3580c3fe291915d5c6a6259be7    https://www.cryptoguyinza.co.za/         2                              558       
4118e2e1c6cdf4b74b7c1eb84682e503213a174955    https://tronscan.org                     0                              558       
412d7bdb9846499a2e5e6c5a7e6fb05731c83107c7    https://www.tronwallet.me/               8                              558       
41b3eec71481e8864f0fc1f601b836b74c40548287    https://www.bittorrent.com/              1                              558       
41bac7378c4265ad2739772337682183b8864f517a    http://trx.market                        4                              557       
41496e85711fa3b7ba5a093af635269a67230ac2c1    https://www.beatzcoin.io/                9                              554       
414a193c92cd631c1911b99ca964da8fd342f4cddd    http://www.skypeople.co.kr               0                              533       
41f29f57614a6b201729473c837e1d2879e9f90b8e    https://www.utorrent.com/                5                              559       
41beab998551416b02f6721129bb01b51fceceba08    https://tronspark.com                    10                             559       
4138e3e3a163163db1f6cfceca1d1c64594dd1f0ca    https://twitter.com/justinsuntron        1                              559       
41d70365508e5a6fe846ad433af9302779fd5fdb1b    http://krypto-knight.us/                 0                              556       
4192c5d96c3b847268f4cb3e33b87ecfc67b5ce3de    https://infstones.io/                    0                              557       
4193a8bc2e7d6bb1bd75fb2d74107ffbda81af439d    http://www.cryptodiva.io/                4                              556       
41a9d4b388c009b7ee36819114b8558d078103ad0b    https://hitbtc.com                       10                             559       
41037e18c9ca44b2ba35f0bb7d0c075f252a191294    https://trxultra.org                     23                             553       
417bdd2efb4401c50b6ad255e6428ba688e0b83f81    https://minergate.com                    11                             555       
415863f6091b8e71766da808b1dd3159790f61de7d    https://www.huobipool.com                7                              550       
411103d62d8299e90fa011b4ce7fc6ba151e5f1a23    https://www.tronvietnam.com/             24                             550       
41a75a876ef0e8715aa2cd34597154382502b8d646                                             25                             553       
41d599cb8c1b609722e81741667ba3c8fb441fba41    www.tronspirit.com                       5                              558       
414d1ef8673f916debb7e2515a8f3ecaf2611034aa    https://www.sesameseed.org               1                              555       
41d25855804e4e65de904faf3ac74b0bdfc53fac76    https://www.bitguild.com                 0                              558       
41c81107148e5fa4b4a2edf3d5354db6c6be5b5549    https://www.trongrid.io                  6                              557       
4184399fc6a98edc11a6efb146e86a3e153d0a0933    https://www.tron-europe.org              3                              557 
```
#### step 3: Get a piece of information
```
$ python scaner.py query --min_block=11960000 --max_block=11965000 
------------------------------------------
     Time Range: 2019-08-18 17:15:30 ~ 2019-08-18 21:26:51
TimeStamp Range: 1566119730000 ~ 1566134811000
    Block Range: 11960000 ~ 11965000
------------------------------------------
SR Address                                    SR NAME                                  OutOfTime Txs      
4167e39013be3cdd3814bed152d7439fb5b6791409    http://cryptochain.network               32                          
41f70386347e689e6308e4172ed7319c49c0f66e0b    http://tronone.com                       0                           
41e40302d6b5e889bfbd395ed884638d7f03ee3f87    https://tronlink.org                     0                           
41c189fa6fc9ed7a3580c3fe291915d5c6a6259be7    https://www.cryptoguyinza.co.za/         0                           
4118e2e1c6cdf4b74b7c1eb84682e503213a174955    https://tronscan.org                     0                           
412d7bdb9846499a2e5e6c5a7e6fb05731c83107c7    https://www.tronwallet.me/               4                           
41b3eec71481e8864f0fc1f601b836b74c40548287    https://www.bittorrent.com/              0                           
41bac7378c4265ad2739772337682183b8864f517a    http://trx.market                        1                           
41496e85711fa3b7ba5a093af635269a67230ac2c1    https://www.beatzcoin.io/                3                           
414a193c92cd631c1911b99ca964da8fd342f4cddd    http://www.skypeople.co.kr               0                           
41f29f57614a6b201729473c837e1d2879e9f90b8e    https://www.utorrent.com/                2                           
41beab998551416b02f6721129bb01b51fceceba08    https://tronspark.com                    4                           
4138e3e3a163163db1f6cfceca1d1c64594dd1f0ca    https://twitter.com/justinsuntron        0                           
41d70365508e5a6fe846ad433af9302779fd5fdb1b    http://krypto-knight.us/                 0                           
4192c5d96c3b847268f4cb3e33b87ecfc67b5ce3de    https://infstones.io/                    0                           
4193a8bc2e7d6bb1bd75fb2d74107ffbda81af439d    http://www.cryptodiva.io/                1                           
41a9d4b388c009b7ee36819114b8558d078103ad0b    https://hitbtc.com                       3                           
41037e18c9ca44b2ba35f0bb7d0c075f252a191294    https://trxultra.org                     7                           
417bdd2efb4401c50b6ad255e6428ba688e0b83f81    https://minergate.com                    4                           
415863f6091b8e71766da808b1dd3159790f61de7d    https://www.huobipool.com                2                           
411103d62d8299e90fa011b4ce7fc6ba151e5f1a23    https://www.tronvietnam.com/             8                           
41a75a876ef0e8715aa2cd34597154382502b8d646                                             7                           
41d599cb8c1b609722e81741667ba3c8fb441fba41    www.tronspirit.com                       3                           
414d1ef8673f916debb7e2515a8f3ecaf2611034aa    https://www.sesameseed.org               0                           
41d25855804e4e65de904faf3ac74b0bdfc53fac76    https://www.bitguild.com                 0                           
41c81107148e5fa4b4a2edf3d5354db6c6be5b5549    https://www.trongrid.io                  2                           
4184399fc6a98edc11a6efb146e86a3e153d0a0933    https://www.tron-europe.org              0                

```
#### step 3: Display out of time transaction information for a certain sr within a certain interval
```
$ python scaner.py txs 4167e39013be3cdd3814bed152d7439fb5b6791409 --min_block=11960000 --max_block=11965000 
------------------------------------------
Time  Range: 2019-08-18 17:15:30 ~ 2019-08-18 21:26:51
Block Range: 11960000 ~ 11965000
------------------------------------------
TxId                                                                   Ret              Time                      FuncID              
453da6882348d46644c283f2619e1a2cf155481886e5700cf1f4b590189f437a       OUT_OF_TIME      2019-08-18 17:37:54       49774683            
db96606f76d90a09978dca64b8bdca786919a1ecf42a2a62dcf2f4c9ab86c0e9       OUT_OF_TIME      2019-08-18 17:40:39       49774683            
5f0d481763f95fad0e7917c3a22e9404c584c9a7a5be3cf2f1119db2d535d999       OUT_OF_TIME      2019-08-18 17:52:49       49774683            
65158803ce1b3da79ae666b02c39bf65714e355f6da82a29d748754d9d7f3a8e       OUT_OF_TIME      2019-08-18 18:02:14       49774683            
73d2343edbdcaaa0f74222485438dbabce80fa35c4e68e3dc45f73eef8b675f4       OUT_OF_TIME      2019-08-18 18:03:35       49774683            
4e25c7d59a22abd9366cb81f7c77a7ae41e60123861279b565a109be4f296306       OUT_OF_TIME      2019-08-18 18:13:04       49774683            
d353872118cd3c372b91500de0d13600b651546b3b652cf5cf190415fbcc1cb3       OUT_OF_TIME      2019-08-18 18:15:46       49774683            
a914aa11cfcd49e5a53165394f574635da61ba28cba505000f02145c631344ba       OUT_OF_TIME      2019-08-18 18:22:30       49774683            
39d22a8816c6364fbd9927d1bdddb0fc3554a1b57b19ca724da17fe22981c310       OUT_OF_TIME      2019-08-18 18:27:55       49774683            
540b8f42f645cb3f78701cf9d46b1bf634cac3112750c8ad4b17747b93065995       OUT_OF_TIME      2019-08-18 18:53:34       49774683            
780b13a417998660d53673dab9c5b1d84a0749e07ee16537c21cb6faf2cd8c41       OUT_OF_TIME      2019-08-18 18:54:56       49774683            
c6bef588d31ec8b9fe6a231f8b394a427306a1b87cfd25b868e29a7ef17c6b50       OUT_OF_TIME      2019-08-18 19:04:21       49774683            
bb280c7616b1c682917e33c15468eec14f8c1177f39670b91d4b9c2df49f417b       OUT_OF_TIME      2019-08-18 19:07:04       fd8b0889            
4f8e79b646e8489867920044ba3d4e16f611dd0fe26f63f297c38b10b853264f       OUT_OF_TIME      2019-08-18 19:09:45       49774683            
61610d6d9bb93eb2fbeb597b37f78761da3ab261f4099bc670bfce0df0114545       OUT_OF_TIME      2019-08-18 19:11:05       49774683            
819f8985b4d4491ba44ff1ffb3d723a9314919eaf272098dd9293f89b93cb8a0       OUT_OF_TIME      2019-08-18 19:12:28       49774683            
3f3e4a56985205a33fb8d6669ecd559f31db8c74cc3954548160a744c60b0d00       OUT_OF_TIME      2019-08-18 19:13:47       49774683            
89c41a64357d540361fecc94dbc3896b8c228cbce12a0d97b5d3e13406b02c79       OUT_OF_TIME      2019-08-18 19:17:50       49774683            
1d46ee8b5bee5db09ef928f6a4bef649c5e821d18e6d0fa0ba55a0563f3400d0       OUT_OF_TIME      2019-08-18 19:25:56       49774683            
b0c542c8b29721dcd45bac4ef2f8728d04832d6b9f2ffca1bfdba86a63995cde       OUT_OF_TIME      2019-08-18 19:27:19       49774683            
8343bd98a9bc21c61df18b49a5fe0c85440ae31d1767c6256a81186a34cba5c6       OUT_OF_TIME      2019-08-18 19:50:14       49774683            
f9a6dd2b8f7eec6c473ece238f2d12a630cef96a99b15d2a91d184ddc3341965       OUT_OF_TIME      2019-08-18 19:51:37       49774683            
3c84c2532b9a97682b49e5b89ac2133f9786378196895579b207df100d712561       OUT_OF_TIME      2019-08-18 19:55:41       49774683            
eaab84fd38a8b8176e55fa7e943ab1a67d26eb1ed544df55990c213dedc4eeaa       OUT_OF_TIME      2019-08-18 20:09:10       49774683            
8d895d4c709bb0f25a6bca5b5f4875bc7989a5e014d62904e1a095f17c378b90       OUT_OF_TIME      2019-08-18 20:17:16       49774683            
cc0d2b69410322a6d247c06d7ed6d4091e2c64130c00c285c807aa9e1463aef8       OUT_OF_TIME      2019-08-18 20:24:02       49774683            
f92ebc4863e96f4cff3a16454473293f073649c1c7dced511a638c896eb80e39       OUT_OF_TIME      2019-08-18 20:57:45       49774683            
ba7c3115ed0e98e8da812a3528061a544d2bc6c3fcbe8955eb0ba1f6e2541348       OUT_OF_TIME      2019-08-18 21:07:12       49774683            
480e4e5bb29fff313d48bed137a9e130dd790c997672bf02cc2233d4ad535c50       OUT_OF_TIME      2019-08-18 21:13:57       49774683            
8f16347b6d385e017bfdd2676408f29a3c2006ddbb330bb9b9b7abbeca4b95dc       OUT_OF_TIME      2019-08-18 21:16:40       49774683            
cba666abc109e8135237b8b2f9dca8ba7e17fc4993185023e22e4793d7f3892e       OUT_OF_TIME      2019-08-18 21:21:59       49774683            
562154fc33bdb641cb4de8334ae60c786fa54a510e051ce94c96233e7af74751       OUT_OF_TIME      2019-08-18 21:26:08       49774683 

```
