import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "args": [
            *browser_type_launch_args.get("args", []),
            "--no-proxy-server"
        ]
    }

@pytest.fixture(scope="session")
def web_url():
    return "http://metalmekid.duckdns.org:5000"