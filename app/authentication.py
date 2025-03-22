# https://www.pathofexile.com/developer/docs/authorization
# https://docs.python.org/3/library/secrets.html

import base64
import hashlib
import secrets
import uuid

from urllib.parse import urlencode  # python3


def do_pkce():
    # https://github.com/RomeoDespres/pkce/blob/master/pkce/__init__.py
    code_verifier = secrets.token_urlsafe(96)[:32]
    hashed = hashlib.sha256(code_verifier.encode("ascii")).digest()
    encoded = base64.urlsafe_b64encode(hashed)
    code_challenge = encoded.decode("ascii")[:-1]
    return {
        "code_verifier": code_verifier,
        "code_challenge": code_challenge,
    }


def get_auth_url():
    pkce_pair = do_pkce()
    base = "https://www.pathofexile.com/oauth/authorize"
    query_parameters = {
        "client_id": "example",
        "response_type": "code",
        "scope": "account:*",
        "state": uuid.uuid4(),
        "redirect_uri": "http://localhost/complete",
        "code_challenge": pkce_pair["code_challenge"],
        "code_challenge_method": "S256",
    }
    query_string = urlencode(query_parameters)
    url = base + "?" + query_string
    return url


print(get_auth_url())

# Work in Progress
