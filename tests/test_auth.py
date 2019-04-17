from labelbot import auth

rsa_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAxgHlyqhl8bMNT8opV631hJy1aJ7guF7iDfBMa+V3kKzo5OUu
h5VGQ5xWQPZDf27brxgL0ywvfYzw+YaP6TaMcmUR8nzE+gr9B+GOc92GtVrZd4dd
o2CL/wLpANUwMZ2sCWWHg3sf5S5KRbg0WUPLk8dqnwINJKUnd1uZW4M76FMJxg92
iQIMgdngEoos+bGE0X8mkClics0hMxZcUUsATV9YnrOztnx356/4yaZaRySp7gqd
bzuDHgi4kJi228eqWH12O6Q2tooOb1WZHUdOjlcYyjulipNiA9G0SnanN9YxmNGc
+0iLRQvlvuHPxA490d/WR+iMXAGHmUN40PYucwIDAQABAoIBAQC6ze2CPU84MOld
HmfUnXzk6IdJNaLirjlsVwlyPaGIr2hlEkbMiSsp/CNv1CWn4umFDhWR27zOIRry
/l1k8x6bifjdoZKgJ5/CQK0JaLR/Aj/qQZ441YweQRubuoVmOc+ladDoXU+hAwP1
NKzGjmxQdjGD5AaMTPen5pYPPQdWzN5AvTH/Q3FIFsGAJ/JZIj3CjxJ5zyDdlYvJ
PKW/3E5DYSCVyjopjZhiNDHIa8Ur8e/b0S7EmxtRZc3IdV1nLAgRCkOkOZo9i0D8
RN+Ro5Aiw/DUcYl4VzVxdikAASu9+Fey9NFDceeClKnIe/L5FXHjXR8VXuaw60AY
htI6g7LpAoGBAPSsiu1Fqtp+s07nHeeChTqPgpSSx7ihhEgZ/TqCElEl4xG4mkMg
vaSX9nS5Mm/cUF3mD40KwS+eaBxIVtk7uyQ80lBEc/lC/7txGKVCFWB+x7ChxPxI
HLA0pBg/O5g9HLtFXGDJn4WwbFU/j1luPuwNOFD/yqTNpQUiubuq9is9AoGBAM8s
V637me/rkyPDP0/up93Ox3szguIv03CaKqvL03ZJU/DZIMwtQgpvIKrBFhlQMG1Q
KkmgeCgpmLjgCIElXqLldur2TSag6Mtw2suomjELLNUpgnDs1hdq1xBcZCDyyGCj
F+AUjEun2+9TVLeGxvjtY1rB2a2Kc/k3XQXi8htvAoGBALYWdqnQUC+dXUpaO+og
O5ByXwa9Gb+xDGYwWUGirYkQviVhEgTlJ92HblY9wWh4OKM45NfdahpLNEXgHCo9
BrAYR5iO6RRXJUTVDTdnr8sJbwlnytbJv/fupTSaUnqg+HHyU6aARqTSwDzNOZyf
rFo2GHRHeQMfPDFPP5SHzf4tAoGBAKsizRcKhMH8zqI3MkCcO4ztuDkcdxzTNw2I
PIGHsRnAPxfwtLgVFr25yLllIRUt+aMDGruRVFCQ8/icEEpmjUNw3AgCB/9F4qfT
hNnBYAXtXk6DqJ4R9lSHzDpWp9vT0hSKBTn0n2QLuJF9O7kTG6AbsPwSr/c8LMsM
ocowC6D/AoGAOEy3olvgdY9lWr6zHdK745qnFK2hHuAT4LEw+37/1WucNIXxItM8
RdDCSLSlSxkpOjWFJPhdW19i/9O4QNNwAF5wCtlIFeN+HF24LwDF7I/Xj26pIKBj
8lEnfws5Dn7I9sG0wBn+5px52jgOqiKzjy3jcIENBRO6i1OZ8c07NmM=
-----END RSA PRIVATE KEY-----"""


def test_auth_jwt_token():
    """Tests that jwt_token is truthy"""
    result = auth.generate_jwt_token(rsa_key.encode("utf8"), 12334)
    assert result


class TestAuthenticateRequest:
    SECRET = "d653a60adc0a16a93e99f0620a67f4a67ef901df"
    BODY = "Hello, World!"
    SIGN = "sha1=8727505c9c036b2337a06d2e63f091a7aa41ae60"

    def test_correct_hash(self):
        result = auth.authenticate_request(self.SECRET, self.BODY, self.SIGN)
        assert result

    def test_incorrect_hash(self):
        result = auth.authenticate_request(self.SECRET, self.BODY.lower(), self.SIGN)
        assert not result

    def test_no_signature(self):
        result = auth.authenticate_request(self.SECRET, self.BODY, None)
        assert not result
