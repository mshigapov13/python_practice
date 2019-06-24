import dns.resolver
import pprint

name = 'python.astrotech.io'

answer = dns.resolver.query(name, 'MX')
print(answer.canonical_name)
print()
print(answer.expiration)
print()
print(answer.response.answer)
print()
print(answer.rrset)
print()
pprint.pprint(answer.rrset.items)

records = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA']
for record in records:
    answer = dns.resolver.query(name, record)
    print(answer.rrset)


import dns.reversename


domain_address = dns.reversename.from_address('8.8.4.4')
ip_address = dns.reversename.to_address(domain_address)
print(f'Domain address = {domain_address}, ip address = {ip_address}')