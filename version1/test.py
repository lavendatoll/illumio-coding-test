import Firewall 
rules_path = "../test/input/rules.csv"

fw = Firewall.Firewall(rules_path)
res = fw.accept_packet("inbound","tcp",11000,"192.168.1.5")
print(res)

res = fw.accept_packet("inbound", "tcp", 80, "192.168.1.2")
print(res)

res = fw.accept_packet("inbound", "udp", 53, "192.168.2.1")
print(res)

res = fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11")
print(res)

res = fw.accept_packet("inbound", "tcp", 81, "192.168.1.2")
print(res)

res = fw.accept_packet("inbound", "udp", 24, "52.12.48.92")
print(res)

res = fw.accept_packet("inbount", "udp", 24, "52.12.48.92")
print(res)