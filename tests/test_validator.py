from redpilot.utils.validator import validate_target, validate_url, sanitize_domain, validate_ip

def test_validate_ip():
    # Valid public IPs
    assert validate_ip("8.8.8.8") is True
    assert validate_ip("1.1.1.1") is True
    assert validate_ip("2001:4860:4860::8888") is True

    # Invalid string/format
    assert validate_ip("invalid") is False
    assert validate_ip("256.256.256.256") is False
    assert validate_ip("") is False

    # Restricted IPs
    assert validate_ip("127.0.0.1") is False       # Loopback
    assert validate_ip("::1") is False             # IPv6 Loopback
    assert validate_ip("169.254.1.1") is False     # Link-local
    assert validate_ip("224.0.0.1") is False       # Multicast
    assert validate_ip("ff02::1") is False         # IPv6 Multicast

def test_validate_target():
    assert validate_target("google.com") is True
    assert validate_target("127.0.0.1") is True
    assert validate_target("invalid target!") is False

def test_validate_url():
    assert validate_url("https://google.com") is True
    assert validate_url("http://localhost:8080") is True
    assert validate_url("google.com") is False

def test_sanitize_domain():
    assert sanitize_domain("https://google.com") == "google.com"
    assert sanitize_domain("http://api.target.local/") == "api.target.local"
    assert sanitize_domain("target.com") == "target.com"
