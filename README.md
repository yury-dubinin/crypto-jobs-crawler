# crypto-jobs-crawler
The idea is to build a dashboard with crypto jobs plus some index number to track industry health. Plus you can search for a job as well :)

# roadmap
- automate scraping positions from most popular HR platforms
- enable simple way of displaying these positions in browser
- enable storage of data as it needed for index calculations
- build better UI with simple search feature
- ...

# how to use?
Given that you have Python 3.5+ and pip instaleed just run pip install -r requirements.txt
Crawler uses just 2 none standard libs:
- selenium 
- json2html

# What we will watch by HR platform
lever:
- https://jobs.lever.co/OpenSea
- https://jobs.lever.co/storyprotocol
- https://jobs.lever.co/ethereumfoundation
- https://jobs.lever.co/chainlink
- https://jobs.lever.co/swissborg
- https://jobs.eu.lever.co/aave
- https://jobs.lever.co/kraken

greenhouse:
- https://boards.greenhouse.io/bitgo
- https://boards.greenhouse.io/genesisglobaltradinginc
- https://boards.greenhouse.io/amun
- https://boards.greenhouse.io/exodus54
- https://boards.eu.greenhouse.io/bitpanda
- https://boards.greenhouse.io/quiknodeinc
- https://boards.greenhouse.io/uniswaplabs
- https://boards.greenhouse.io/alchemy
- https://boards.greenhouse.io/chainalysis

wip:
- https://community.dune.com/wizard-jobs
- https://community.dune.com/careers
- https://www.trmlabs.com/careers#open-roles
- https://kiln.crew.work/jobs
- https://ratedlabs.notion.site/Open-Roles-at-Rated
- https://metrika.recruitee.com/
- https://blockdaemon.com/about/careers/
- https://www.circle.com/en/careers
- https://apply.workable.com/avantgarde/
- https://zenith-caboc-8a4.notion.site/Join-Llama-ad66be1cb28541f5b5346aa37d192b79
- https://bullish.wd3.myworkdayjobs.com/Bullish
- https://www.bitmex.com/careers
- https://verum.capital/careers/
- https://paxos.com/careers/
- https://careers.aplo.io/
- https://join.com/companies/sygnum
- https://coinmarketcap.com/jobs/
- https://jobs.coinmarketcap.com/
- https://bitfinex.recruitee.com/
- https://www.abra.com/careers/
- https://dappradar.com/careers
- https://changenow.io/jobs
- https://jobs.bitvavo.com/en/jobs/
- https://nethermind.io/company
- https://web3labs.jobs.personio.com
- https://jobs.status.im/

# UI staff
For now just converts data to html files and dumps them to resources folder. So, simply run cd ./resources && python3 -m http.server 8000
You sould see something like this on top level:

<img width="308" alt="image" src="https://user-images.githubusercontent.com/62520712/216639741-b947fa0a-3fc9-4457-8b12-8ea01ab7892f.png">
And something like this on company level:

<img width="689" alt="image" src="https://user-images.githubusercontent.com/62520712/216641018-020365bc-d0e3-451f-a131-48ce64d5369d.png">


<table border="1"><tr><th>Engineering Manager, Blockchain (India)</th><td>https://boards.greenhouse.io/bitgo/jobs/6414934002</td></tr><tr><th>Lead QA Engineer</th><td>https://boards.greenhouse.io/bitgo/jobs/6209013002</td></tr><tr><th>Senior Data Engineer</th><td>https://boards.greenhouse.io/bitgo/jobs/6514143002</td></tr><tr><th>Senior Infrastructure Engineer - DevOps India</th><td>https://boards.greenhouse.io/bitgo/jobs/6388857002</td></tr><tr><th>Senior Software Engineer, India</th><td>https://boards.greenhouse.io/bitgo/jobs/6319689002</td></tr><tr><th>Product Marketing Manager</th><td>https://boards.greenhouse.io/bitgo/jobs/5711208002</td></tr><tr><th>Senior Manager of Demand Generation</th><td>https://boards.greenhouse.io/bitgo/jobs/6560378002</td></tr><tr><th>Product Manager</th><td>https://boards.greenhouse.io/bitgo/jobs/5089954002</td></tr><tr><th>AML Analyst (Germany)</th><td>https://boards.greenhouse.io/bitgo/jobs/5548606002</td></tr><tr><th>Risk Outsourcing Manager (Germany)</th><td>https://boards.greenhouse.io/bitgo/jobs/6571836002</td></tr><tr><th>Associate - Digital Asset Sales &amp; Research (US)</th><td>https://boards.greenhouse.io/bitgo/jobs/5993071002</td></tr><tr><th>Associate - Institutional Sales (APAC)</th><td>https://boards.greenhouse.io/bitgo/jobs/5732221002</td></tr><tr><th>Associate - Institutional Sales (India)</th><td>https://boards.greenhouse.io/bitgo/jobs/6455495002</td></tr></table>
