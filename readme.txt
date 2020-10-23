THIS TOOL WILL EXTRACT USERNAMES AND PASSWORD OVER HTTP/S

REQUIRMENTS:
PYTHON3 
SCAPY

IF YOU DO NOT HAVE SCAPY:
RUN-->
pip3 install --pre scapy[complete]

sudo pip install scapy-http

TO RUN THE PROGRAM:
git clone https://github.com/mpandey67/cred-extractor
cd cred-extractor
python3 cred-extractor.py



NOTE- 
1.You can extract credentials over HTTP if you want to do it on https you can downgrade https to http.
2.To sniff the credentials over the network you have to be at the middle of the connection for that you can use my pre built tool (middle-man) : https://github.com/mpandey67/middle-man

