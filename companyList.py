from companyItem import CompanyItem
from scrapeLever import ScrapeLever
from scrapeGreenhouse import ScrapeGreenhouse
from scrapeSmartrecruiters import ScrapeSmartrecruiters
from scrapeRecruitee import ScrapeRecruitee
from scrapeBinance import ScrapeBinance
from scrape_bamboohr import ScrapeBamboohr
from scrape_consensys import ScrapeConsensys
from scrape_ripple import ScrapeRipple
from scrape_workable import ScrapeWorkable


def getCompanyList() -> list():
    company_list = []
    company_list.append(CompanyItem("kraken",  "https://jobs.lever.co/kraken", ScrapeLever, "https://kraken.com","Exchange"))
    company_list.append(CompanyItem("chainlink",  "https://jobs.lever.co/chainlink", ScrapeLever, "https://chain.link","Blockchain"))
    company_list.append(CompanyItem("chainstack", "https://chainstack.bamboohr.com/jobs", ScrapeBamboohr, "https://chainstack.com", "Infra"))
    company_list.append(CompanyItem("tessera",  "https://jobs.lever.co/ftc", ScrapeLever, "https://tessera.co", "NFT"))
    company_list.append(CompanyItem("paxos",  "https://paxos.com/careers/role", ScrapeGreenhouse, "https://paxos.com", "Stable Coin"))
    company_list.append(CompanyItem("bitcoin", "https://www.bitcoin.com/jobs/#joblist", ScrapeGreenhouse, "https://www.bitcoin.com", 'Exchange'))
    company_list.append(
        CompanyItem("cexio", "https://cexio.bamboohr.com/jobs", ScrapeBamboohr, "https://cex.io", "Exchange"))
    company_list.append(CompanyItem("circle",  "https://boards.greenhouse.io/circle", ScrapeGreenhouse, "https://circle.com", "Stable Coin"))
    company_list.append(CompanyItem("status",  "https://jobs.status.im", ScrapeGreenhouse, "https://status.im","Messanger"))
    company_list.append(CompanyItem("OKX",  "https://boards.greenhouse.io/OKX", ScrapeGreenhouse, "https://okx.com","Exchange"))
    company_list.append(CompanyItem("bittrex", "https://boards.greenhouse.io/bittrex", ScrapeGreenhouse, "https://global.bittrex.com", 'Exchange'))
    company_list.append(CompanyItem("kaiko",  "https://jobs.eu.lever.co/kaiko", ScrapeLever, "https://www.kaiko.com", "Data"))
    company_list.append(CompanyItem("bitmex",  "https://boards.greenhouse.io/bitmex", ScrapeGreenhouse, "https://bitmex.com","Exchange"))
    company_list.append(CompanyItem("bitgo",  "https://boards.greenhouse.io/bitgo", ScrapeGreenhouse, "https://bitgo.com","Exchange"))
    company_list.append(CompanyItem("bitpanda",  "https://boards.eu.greenhouse.io/bitpanda", ScrapeGreenhouse, "https://bitpanda.com","Exchange"))
    company_list.append(CompanyItem("uniswaplabs",  "https://boards.greenhouse.io/uniswaplabs", ScrapeGreenhouse, "https://uniswap.org","Exchange Protocol"))
    company_list.append(CompanyItem("moonpay",  "https://boards.greenhouse.io/moonpay", ScrapeGreenhouse, "https://www.moonpay.com","Payments"))
    company_list.append(CompanyItem("moonwalk",  "https://boards.greenhouse.io/moonwalk", ScrapeGreenhouse, "https://www.moonwalk.com","Platform"))
    company_list.append(CompanyItem("blockdaemon",  "https://boards.greenhouse.io/blockdaemon", ScrapeGreenhouse, "https://www.blockdaemon.com","Staking & Infra"))
    company_list.append(CompanyItem("figment",  "https://boards.greenhouse.io/figment", ScrapeGreenhouse, "https://www.figment.io","Staking & Infra"))
    company_list.append(CompanyItem("quiknodeinc",  "https://boards.greenhouse.io/quiknodeinc", ScrapeGreenhouse, "https://www.quicknode.com","Staking & Infra"))
    company_list.append(CompanyItem("genesisglobaltradinginc",  "https://boards.greenhouse.io/genesisglobaltradinginc", ScrapeGreenhouse, "https://genesistrading.com","OTC Trading"))
    company_list.append(CompanyItem("amun",  "https://boards.greenhouse.io/amun", ScrapeGreenhouse, "https://www.21.co","OTC"))
    company_list.append(CompanyItem("exodus54",  "https://boards.greenhouse.io/exodus54", ScrapeGreenhouse, "https://www.exodus.com","Wallet"))
    company_list.append(CompanyItem("alchemy",  "https://boards.greenhouse.io/alchemy", ScrapeGreenhouse, "https://www.alchemy.com","Dev & Infra"))
    company_list.append(CompanyItem("chainalysis",  "https://boards.greenhouse.io/chainalysis", ScrapeGreenhouse, "https://www.chainalysis.com","Crypto Research"))
    company_list.append(CompanyItem("magiceden",  "https://boards.greenhouse.io/magiceden", ScrapeGreenhouse, "https://www.magiceden.io","NFT"))
    company_list.append(
        CompanyItem("aztec", "https://boards.eu.greenhouse.io/aztec", ScrapeGreenhouse, "https://aztec.network",
                    "Protocol"))
    company_list.append(CompanyItem("nethermind",  "https://boards.eu.greenhouse.io/nethermind", ScrapeGreenhouse, "https://nethermind.io","Crypto software"))
    company_list.append(CompanyItem("dfinity",  "https://boards.greenhouse.io/dfinity", ScrapeGreenhouse, "https://dfinity.org","Blockchain"))
    company_list.append(CompanyItem("parity",  "https://boards.greenhouse.io/parity", ScrapeGreenhouse, "https://www.parity.io","Infra"))
    company_list.append(CompanyItem("optimism",  "https://boards.greenhouse.io/optimism", ScrapeGreenhouse, "https://www.optimism.io","L2 protocol"))
    company_list.append(CompanyItem("flashbots",  "https://boards.greenhouse.io/flashbots", ScrapeGreenhouse, "https://www.flashbots.net","ETH MEV"))
    company_list.append(CompanyItem("oplabs",  "https://boards.greenhouse.io/oplabs", ScrapeGreenhouse, "https://www.oplabs.co","L2 protocol"))
    company_list.append(CompanyItem("bitfinex",  "https://bitfinex.recruitee.com", ScrapeRecruitee, "https://www.bitfinex.com","Exchange"))
    company_list.append(CompanyItem("binance",  "https://www.binance.com/en/careers/job-openings", ScrapeBinance, "https://www.binance.com","Exchange"))
    company_list.append(CompanyItem("coinmarketcap",  "https://careers.smartrecruiters.com/B6/coinmarketcap", ScrapeSmartrecruiters, "https://coinmarketcap.com","Information"))
    company_list.append(CompanyItem("trustwallet",  "https://careers.smartrecruiters.com/B6/trustwallet", ScrapeSmartrecruiters, "https://trustwallet.com","Wallet"))
    company_list.append(CompanyItem("Swissquote",  "https://careers.smartrecruiters.com/Swissquote", ScrapeSmartrecruiters, "https://en.swissquote.com","Exchange"))
    company_list.append(CompanyItem("Coinshift",  "https://jobs.lever.co/Coinshift", ScrapeLever, "https://coinshift.xyz","Custody software"))
    company_list.append(CompanyItem("swissborg",  "https://jobs.lever.co/swissborg", ScrapeLever, "https://swissborg.com","Exchange"))
    company_list.append(CompanyItem("OpenSea",  "https://jobs.lever.co/OpenSea", ScrapeLever, "https://opensea.io","NFT"))
    company_list.append(CompanyItem("storyprotocol",  "https://jobs.lever.co/storyprotocol", ScrapeLever, "https://www.storyprotocol.xyz","Protocol"))
    company_list.append(CompanyItem("ethereumfoundation",  "https://jobs.lever.co/ethereumfoundation", ScrapeLever, "https://ethereum.org","Blockchain"))
    company_list.append(CompanyItem("aave",  "https://jobs.eu.lever.co/aave", ScrapeLever, "https://aave.com","Protocol"))
    company_list.append(CompanyItem("crypto",  "https://jobs.lever.co/crypto", ScrapeLever, "https://crypto.com","Exchange"))
    company_list.append(
        CompanyItem("avalabs", "https://boards.greenhouse.io/avalabs", ScrapeGreenhouse, "https://www.avalabs.org",
                    "Blockchain"))
    company_list.append(CompanyItem("Polygon",  "https://jobs.lever.co/Polygon", ScrapeLever, "https://polygon.technology","Blockchain"))
    company_list.append(CompanyItem("tokenmetrics",  "https://jobs.lever.co/tokenmetrics", ScrapeLever, "https://www.tokenmetrics.com","Information"))
    company_list.append(CompanyItem("offchainlabs",  "https://jobs.lever.co/offchainlabs", ScrapeLever, "https://offchainlabs.com","Protocol"))
    company_list.append(CompanyItem("subspacelabs",  "https://jobs.lever.co/subspacelabs", ScrapeLever, "https://subspace.network","Blockchain Infra"))
    company_list.append(CompanyItem("tron",  "https://boards.greenhouse.io/rainberry", ScrapeGreenhouse, "https://tron.network","Blockchain"))
    company_list.append(CompanyItem("messari",  "https://boards.greenhouse.io/messari", ScrapeGreenhouse, "https://messari.io","Information"))
    company_list.append(CompanyItem("copperco",  "https://boards.eu.greenhouse.io/copperco", ScrapeGreenhouse, "https://copper.co","Custody"))
    company_list.append(CompanyItem("digitalasset",  "https://boards.greenhouse.io/digitalasset", ScrapeGreenhouse, "https://www.digitalasset.com","Custody"))
    company_list.append(CompanyItem("ramp.network",  "https://jobs.lever.co/careers.ramp.network", ScrapeLever, "https://ramp.network", "Payments"))
    company_list.append(CompanyItem("ledger",  "https://jobs.lever.co/ledger", ScrapeLever, "https://www.ledger.com", "Wallet"))
    company_list.append(CompanyItem("layerzerolabs",  "https://boards.greenhouse.io/layerzerolabs", ScrapeGreenhouse, "https://layerzero.network","Infra"))
    company_list.append(CompanyItem("request",  "https://jobs.lever.co/request", ScrapeLever, "https://request.network", "Payments"))
    company_list.append(CompanyItem("immutable",  "https://jobs.lever.co/immutable", ScrapeLever, "https://www.immutable.com", "NFT"))
    company_list.append(CompanyItem("web3auth",  "https://jobs.lever.co/TorusLabs", ScrapeLever, "https://web3auth.io", "Auth"))
    company_list.append(CompanyItem("jumpcrypto",  "https://boards.greenhouse.io/jumpcrypto", ScrapeGreenhouse, "https://jumpcrypto.com","Infra"))
    company_list.append(CompanyItem("oasisnetwork",  "https://boards.greenhouse.io/oasisnetwork", ScrapeGreenhouse, "https://oasisprotocol.org","Protocol"))
    company_list.append(CompanyItem("consensys",  "https://consensys.net/open-roles", ScrapeConsensys, "https://consensys.net","Infra"))
    company_list.append(CompanyItem("poap", "https://boards.greenhouse.io/poaptheproofofattendanceprotocol", ScrapeGreenhouse, "https://poap.xyz", "Protocol"))
    company_list.append(CompanyItem("chainsafesystems", "https://boards.greenhouse.io/chainsafesystems", ScrapeGreenhouse, "https://chainsafe.io", "Infra"))
    company_list.append(CompanyItem("ripple", "https://ripple.com/careers/all-jobs", ScrapeRipple, "https://ripple.com", "Blockchain"))
    company_list.append(CompanyItem("kadena", "https://boards.greenhouse.io/kadenallc", ScrapeGreenhouse, "https://kadena.io", "Blockchain"))
    company_list.append(CompanyItem("EigenLabs", "https://boards.greenhouse.io/layrlabs", ScrapeGreenhouse, "https://www.v1.eigenlayer.xyz", "Infra"))
    company_list.append(CompanyItem("cere-network",  "https://jobs.lever.co/cere-network", ScrapeLever, "https://cere.network", "Infra"))
    company_list.append(
        CompanyItem('sygnum', 'https://sygnum.bamboohr.com/careers', ScrapeBamboohr, 'https://www.sygnum.com',
                    'Crypto bank'))
    company_list.append(CompanyItem('iofinnet', 'https://iofinnethr.bamboohr.com/jobs/?source=bamboohr', ScrapeBamboohr,
                                    'https://www.iofinnet.com', 'Custody'))
    company_list.append(
        CompanyItem("galaxydigitalservices", "https://boards.greenhouse.io/galaxydigitalservices", ScrapeGreenhouse,
                    "https://www.galaxy.com", 'Trading'))
    company_list.append(CompanyItem("hiro", "https://jobs.lever.co/hiro", ScrapeLever, "https://www.hiro.so", "Infra"))
    company_list.append(
        CompanyItem('web3', 'https://web3.bamboohr.com/jobs', ScrapeBamboohr, 'https://web3.foundation', 'web3'))
    company_list.append(
        CompanyItem('dappradar', 'https://dappradar.bamboohr.com/careers', ScrapeBamboohr, 'https://dappradar.com',
                    'Exchange & NFT'))
    company_list.append(
        CompanyItem('bitstamp', 'https://apply.workable.com/bitstamp/#jobs', ScrapeWorkable, 'https://www.bitstamp.net',
                    'Exchange'))
    company_list.append(CompanyItem('smart-token-labs', 'https://apply.workable.com/smart-token-labs', ScrapeWorkable,
                                    'https://smarttokenlabs.com', 'Web3 bridge'))
    company_list.append(
        CompanyItem('avantgarde', 'https://apply.workable.com/avantgarde', ScrapeWorkable, 'https://avantgarde.finance',
                    'Asset Management'))
    company_list.append(
        CompanyItem('stably', 'https://apply.workable.com/stably', ScrapeWorkable, 'https://stably.io', 'Stable Coin'))
    company_list.append(CompanyItem('cryptofinance', 'https://apply.workable.com/cryptofinance', ScrapeWorkable,
                                    'https://www.crypto-finance.com', 'Exchange'))
    company_list.append(
        CompanyItem('bitget', 'https://apply.workable.com/bitget', ScrapeWorkable, 'https://www.bitget.com/en',
                    'Exchange'))

    return company_list


