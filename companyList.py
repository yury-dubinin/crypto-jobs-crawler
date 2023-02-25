from companyItem import CompanyItem
from scrapeLever import ScrapeLever
from scrapeGreenhouse import ScrapeGreenhouse
from scrapeSmartrecruiters import ScrapeSmartrecruiters
from scrapeRecruitee import ScrapeRecruitee
from scrapeBinance import ScrapeBinance


def getCompanyList() -> list():
    company_list = []
    company_list.append(CompanyItem("kraken",  "https://jobs.lever.co/kraken", ScrapeLever, "https://kraken.com","Exchange"))
    company_list.append(CompanyItem("paxos",  "https://paxos.com/careers/role", ScrapeGreenhouse, "https://paxos.com", "Stable Coin"))
    company_list.append(CompanyItem("circle",  "https://boards.greenhouse.io/circle", ScrapeGreenhouse, "https://circle.com", "Stable Coin"))
    company_list.append(CompanyItem("status",  "https://jobs.status.im", ScrapeGreenhouse, "https://status.im","Messanger"))
    company_list.append(CompanyItem("OKX",  "https://boards.greenhouse.io/OKX", ScrapeGreenhouse, "https://okx.com","Exchange"))
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
    company_list.append(CompanyItem("chainlink",  "https://jobs.lever.co/chainlink", ScrapeLever, "https://chain.link","Blockchain"))
    company_list.append(CompanyItem("swissborg",  "https://jobs.lever.co/swissborg", ScrapeLever, "https://swissborg.com","Exchange"))
    company_list.append(CompanyItem("OpenSea",  "https://jobs.lever.co/OpenSea", ScrapeLever, "https://opensea.io","NFT"))
    company_list.append(CompanyItem("storyprotocol",  "https://jobs.lever.co/storyprotocol", ScrapeLever, "https://www.storyprotocol.xyz","Protocol"))
    company_list.append(CompanyItem("ethereumfoundation",  "https://jobs.lever.co/ethereumfoundation", ScrapeLever, "https://ethereum.org","Blockchain"))
    company_list.append(CompanyItem("aave",  "https://jobs.eu.lever.co/aave", ScrapeLever, "https://aave.com","Protocol"))
    company_list.append(CompanyItem("crypto",  "https://jobs.lever.co/crypto", ScrapeLever, "https://crypto.com","Exchange"))
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

    return company_list
