import pandas as pd
import numpy as np
SIZE = 2
class Firewall:
    def __init__(self, path):
        """
        @para
        path: string: the path of the input file
        """
        self.path = path
        
       
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
        
        df = pd.read_csv(self.path,chunksize = SIZE)
        df.columns = ['direction','protocol','port','ip_address']
        
        # check input style
        if direc != "inbound" and direc != "outbound":
            return False
        if pro !=  "udp" and pro != "tcp":
            return False

       
        for chunk in df:
            
            # check direction and protocol
            chunkcopy = chunk[(chunk['direction'] == direc) & (chunk['protocol'] == pro)].copy()
            if len(chunkcopy) == 0:
                continue
        
            # check port
            sp = []
            for item in list(chunkcopy['port']):
                n = item.split('-')
                if len(n) == 1:
                    n.append(n[0])
                sp.append(n)
                
            chunkcopy['startport'] = np.array(sp)[:,0] 
            chunkcopy['endport'] = np.array(sp)[:,1] 
            chunkcopy.startport=  chunkcopy.startport.astype(int)
            chunkcopy.endport =  chunkcopy.endport.astype(int)
            
            chunkcopy = chunkcopy[(chunkcopy['startport'] <= port)& (chunkcopy['endport'] >= port)]

            if len(chunkcopy) == 0:
                continue

            # check ip
            sp = []
            for item in list(chunkcopy['ip_address']):
                n = item.split('-')
                if len(n) == 1:
                    n.append(n[0])
                sp.append(n)

            chunkcopy['startip'] = np.array(sp)[:,0] 
            chunkcopy['endip'] = np.array(sp)[:,1] 
            chunkcopy = chunkcopy[(chunkcopy['startip'] <= ip) & (chunkcopy['endip'] >= ip)]
           
            if len(chunkcopy) > 0:
                return True


        return False