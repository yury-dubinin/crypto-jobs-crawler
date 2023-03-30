from src.company_item import CompanyItem
from src.scrape_lever import ScrapeLever
from src.scrape_greenhouse import ScrapeGreenhouse
from src.scrape_smartrecruiters import ScrapeSmartrecruiters
from src.scrape_recruitee import ScrapeRecruitee
from src.scrape_binance import ScrapeBinance
from src.scrape_bamboohr import ScrapeBamboohr
from src.scrape_consensys import ScrapeConsensys
from src.scrape_ripple import ScrapeRipple
from src.scrape_workable import ScrapeWorkable


def get_company_list() -> list():
    return [CompanyItem("kraken", "https://jobs.lever.co/kraken", ScrapeLever, "https://kraken.com", "Exchange"),
            CompanyItem("chainlink", "https://jobs.lever.co/chainlink", ScrapeLever, "https://chain.link",
                        "Blockchain"),
            CompanyItem('ethglobal', 'https://jobs.lever.co/ETHGlobal', ScrapeLever, 'https://ethglobal.com',
                        'Community'),
            CompanyItem("chainstack", "https://chainstack.bamboohr.com/jobs", ScrapeBamboohr,
                        "https://chainstack.com", "Infra"),
            CompanyItem("tessera", "https://jobs.lever.co/ftc", ScrapeLever, "https://tessera.co", "NFT"),
            CompanyItem("paxos", "https://paxos.com/careers/role", ScrapeGreenhouse, "https://paxos.com",
                        "Stable Coin"),
            CompanyItem('fuellabs', 'https://jobs.lever.co/fuellabs', ScrapeLever, 'https://www.fuel.network',
                        'Blockchain'),
            CompanyItem('wintermute', 'https://jobs.lever.co/wintermute-trading', ScrapeLever,
                        'https://www.wintermute.com',
                        'Trading'),
            CompanyItem("bitcoin", "https://www.bitcoin.com/jobs/#joblist", ScrapeGreenhouse,
                        "https://www.bitcoin.com", 'Exchange'),
            CompanyItem("cexio", "https://cexio.bamboohr.com/jobs", ScrapeBamboohr, "https://cex.io", "Exchange"),
            CompanyItem("circle", "https://boards.greenhouse.io/circle", ScrapeGreenhouse, "https://circle.com",
                        "Stable Coin"),
            CompanyItem("status", "https://jobs.status.im", ScrapeGreenhouse, "https://status.im", "Messanger"),
            CompanyItem("OKX", "https://boards.greenhouse.io/OKX", ScrapeGreenhouse, "https://okx.com",
                        "Exchange"),
            CompanyItem("bittrex", "https://boards.greenhouse.io/bittrex", ScrapeGreenhouse,
                        "https://global.bittrex.com", 'Exchange'),
            CompanyItem("kaiko", "https://jobs.eu.lever.co/kaiko", ScrapeLever, "https://www.kaiko.com", "Data"),
            CompanyItem("bitmex", "https://boards.greenhouse.io/bitmex", ScrapeGreenhouse, "https://bitmex.com",
                        "Exchange"),
            CompanyItem("bitgo", "https://boards.greenhouse.io/bitgo", ScrapeGreenhouse, "https://bitgo.com",
                        "Exchange"),
            CompanyItem("bitpanda", "https://boards.eu.greenhouse.io/bitpanda", ScrapeGreenhouse,
                        "https://bitpanda.com", "Exchange"),
            CompanyItem("uniswaplabs", "https://boards.greenhouse.io/uniswaplabs", ScrapeGreenhouse,
                        "https://uniswap.org", "Exchange Protocol"),
            CompanyItem("moonpay", "https://boards.greenhouse.io/moonpay", ScrapeGreenhouse,
                        "https://www.moonpay.com", "Payments"),
            CompanyItem("moonwalk", "https://boards.greenhouse.io/moonwalk", ScrapeGreenhouse,
                        "https://www.moonwalk.com", "Platform"),
            CompanyItem("blockdaemon", "https://boards.greenhouse.io/blockdaemon", ScrapeGreenhouse,
                        "https://www.blockdaemon.com", "Staking & Infra"),
            CompanyItem("figment", "https://boards.greenhouse.io/figment", ScrapeGreenhouse,
                        "https://www.figment.io", "Staking & Infra"),
            CompanyItem("quiknodeinc", "https://boards.greenhouse.io/quiknodeinc", ScrapeGreenhouse,
                        "https://www.quicknode.com", "Staking & Infra"),
            CompanyItem("genesisglobaltradinginc", "https://boards.greenhouse.io/genesisglobaltradinginc",
                        ScrapeGreenhouse, "https://genesistrading.com", "OTC Trading"),
            CompanyItem("amun", "https://boards.greenhouse.io/amun", ScrapeGreenhouse, "https://www.21.co", "OTC"),
            CompanyItem("exodus54", "https://boards.greenhouse.io/exodus54", ScrapeGreenhouse,
                        "https://www.exodus.com", "Wallet"),
            CompanyItem("alchemy", "https://boards.greenhouse.io/alchemy", ScrapeGreenhouse,
                        "https://www.alchemy.com", "Dev & Infra"),
            CompanyItem("chainalysis", "https://boards.greenhouse.io/chainalysis", ScrapeGreenhouse,
                        "https://www.chainalysis.com", "Crypto Research"),
            CompanyItem("magiceden", "https://boards.greenhouse.io/magiceden", ScrapeGreenhouse,
                        "https://www.magiceden.io", "NFT"),
            CompanyItem("aztec", "https://boards.eu.greenhouse.io/aztec", ScrapeGreenhouse,
                        "https://aztec.network",
                        "Protocol"),
            CompanyItem("nethermind", "https://boards.eu.greenhouse.io/nethermind", ScrapeGreenhouse,
                        "https://nethermind.io", "Crypto software"),
            CompanyItem("dfinity", "https://boards.greenhouse.io/dfinity", ScrapeGreenhouse, "https://dfinity.org",
                        "Blockchain"),
            CompanyItem('stellar', 'https://boards.greenhouse.io/stellar', ScrapeGreenhouse,
                        'https://stellar.org', 'Blockchain'),
            CompanyItem("parity", "https://boards.greenhouse.io/parity", ScrapeGreenhouse, "https://www.parity.io",
                        "Infra"),
            CompanyItem("optimism", "https://boards.greenhouse.io/optimism", ScrapeGreenhouse,
                        "https://www.optimism.io", "L2 protocol"),
            CompanyItem("flashbots", "https://boards.greenhouse.io/flashbots", ScrapeGreenhouse,
                        "https://www.flashbots.net", "ETH MEV"),
            CompanyItem("oplabs", "https://boards.greenhouse.io/oplabs", ScrapeGreenhouse, "https://www.oplabs.co",
                        "L2 protocol"),
            CompanyItem("bitfinex", "https://bitfinex.recruitee.com", ScrapeRecruitee, "https://www.bitfinex.com",
                        "Exchange"),
            CompanyItem("binance", "https://www.binance.com/en/careers/job-openings", ScrapeBinance,
                        "https://www.binance.com", "Exchange"),
            CompanyItem("coinmarketcap", "https://careers.smartrecruiters.com/B6/coinmarketcap",
                        ScrapeSmartrecruiters, "https://coinmarketcap.com", "Information"),
            CompanyItem("trustwallet", "https://careers.smartrecruiters.com/B6/trustwallet", ScrapeSmartrecruiters,
                        "https://trustwallet.com", "Wallet"),
            CompanyItem("Swissquote", "https://careers.smartrecruiters.com/Swissquote", ScrapeSmartrecruiters,
                        "https://en.swissquote.com", "Exchange"),
            CompanyItem("Coinshift", "https://jobs.lever.co/Coinshift", ScrapeLever, "https://coinshift.xyz",
                        "Custody software"),
            CompanyItem("swissborg", "https://jobs.lever.co/swissborg", ScrapeLever, "https://swissborg.com",
                        "Exchange"),
            CompanyItem("OpenSea", "https://jobs.lever.co/OpenSea", ScrapeLever, "https://opensea.io", "NFT"),
            CompanyItem("storyprotocol", "https://jobs.lever.co/storyprotocol", ScrapeLever,
                        "https://www.storyprotocol.xyz", "Protocol"),
            CompanyItem("ethereumfoundation", "https://jobs.lever.co/ethereumfoundation", ScrapeLever,
                        "https://ethereum.org", "Blockchain"),
            CompanyItem("aave", "https://jobs.eu.lever.co/aave", ScrapeLever, "https://aave.com", "Protocol"),
            CompanyItem("crypto", "https://jobs.lever.co/crypto", ScrapeLever, "https://crypto.com", "Exchange"),
            CompanyItem("Luxor", "https://jobs.lever.co/LuxorTechnology", ScrapeLever, "https://www.luxor.tech",
                        "Mining"),
            CompanyItem("anchorage", "https://jobs.lever.co/anchorage", ScrapeLever, "https://www.anchorage.com",
                        "Trading"),
            CompanyItem("biconomy", "https://jobs.lever.co/biconomy", ScrapeLever, "https://www.biconomy.io",
                        "Infra"), CompanyItem("avalabs", "https://boards.greenhouse.io/avalabs", ScrapeGreenhouse,
                                              "https://www.avalabs.org",
                                              "Blockchain"),
            CompanyItem("Polygon", "https://jobs.lever.co/Polygon", ScrapeLever, "https://polygon.technology",
                        "Blockchain"),
            CompanyItem("tokenmetrics", "https://jobs.lever.co/tokenmetrics", ScrapeLever,
                        "https://www.tokenmetrics.com", "Information"),
            CompanyItem("offchainlabs", "https://jobs.lever.co/offchainlabs", ScrapeLever,
                        "https://offchainlabs.com", "Protocol"),
            CompanyItem("subspacelabs", "https://jobs.lever.co/subspacelabs", ScrapeLever,
                        "https://subspace.network", "Blockchain Infra"),
            CompanyItem("tron", "https://boards.greenhouse.io/rainberry", ScrapeGreenhouse, "https://tron.network",
                        "Blockchain"),
            CompanyItem("messari", "https://boards.greenhouse.io/messari", ScrapeGreenhouse, "https://messari.io",
                        "Information"),
            CompanyItem("copperco", "https://boards.eu.greenhouse.io/copperco", ScrapeGreenhouse,
                        "https://copper.co", "Custody"),
            CompanyItem("digitalasset", "https://boards.greenhouse.io/digitalasset", ScrapeGreenhouse,
                        "https://www.digitalasset.com", "Custody"),
            CompanyItem("ramp.network", "https://jobs.lever.co/careers.ramp.network", ScrapeLever,
                        "https://ramp.network", "Payments"),
            CompanyItem("ledger", "https://jobs.lever.co/ledger", ScrapeLever, "https://www.ledger.com", "Wallet"),
            CompanyItem("layerzerolabs", "https://boards.greenhouse.io/layerzerolabs", ScrapeGreenhouse,
                        "https://layerzero.network", "Infra"),
            CompanyItem("request", "https://jobs.lever.co/request", ScrapeLever, "https://request.network",
                        "Payments"), CompanyItem('okcoin', 'https://boards.greenhouse.io/okcoin', ScrapeGreenhouse,
                                                 'https://www.okcoin.com',
                                                 'Exchange'),
            CompanyItem("immutable", "https://jobs.lever.co/immutable", ScrapeLever, "https://www.immutable.com",
                        "NFT"),
            CompanyItem("web3auth", "https://jobs.lever.co/TorusLabs", ScrapeLever, "https://web3auth.io", "Auth"),
            CompanyItem("jumpcrypto", "https://boards.greenhouse.io/jumpcrypto", ScrapeGreenhouse,
                        "https://jumpcrypto.com", "Infra"),
            CompanyItem("oasisnetwork", "https://boards.greenhouse.io/oasisnetwork", ScrapeGreenhouse,
                        "https://oasisprotocol.org", "Protocol"),
            CompanyItem("consensys", "https://consensys.net/open-roles", ScrapeConsensys, "https://consensys.net",
                        "Infra"),
            CompanyItem("poap", "https://boards.greenhouse.io/poaptheproofofattendanceprotocol", ScrapeGreenhouse,
                        "https://poap.xyz", "Protocol"),
            CompanyItem("chainsafesystems", "https://boards.greenhouse.io/chainsafesystems", ScrapeGreenhouse,
                        "https://chainsafe.io", "Infra"),
            CompanyItem("ripple", "https://ripple.com/careers/all-jobs", ScrapeRipple, "https://ripple.com",
                        "Blockchain"),
            CompanyItem("kadena", "https://boards.greenhouse.io/kadenallc", ScrapeGreenhouse, "https://kadena.io",
                        "Blockchain"),
            CompanyItem("EigenLabs", "https://boards.greenhouse.io/layrlabs", ScrapeGreenhouse,
                        "https://www.v1.eigenlayer.xyz", "Infra"),
            CompanyItem("cere-network", "https://jobs.lever.co/cere-network", ScrapeLever, "https://cere.network",
                        "Infra"),
            CompanyItem('sygnum', 'https://sygnum.bamboohr.com/careers', ScrapeBamboohr, 'https://www.sygnum.com',
                        'Crypto bank'),
            CompanyItem('matterlabs', 'https://jobs.eu.lever.co/matterlabs', ScrapeLever, 'https://matter-labs.io',
                        'Protocol'),
            CompanyItem('iofinnet', 'https://iofinnethr.bamboohr.com/jobs/?source=bamboohr', ScrapeBamboohr,
                        'https://www.iofinnet.com', 'Custody'),
            CompanyItem("galaxydigitalservices", "https://boards.greenhouse.io/galaxydigitalservices",
                        ScrapeGreenhouse,
                        "https://www.galaxy.com", 'Trading'),
            CompanyItem("hiro", "https://jobs.lever.co/hiro", ScrapeLever, "https://www.hiro.so", "Infra"),
            CompanyItem('web3', 'https://web3.bamboohr.com/jobs', ScrapeBamboohr, 'https://web3.foundation',
                        'web3'),
            CompanyItem('dappradar', 'https://dappradar.bamboohr.com/careers', ScrapeBamboohr,
                        'https://dappradar.com',
                        'Exchange & NFT'),
            CompanyItem("solanafoundation", "https://boards.greenhouse.io/solanafoundation", ScrapeGreenhouse,
                        "https://solana.org", "Blockchain"),
            CompanyItem("worldcoin", "https://boards.greenhouse.io/worldcoinorg", ScrapeGreenhouse,
                        "https://worldcoin.org", "Blockchain"),
            CompanyItem("edgeandnode", "https://boards.greenhouse.io/edgeandnode", ScrapeGreenhouse,
                        "https://edgeandnode.com", "Infra"),
            CompanyItem("clearmatics", "https://boards.greenhouse.io/clearmatics", ScrapeGreenhouse,
                        "https://www.clearmatics.com", "Protocol"),
            CompanyItem('bitstamp', 'https://apply.workable.com/bitstamp/#jobs', ScrapeWorkable,
                        'https://www.bitstamp.net',
                        'Exchange'),
            CompanyItem('smart-token-labs', 'https://apply.workable.com/smart-token-labs', ScrapeWorkable,
                        'https://smarttokenlabs.com', 'Web3 bridge'),
            CompanyItem('avantgarde', 'https://apply.workable.com/avantgarde', ScrapeWorkable,
                        'https://avantgarde.finance',
                        'Asset Management'),
            CompanyItem('stably', 'https://apply.workable.com/stably', ScrapeWorkable, 'https://stably.io',
                        'Stable Coin'),
            CompanyItem('cryptofinance', 'https://apply.workable.com/cryptofinance', ScrapeWorkable,
                        'https://www.crypto-finance.com', 'Exchange'),
            CompanyItem('bitget', 'https://apply.workable.com/bitget', ScrapeWorkable, 'https://www.bitget.com/en',
                        'Exchange')]


