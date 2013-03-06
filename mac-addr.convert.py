# #!/usr/bin/env python  
""" Function to convert mac addr to standard format. """  

#addr = "0014.4f39.ef30"

def normalize(addr):  

    # Determine which delimiter style out input is using
    if "." in addr:
     delimiter = "."
    elif ":" in addr:
     delimiter = ":"
    elif "-" in addr:
     delimiter = "-"

    # Eliminate the delimiter
    m = addr.replace(delimiter, "")

    m = m.lower()

    # Normalize
    n= ":".join(["%s%s" % (m[i], m[i+1]) for i in range(0,12,2)])

    return n
    #print n
