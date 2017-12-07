import csv
import requests
import json

fileList=["TOTAL TWEETS.csv"]
createList=["TOTAL_TWEETS_DELAYS.csv"]
fileIndex=0
for monthFile in fileList:
    testFile= open(createList[fileIndex], "w")
    writer = csv.writer(testFile, delimiter=',')
    lines= []
    with open(monthFile, "r") as f:
        reader = csv.reader(f)
        br=1000000
        i=0
        cont=0
        print("Start")
        for row in reader:
            if cont==0:

                print(row[0]+" "+row[1] +" "+row[2] +" "+row[3] +" "+row[4]+ " IS_DELAY STATION1 STATION2 STATION3 STATION4 STATION5")
                tittle=[row[0],row[1],row[2],row[3],row[4],"IS_DELAY", "STATION1", "STATION2", "STATION3", "STATION4", "STATION5"]
                writer.writerow(tittle)
                cont+=1
            else:                
                line= row
                isDelay=0
                keCollection=["delay","problem","altered","alter","delayed","delays","late","engineering","unexpected","unplanned","cancelled","fault","faults","amended","emergency"]
                reverseKey=["late Jan","late Feb","late Mar","late Apr","late May","late Apr","late Jun","late Jul","late Aug","late Sep","late Oct","late Nov","late Dec","late January","late February","late March","late April","late May","late April","late June","late July","late August","late September","late October","late November","late December"]
                stationCollection=['Waterloo','King\'s Cross St. Pancras','Victoria','Oxford Circus','Liverpool Street','London Bridge','Stratford','Bank','Monument','Canary Wharf','Paddington','Euston','Piccadilly Circus','Green Park','Bond Street','Tottenham Court Road','Leicester Square','Holborn','South Kensington','Brixton','Finsbury Park','Vauxhall','Baker Street','Hammersmith','Westminster','Moorgate','Embankment','North Greenwich','Old Street','Elephant & Castle','Camden Town','Shepherd\'s Bush','Walthamstow Central','Tower Hill','Warren Street','Highbury & Islington','Angel','Earl\'s Court','Knightsbridge','Seven Sisters','Ealing Broadway','St. Paul\'s','Chancery Lane','Southwark','Covent Garden','Notting Hill Gate','Sloane Square','Bethnal Green','Tooting Broadway','Farringdon','Barking','Mile End','Blackfriars','Wembley Park','St. James\'s Park','East Ham','Balham','Canada Water','Euston Square','Whitechapel','Leyton','Marble Arch','Gloucester Road','Aldgate East','Wimbledon','Tottenham Hale','Wood Green','High Street Kensington','Marylebone','Russell Square','Barbican','Canning Town','Pimlico','Stockwell','Leytonstone','Bermondsey','West Hampstead','Turnpike Lane','Harrow-on-the-Hill','Fulham Broadway','Upton Park','Morden','Clapham Common','Finchley Road','Archway','Manor House','Cannon Street','Willesden Green','White City','Clapham South','Queensway','Great Portland Street','Kilburn','Golders Green','Goodge Street','Blackhorse Road','Uxbridge','Kentish Town','Temple','Charing Cross','Hendon Central','Richmond','Aldgate','Tooting Bec','St. John\'s Wood','Heathrow Terminals 2 & 3','Swiss Cottage','East Finchley','Barons Court','Gants Hill','Lancaster Gate','Latimer Road','Edgware Road','Finchley Central','Clapham North','Parsons Green','Colliers Wood','Holloway Road','Bounds Green','North Acton','Belsize Park','Oval','Stepney Green','East Putney','Hyde Park Corner','Southfields','Acton Town','Colindale','Mansion House','West Brompton','Dagenham Heathway','Borough','Ladbroke Grove','Gunnersbury','Highgate','Wembley Central','Caledonian Road','Woodford','Bow Road','Southgate','Turnham Green','Queen\'s Park','Chalk Farm','Kennington','Plaistow','Newbury Park','Putney Bridge','Upminster','South Woodford','Edgware','Northolt','Kingsbury','West Kensington','Mornington Crescent','Harrow & Wealdstone','Greenford','Bayswater','South Wimbledon','Willesden Junction','Queensbury','Arnos Grove','Northwick Park','Hampstead','Burnt Oak','Warwick Avenue','Rayners Lane','Heathrow Terminal 5','Dollis Hill','Kew Gardens','East Acton','Hanger Lane','Stanmore','Westbourne Park','Northfields','Hounslow East','Hounslow Central','Bromley-by-Bow','Epping','Neasden','Hainault','Tufnell Park','Wood Lane','High Barnet','South Ealing','Shepherd\'s Bush Market','Becontree','Hounslow West','West Ham','Loughton','Kilburn Park','Maida Vale','Regent\'s Park','Preston Road','Hatton Cross','Holland Park','Pinner','Ealing Common','Ravenscourt Park','Alperton','Elm Park','Harlesden','Redbridge','Arsenal','Dagenham East','Wanstead','Eastcote','Canons Park','Oakwood','Woodside Park','Kensal Green','Upney','Stamford Brook','Snaresbrook','Royal Oak','Stonebridge Park','Brent Cross','Northwood','South Harrow','Debden','Perivale','Rickmansworth','Amersham','Boston Manor','Osterley','Chiswick Park','Heathrow Terminal 4','Totteridge & Whetstone','Buckhurst Hill','Goldhawk Road','Hornchurch','Kenton','Kensington (Olympia)','Cockfosters','Park Royal','Sudbury Town','Ruislip Manor','Sudbury Hill','North Harrow','Ruislip','Northwood Hills','Wimbledon Park','Watford','West Acton','North Wembley','Hillingdon','South Ruislip','West Finchley','West Ruislip','Barkingside','Chalfont & Latimer','West Harrow','Mill Hill East','Fairlop','Ickenham','South Kenton','Upminster Bridge','Croxley','Chesham','Chorleywood','Ruislip Gardens','Moor Park','North Ealing','Theydon Bois','Grange Hill','Chigwell','Roding Valley','Lambeth North']
                
                #LOOK FOR STATIONS IN THE TWEETS
                for keyWord in keCollection:
                    if keyWord.upper() in row[4].upper() and (reverseKey[0].upper() not in row[4].upper() and reverseKey[1].upper() not in row[4].upper() and reverseKey[2].upper() not in row[4].upper() and reverseKey[3].upper() not in row[4].upper() and reverseKey[4].upper() not in row[4].upper() and reverseKey[5].upper() not in row[4].upper() and reverseKey[6].upper() not in row[4].upper() and reverseKey[7].upper() not in row[4].upper() and reverseKey[8].upper() not in row[4].upper() and reverseKey[9].upper() not in row[4].upper() and reverseKey[10].upper() not in row[4].upper() and reverseKey[11].upper() not in row[4].upper() and reverseKey[12].upper() not in row[4].upper() and reverseKey[13].upper() not in row[4].upper() and reverseKey[14].upper() not in row[4].upper() and reverseKey[15].upper() not in row[4].upper() and reverseKey[16].upper() not in row[4].upper() and reverseKey[17].upper() not in row[4].upper() and reverseKey[18].upper() not in row[4].upper() and reverseKey[19].upper() not in row[4].upper() and reverseKey[20].upper() not in row[4].upper() and reverseKey[21].upper() not in row[4].upper() and reverseKey[22].upper() not in row[4].upper() and reverseKey[23].upper() not in row[4].upper()): 
                        isDelay=1
                        stationList=["","","","",""]
                        stCont=0
                        for station in stationCollection:
                            if station.upper() in row[4].upper():
                                stationList[stCont]=station.upper()
                                print("Found station "+stationList[stCont])
                                
                                stCont+=1
                                
                                if stCont==4:
                                    break
                        break
                #ADD COLUMNS
                line.append(isDelay)
                line.append(stationList[0])
                line.append(stationList[1])
                line.append(stationList[2])
                line.append(stationList[3])
                line.append(stationList[4])
                writer.writerow(line)        
            i+=1
            br-=1
            # STATUS REPORT
            if i%10000==0:
                print(i)
            if br==1:
                break
        
    testFile.close()
    print("FIle closed " + createList[fileIndex])
    fileIndex+=1