def build_img_tag(name):
    return f'<img src="resources/{name}.png" alt="{name.title()}" loading="lazy" width="182" height: auto >'


def get_logo(company_name):
    company_logos = {
        'kraken': build_img_tag(company_name),
        'ethglobal': build_img_tag(company_name),
        'chainstack': build_img_tag(company_name),
        'chainlink': build_img_tag(company_name),
        'tessera': '<img src="https://lever-client-logos.s3.us-west-2.amazonaws.com/f711539a-a00c-495a-9563-a5a91b7f7b55-1666821573698.png" alt="Tessera" loading="lazy" width="182" height: auto >',
        'paxos': build_img_tag(company_name),
        'close': '<img src="https://lever-client-logos.s3.us-west-2.amazonaws.com/7cee7f57-cca0-4e06-9fa2-82d0871a65f3-1674590276705.png" alt="Close" loading="lazy" width="182" height: auto >',
        'bitcoin': build_img_tag(company_name),
        'binance': build_img_tag(company_name),
        'bitget': build_img_tag(company_name),
        'stably': build_img_tag(company_name),
        'bitstamp': build_img_tag(company_name),
        'consensys': build_img_tag(company_name),
        'ripple': build_img_tag(company_name),
        'aztec': build_img_tag(company_name),
        'stellar': build_img_tag(company_name),
        'sygnum': build_img_tag(company_name),
        'okcoin': build_img_tag(company_name),
        'matterlabs': build_img_tag(company_name),
        'clearmatics': build_img_tag(company_name),
        'worldcoin': build_img_tag(company_name),
        'edgeandnode': build_img_tag(company_name),
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
        'cryptofinance': '<img src="https://workable-application-form.s3.amazonaws.com/advanced/production/60bf845679ed484c4e780ea0/8024882f-65cc-9c45-b169-229b1e93c0f5" loading="lazy" width="182" height: auto >',
        'Luxor': '<img alt="Luxor" src="https://lever-client-logos.s3.us-west-2.amazonaws.com/1d9e9b01-d69d-4a75-95ff-a48d3687d478-1623209594362.png" loading="lazy" width="182" height: auto >',
        'anchorage': '<img alt="Anchorage" src="https://lever-client-logos.s3.us-west-2.amazonaws.com/a0746087-e4a6-446d-9122-c353f372d3e7-1669735538820.png" loading="lazy" width="182" height: auto >',
        'biconomy': '<img alt="Biconomy" src="https://lever-client-logos.s3.us-west-2.amazonaws.com/73c89f44-01e6-4d0a-9354-9661e253e4bf-1663252279527.png" loading="lazy" width="182" height: auto >',
        'solanafoundation': '<img alt="Solana" src="https://s4-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/510/100/resized/Foundation_Linkedin.jpg?1656548101" loading="lazy" width="182" height: auto >',
        'fuellabs': '<img alt="FuelLabs" src="https://lever-client-logos.s3.us-west-2.amazonaws.com/1c78fcea-637a-4e49-8e01-52a7daa4431e-1648557736900.png" loading="lazy" width="182" height: auto >'
    }
    return company_logos.get(company_name, company_name.upper())