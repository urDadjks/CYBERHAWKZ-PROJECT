print(''' __      __ _____________________       _____________________________   ____ ___ __________ .___ ________________.___. 
/  \    /  \\_   _____/\______   \     /   _____/\_   _____/\_   ___ \ |    |   \\______   \|   |\__    ___/\__  |   | 
\   \/\/   / |    __)_  |    |  _/     \_____  \  |    __)_ /    \  \/ |    |   / |       _/|   |  |    |    /   |   | 
 \        /  |        \ |    |   \     /        \ |        \\     \____|    |  /  |    |   \|   |  |    |    \____   | 
  \__/\  /  /_______  / |______  /    /_______  //_______  / \______  /|______/   |____|_  /|___|  |____|    / ______| 
       \/           \/         \/             \/         \/         \/                   \/                  \/        
                                                                                                                       ''')
with open("old.txt","r") as f:
                             lines=f.readlines()
                             with open("output.txt",'w+') as nf:
                                                               for line in lines:
                                                                                line=line.split(" ")
                                                                                print("IP \t Date time \t Time Zone \t Request Type \t Path \t HTTP Protocol \t Status Code \t Packet Size \t User Agent")
                                                                                nf.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(str ((line[0])).replace('"',' '),str(line[3]).replace('"',' '),str(line[4]).replace('"',' '),str(line[5]).replace('"',' '),str(line[6]).replace('"',' '),str(line[7]).replace('"',' '),str(line[8]).replace('"',' '),str(line[9]).replace('"',' '),str(line[11:]).replace('"',' ')))
                                              
                                              
                                              #print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(str(line[0]).replace('"',' '),str(line[3]).replace('"',' '),str(line[4]).replace('"',' '),str(line[5]).replace('"',' '),str(line[6]).replace('"',' '),str(line[7]).replace('"',' '),str(line[8]).replace('"',' '),str(line[9]).replace('"',' '),str(line[11:]).replace('"',' ')))
