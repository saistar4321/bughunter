import argparse
from core import (
    recon, subdomain_takeover, ssrf_scanner, idor_bruteforce, cors_check,
    cve_js_scanner, crlf_injector, js_parser, parameter_pollution,
    open_redirect_xss, auth_bypass_checker, graphql_enum_leak, token_leak_scanner
)

parser = argparse.ArgumentParser(description="BugHunter - Automated Bug Bounty Recon Tool")
parser.add_argument("domain", help="Target domain for scanning")
parser.add_argument("--all", action="store_true", help="Run all modules")
parser.add_argument("--takeover", action="store_true", help="Subdomain Takeover Detection")
parser.add_argument("--ssrf", action="store_true", help="SSRF Scanner")
parser.add_argument("--idor", action="store_true", help="IDOR Brute Forcer")
parser.add_argument("--cors", action="store_true", help="CORS Misconfig Scanner")
parser.add_argument("--cve", action="store_true", help="JS CVE Scanner")
parser.add_argument("--crlf", action="store_true", help="CRLF Injection")
parser.add_argument("--js", action="store_true", help="JS Parser + Endpoint Extractor")
args = parser.parse_args()

if args.all or args.takeover:
    subdomain_takeover.run(args.domain)
if args.all or args.ssrf:
    ssrf_scanner.run(args.domain)
if args.all or args.idor:
    idor_bruteforce.run(args.domain)
if args.all or args.cors:
    cors_check.run(args.domain)
if args.all or args.cve:
    cve_js_scanner.run(args.domain)
if args.all or args.crlf:
    crlf_injector.run(args.domain)
if args.all or args.js:
    js_parser.run(args.domain)
if args.all:
    recon.run(args.domain)
    parameter_pollution.run(args.domain)
    open_redirect_xss.run(args.domain)
    auth_bypass_checker.run(args.domain)
    graphql_enum_leak.run(args.domain)
    token_leak_scanner.run(args.domain)