import pandas as pd
import numpy as np

class Firewall:
    def __init__(self, path):
        """
        @para
        path: string: the path of the input file
        """
        self.path = path
        self.df = pd.read_csv(path)
        self.df.columns = ['direction','protocol','port','ip_address']
        sp = []
        for item in list(self.df['port']):
            n = item.split('-')
            if len(n) == 1:
                n.append(n[0])
            sp.append(n)
        self.df['startport'] = np.array(sp)[:,0] 
        self.df['endport'] = np.array(sp)[:,1] 
        self.df.startport=  self.df.startport.astype(int)
        self.df.endport =  self.df.endport.astype(int)
            
        sp = []
        for item in list(self.df['ip_address']):
            n = item.split('-')
            if len(n) == 1:
                n.append(n[0])
            sp.append(n)

        self.df['startip'] = np.array(sp)[:,0] 
        self.df['endip'] = np.array(sp)[:,1] 
        
            
        
    def accept_packet(self, direc, pro, port, ip) :
        """
        @para
        direc: direction (string): “inbound” or “outbound"
        pro: protocol (string): exactly one of “tcp” or “udp”, all lowercase 
        port: (integer): – an integer in the range [1, 65535]
        ip: ip_address (string): a single well-formed IPv4 address.
        @return
        true if matches the rules
        """
        
        df = self.df
        # check input style
        if direc != "inbound" and direc != "outbound":
            return False
        if pro !=  "udp" and pro != "tcp":
            return False

        cur = df[(df['direction'] == direc) & (df['protocol'] == pro) & (df['startport'] <= port)& (df['endport'] >= port) & (df['startip'] <= ip) & (df['endip'] >= ip)]

        if len(cur) > 0:
            return True

        return False