def get_logo(company_name):
    company_logos = {
        'kraken': '<img src="https://lever-client-logos.s3.us-west-2.amazonaws.com/741f7d55-0312-4036-bd47-ce74d90a2485-1623433607520.png" alt="Kraken" loading="lazy" width="182" height: auto >',
        'chainstack':'<img src="https://images4.bamboohr.com/401182/logos/cropped.jpg?v=29" alt="Chainstack" loading="lazy" width="182" height: auto >',
        'chainlink': '<img src="https://assets-global.website-files.com/5f6b7190899f41fb70882d08/5f760a499b56c47b8fa74fbb_chainlink-logo.svg" alt="Chainlink" loading="lazy" width="182" height: auto >',
        'tessera': '<img src="https://lever-client-logos.s3.us-west-2.amazonaws.com/f711539a-a00c-495a-9563-a5a91b7f7b55-1666821573698.png" alt="Tessera" loading="lazy" width="182" height: auto >',
        'paxos': '<img src="https://paxos.com/wp-content/uploads/2019/01/paxos-logo.svg" alt="paxos" loading="lazy" width="182" height: auto >',
        'close': '<img src="https://lever-client-logos.s3.us-west-2.amazonaws.com/7cee7f57-cca0-4e06-9fa2-82d0871a65f3-1674590276705.png" alt="Close" loading="lazy" width="182" height: auto >',
        'bitcoin': '<img src="resources/bitcoincom.jpg" alt="Bitcoin.com" loading="lazy" width="182" height: auto >',
        'binance': '<img src="resources/binance.png" alt="Binance" loading="lazy" width="182" height: auto >',
        'bitget': '<img src="resources/bitget.png" alt="Bitget" loading="lazy" width="182" height: auto >',
        'stably': '<img src="resources/stably.png" alt="Stably" loading="lazy" width="182" height: auto >',
        'bitstamp': '<img src="resources/bitstamp.png" alt="Bitstamp" loading="lazy" width="182" height: auto >',
        'consensys': '<img src="resources/consensys.png" alt="Consensys" loading="lazy" width="182" height: auto >',
        'ripple': '<img src="resources/ripple.png" alt="Ripple" loading="lazy" width="182" height: auto >',
        'aztec': '<img src="resources/aztec.png" alt="Aztec" loading="lazy" width="182" height: auto >',
        'sygnum': '<img src="resources/sygnum.png" alt="Sygnum" loading="lazy" width="182" height: auto >',
        'circle': '<img src="https://s2-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/298/100/resized/circle-logo_(1).png?1675270133" alt="Circle" loading="lazy" width="182" height: auto >',
        'bittrex': '<img alt="Bittrex" src="https://s2-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/396/100/resized/Symbol-Color-BUS.png?1597265780" loading="lazy" width="75" height: auto >',
        'kaiko': '<img alt="Kaiko" src="https://s3.eu-central-1.amazonaws.com/co.lever.eu.client-logos/55cd4a1a-9f43-486d-a46d-f835a8f4cbe3-1671611915232.png" loading="lazy" width="182" height: auto >',
        'hiro': '<img alt="Hiro" src="https://lever-client-logos.s3.us-west-2.amazonaws.com/7e352a0c-9e67-43aa-857f-18420307b456-1665900839285.png" loading="lazy" width="182" height: auto >',
        'avalabs': '<img alt="AvaLabs" src="https://s4-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/388/300/resized/Ava_Labs._Black.png?1627876089" loading="lazy" width="175" height: auto >',
        'Polygon': '<img alt="Polygon" src="https://lever-client-logos.s3.us-west-2.amazonaws.com/7fb55e63-b76e-4d3c-b15c-ecb8fa5399db-1633069374539.png" loading="lazy" width="182" height: auto >',
        'status': '<img alt="Status" src="https://status.im/img/logo.svg" loading="lazy" width="182" height: auto >',
        'cexio': '<img src="https://images4.bamboohr.com/279437/logos/cropped.jpg?v=35" alt="CEX.IO" loading="lazy" width="182" height: auto >',
        'dappradar': '<img alt="DappRadar" src="https://images4.bamboohr.com/198519/logos/cropped.jpg?v=35 loading="lazy" width="182" height: auto >',
        'web3': '<img src="https://images4.bamboohr.com/104723/logos/cropped.jpg?v=47" alt="Web3" loading="lazy" width="182" height: auto >',
        'smart-token-labs': '<img src="https://workablehr.s3.amazonaws.com/uploads/account/logo/533066/logo" alt="Smart Token Labs" loading="lazy" width="182" height: auto >',
        'avantgarde': '<img src="https://workablehr.s3.amazonaws.com/uploads/account/logo/488245/logo" alt="Avantgarde" loading="lazy" width="182" height: auto >',
        'cryptofinance': '<img src="https://workable-application-form.s3.amazonaws.com/advanced/production/60bf845679ed484c4e780ea0/8024882f-65cc-9c45-b169-229b1e93c0f5" loading="lazy" width="182" height: auto >'
    }
    return company_logos.get(company_name, company_name.upper())
