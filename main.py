import os

vercel_url = "osmosis-frontend-qtpf9r606-osmo-labs.vercel.app"
gh_out = f"environment_url={vercel_url}"
os.system(f'echo "{gh_out}" >> $GITHUB_OUTPUT')
os.system(f'echo "{gh_out}" >> $GITHUB_ENV')
os.system(f'echo Vercel deployment: "{gh_out}" >> $GITHUB_STEP_SUMMARY')
