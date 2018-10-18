from pycarrot import Clustering, Document

x = {"searchresult": {
    "query": "seattle",
    "documents": [
        {
            "title": "City of Seattle",
            "snippet": "Official site featuring a guide to living in Seattle and information on doing business, city services, and visitor's resources.",
            "url": "http://www.seattle.gov/"
        },
        {
            "title": "Seattle's Convention and Visitors Bureau",
            "snippet": "Includes a visitors guide to Seattle, calendar of events, map, hotel reservations, and other tourism resources.",
            "url": "http://www.seeseattle.org/"
        },
        {
            "title": "The Seattle Times",
            "snippet": "Daily newspaper presenting local and worldwide news headlines, entertainment, sports, and business coverage.",
            "url": "http://www.seattletimes.com/"
        },
        {
            "title": "Seattle Weekly",
            "snippet": "In-depth news, innovative arts coverage, comprehensive entertainment listings, and searchable classifieds.",
            "url": "http://www.seattleweekly.com/"
        },
        {
            "title": "Visiting Seattle",
            "snippet": "Official guide from the City of Seattle. Includes a virtual tour, points of interest, photos, directions, and local resources like hotels and restaurants.",
            "url": "http://www.cityofseattle.net/html/visitor"
        },
        {
            "title": "Metroblogging Seattle",
            "snippet": "Hyper-local look at what's going on in the city. Regional bloggers give a perspective on daily life.",
            "url": "http://seattle.metblogs.com/"
        },
        {
            "title": "Seattle SuperSonics",
            "snippet": "Official site of the Sonics, featuring news, schedule and scores, players, stats, ticket information, and more.",
            "url": "http://www.nba.com/sonics"
        },
        {
            "title": "Seattle, Washington - Wikipedia, the free encyclopedia",
            "snippet": "Seattle, Washington. From Wikipedia, the free encyclopedia. \"Seattle\" redirects here. For the Suquamish chief, see Chief Seattle. Seattle, Washington. Nickname: \"The Emerald City\" Location. Government. Geographical characteristics. Land",
            "url": "http://en.wikipedia.org/wiki/Seattle"
        },
        {
            "title": "Seattle-Tacoma International Airport (SEA-TAC)",
            "snippet": "Maps, shuttles, tourist info, and more.",
            "url": "http://www.portseattle.org/seatac/"
        },
        {
            "title": "EarthCam: Seattle",
            "snippet": "Directory of live cams across the Seattle area.",
            "url": "http://www.earthcam.com/usa/washington/seattle"
        },
        {
            "title": "Metroblogging Seattle: Zombies!",
            "snippet": "posted by Samantha Mastridge at 12:36 PM on October 11, 2005 ... chance to, \"Walk with your un-dead brethren through the streets of Seattle in the light of day ... and play here every day, Seattle is one of over forty five ...",
            "url": "http://seattle.metblogs.com/archives/2005/10/zombies.phtml"
        },
        {
            "title": "craigslist: seattle",
            "snippet": "Online community with classifieds for housing, jobs, community events, volunteer opportunities, and for-sale items.",
            "url": "http://seattle.craigslist.org/"
        },
        {
            "title": "Seattle Post-Intelligencer",
            "snippet": "... View map * Seattle (Central) Seattle (Southeast) Seattle (Southwest) Seattle (Northwest) Seattle (Northeast) North ... Vashon Island Wallingford West Seattle Whidbey Island White Center ...",
            "url": "http://seattlepi.nwsource.com/"
        },
        {
            "title": "Seattle, Washington - Wikipedia, the free encyclopedia",
            "snippet": "Seattle, Washington From Wikipedia, the free encyclopedia \"Seattle\" redirects here. For the Suquamish chief, see Chief Seattle. Seattle, Washington Nickname: \"The Emerald City\" Location Government Geographical characteristics Land",
            "url": "http://en.wikipedia.org/wiki/Seattle,_Washington"
        },
        {
            "title": "Weather Underground: Seattle",
            "snippet": "Features current conditions, a forecast, radar images, and more.",
            "url": "http://www.wunderground.com/US/WA/Seattle.html"
        },
        {
            "title": "Seattle Mariners",
            "snippet": "Official site for the Seattle Mariners. Features up-to-date stats and results, player bios, minor league information, ticket and merchandise ordering info, player photos, and audio highlights.",
            "url": "http://www.mariners.org/"
        },
        {
            "title": "Seattlest",
            "snippet": "What's happening in Seattle, including news and events, restaurants and bars, and goings-on.",
            "url": "http://www.seattlest.com/"
        },
        {
            "title": "Seattle University",
            "snippet": "Student Diaries Personal accounts of life at SU Fun Stuff E-Postcards and desktop downloads Born to run Law school student races into SU's record books. Seattle University Seattle University is the largest independent university in the Pacific Northwest. ... Connecting the Mind To What Matters Seattle University 901 12th Avenue, P.O ...",
            "url": "http://www.seattleu.edu/"
        },
        {
            "title": "Washington State &amp;gt; Seattle Metro in the Yahoo! Directory",
            "snippet": "Yahoo! reviewed these sites and found them related to Washington State &amp;gt; Seattle Metro",
            "url": "http://seattle.yahoo.com/"
        },
        {
            "title": "Holiday Inn Express Seattle Hotels - Holiday Inn Express Hotel Reservations Seattle, WA",
            "snippet": "Holiday Inn Express Seattle Hotels - Lowest Internet Rates Guaranteed - Make Hotel Reservations for Seattle Downtown and all Seattle Hotel Locations",
            "url": "http://www.seattlehotels.holidayinnexpress.com/"
        },
        {
            "title": "Seattle Seahawks",
            "snippet": "Official site of the Seahawks. Includes schedule, news, multimedia, photos, player information, statistics, team store, tickets, and more.",
            "url": "http://www.seahawks.com/"
        },
        {
            "title": "Seattle Mariners",
            "snippet": "Official site for the Seattle Mariners. Features up-to-date stats and results, player bios, minor league information, ticket and merchandise ordering info, player photos, and audio highlights.",
            "url": "http://seattle.mariners.mlb.com/NASApp/mlb/index.jsp?c_id=sea"
        },
        {
            "title": "Seattle Seahawks - NFL.com",
            "snippet": "Offers the latest Seahawks news.",
            "url": "http://www.nfl.com/teams/news/SEA"
        },
        {
            "title": "Seattle/Tacoma - About.com",
            "snippet": "Your central resource for a wide range of information related to the Seattle/Tacoma metropolitan area. Information includes arts, entertainment, business, education, employment, government, health, lodging, media, real estate, restaurants, ... As the Seattle metro area continues to grow, many people are finding South King County a great place ...",
            "url": "http://seattle.about.com/"
        },
        {
            "title": "Current local time in Seattle - Washington - U.S.A.",
            "snippet": "Current local time in Seattle. Seattle, Washington, U.S.A. Current time. Thursday, July 6, 2006 at 6:44:14 PM PDT. UTC/GMT Offset. Standard time zone: UTC/GMT -8 hours. Daylight saving time: +1 hour. Current time zone offset: UTC/GMT -7 hours. Time zone abbreviation:",
            "url": "http://www.timeanddate.com/worldclock/city.html?n=234"
        },
        {
            "title": "Port of Seattle",
            "snippet": "Operates the airport and the marine terminals.",
            "url": "http://www.seatac.org/"
        },
        {
            "title": "Seattle SuperSonics News, Scores, Schedule, Stats - Yahoo! Sports",
            "snippet": "Comprehensive and up-to-date Seattle SuperSonics news, scores, schedule, stats and roster ... Sacramento Kings San Antonio Spurs Seattle SuperSonics Toronto Raptors Utah Jazz Washington ... first contract talks between the Seattle SuperSonics and restricted free agent forward ...",
            "url": "http://sports.yahoo.com/nba/teams/sea"
        },
        {
            "title": "Seattle Magazine",
            "snippet": "Monthly city and lifestyle magazine covering the arts, dining, personalities, businesses, and more.",
            "url": "http://seattlemag.com/"
        },
        {
            "title": "Seattle.Net",
            "snippet": "Links to all things Seattle including local business, entertainment, and community web sites.",
            "url": "http://www.seattle.net/"
        },
        {
            "title": "HistoryLink",
            "snippet": "The online encyclopedia of Washington state history. Featuring essays, timelines, photos, study aids, and more.",
            "url": "http://www.historylink.org/"
        },
        {
            "title": "Seattle International Film Festival",
            "snippet": "Held annually, from late May to early June.",
            "url": "http://www.seattlefilm.com/"
        },
        {
            "title": "Seattle Wireless",
            "snippet": "Project to develop a community wireless network.",
            "url": "http://www.seattlewireless.net/"
        },
        {
            "title": "Seattle Aquarium",
            "snippet": "Features visitor information, kid resources, education, and conservation resources.",
            "url": "http://www.seattleaquarium.org/"
        },
        {
            "title": "Seattle Travel Information | Lonely Planet Destination Guide",
            "snippet": "Lonely Planet's online guide to Seattle ... Ever wondered whether caffeine is a viable substitute for sunshine? If so, Seattle is your kind of town ... other city in the region, Seattle epitomises what people know of (and ...",
            "url": "http://www.lonelyplanet.com/worldguide/destinations/north-america/usa/seattle/"
        },
        {
            "title": "Seattle Seahawks News, Scores, Schedule, Stats - Yahoo! Sports",
            "snippet": "Comprehensive and up-to-date Seattle Seahawks news, scores, schedule, stats and roster ... Seattle Seahawks. Seattle Seahawks. 13-3-0, 1st NFC West ... Jets Oakland Raiders Philadelphia Eagles Pittsburgh Steelers San Diego Chargers Seattle Seahawks San Francisco 49ers St ...",
            "url": "http://sports.yahoo.com/nfl/teams/sea"
        },
        {
            "title": "Seattle Citysearch",
            "snippet": "Local city guide and yellow pages with business listings, reviews, events, nightlife, and other features.",
            "url": "http://seattle.citysearch.com/"
        },
        {
            "title": "Seattle on 43 Places",
            "snippet": "Advertisements. No obligation search of the entire Seattle MLS. 1000's of listings. A Complete Resource - Find Maps, Photos, Helpful Hints, Links &amp;amp; More. Moving? Get info on schools, homes, jobs, Free Relo Information! ... So Seattle, I explored with him when I went up for my 8 days ...",
            "url": "http://www.43places.com/places/view/106707"
        },
        {
            "title": "Seattle Thunderbirds",
            "snippet": "Official site features ticket information, schedule, stats, news, game recaps, and more.",
            "url": "http://www.seattle-thunderbirds.com/"
        },
        {
            "title": "Seattle, WA vacations, tourism, hotels, and attractions - Yahoo! Travel",
            "snippet": "Seattle, WA vacations: Find the best Seattle hotels, attractions, maps, pictures, weather, airport information, travel advice and more on Yahoo! Travel.",
            "url": "http://travel.yahoo.com/p-travelguide-191502031-seattle_vacations-i"
        },
        {
            "title": "Seattle Opera",
            "snippet": "Julius Caesar and The Italian Girl in Algiers round out this unbelievable season. Listen to musical highlights, view photos of scrumptious costumes, and buy your subscription online today. ... Seattle Opera, 1020 John Street, Seattle, Washington 98109 Copyright © 2005 Seattle Opera ...",
            "url": "http://www.seattleopera.org/"
        },
        {
            "title": "ESPN.com: Seattle SuperSonics Clubhouse",
            "snippet": "News, schedule, player stats, roster, and message board.",
            "url": "http://sports.espn.go.com/nba/clubhouse?team=sea"
        },
        {
            "title": "Martin Luther King Jr. - Seattle Times",
            "snippet": "Online exhibit about Dr. Martin Luther King and the civil rights movement in the U.S. Learn about the civil rights leader and his work, read his speeches, or read present-day writings about his legacy.",
            "url": "http://seattletimes.nwsource.com/mlk/"
        },
        {
            "title": "Seattle Washington Apartments For Rent | Seattle Apartment Rentals | Apartments.com",
            "snippet": "Find an Apartment in Seattle on Apartments.com, your Seattle apartment guide! ... to start your search for an apartment in Seattle. Plug in to our Seattle apartments power search and ...",
            "url": "http://seattle.apartments.com/"
        },
        {
            "title": "Seattle Wanderlust on 43 Places",
            "snippet": "Seattle Wanderlust. Goals Popular in Seattle. People in Seattle. 15 places. 42 places. 42 places. 30 places. 29 places. 4 places. 43 places. 43 places",
            "url": "http://www.43places.com/city/wanderlust/106707"
        },
        {
            "title": "Map of Seattle, WA by MapQuest",
            "snippet": "Map search for Seattle, WA provided by MapQuest. The consumer's choice for online maps and directions. ... Send Flowers in Seattle &amp;amp; Save $8. Guaranteed Same Day Delivery ... Same Day Seattle Delivery Guarantee. Family Owned For Over 90 Years ...",
            "url": "http://www.mapquest.com/maps/map.adp?country=US&amp;address=&amp;city=Seattle&amp;state=WA"
        },
        {
            "title": "SEATTLE",
            "snippet": "Seattle: Selected Resources. (http://faculty.washington.edu/krumme/readings/seattle.html) QUICK INDEX: opened in 1999, is located in a 1922 building on Seattle's historic First Hill. ... 1993, and conducted with the assistance of the City of Seattle, Port of Seattle, and King County governments ...",
            "url": "http://faculty.washington.edu/~krumme/readings/seattle.html"
        },
        {
            "title": "Seattle Center",
            "snippet": "Search Events. Today's Date. Today's Events. Event Calendar. JanFebMarAprMayJunJulAugSepOctNovDec20062007. July 2006. S. M. T. W. T. F. S. 26. 27. 28. 29. 30. 31. 1. 2. 3. 4. 5. @ Seattle Center. History Photos. HISTORY PHOTOS - ... An overhead view of Seattle Center as it looked for the 1962 World's Fair ... roof begins to take shape at the Seattle Center Coliseum, what would be the Washington State ...",
            "url": "http://www.seattlecenter.com/Information/historyphotos.asp"
        },
        {
            "title": "Houghton Mifflin College - Log In/Registration",
            "snippet": "Your browser's JavaScript support has been disabled. Please enable JavaScript to make use of this site. Registered Members. Please enter your username and password. Username: Password: This is a case-sensitive field. New Members",
            "url": "https://secure.college.hmco.com/passkeyauth/college_loginandregister.html?targeturl=%2Fhistory%2Freaderscomp%2Fnaind%2Fhtml%2Fna_035100_seattle.htm"
        },
        {
            "title": "SeattleInsider",
            "snippet": "Source for local news, weather, movie listings, and Mariners/Seahawks updates.",
            "url": "http://www.seattleinsider.com/"
        },
        {
            "title": "Flickr: Photos tagged with seattle",
            "snippet": "... NEW Explore and refine seattle photos with our brand new clustery goodness ... Real Estate MLS for Seattle, Washington. Official MLS site for greater SeaTac area ...",
            "url": "http://www.flickr.com/photos/tags/seattle"
        },
        {
            "title": "Seattle Intergroup of AA",
            "snippet": "Revealing, touching, sometimes startlingly frank stories of recovery from Seattle Intergroup's newsletter, \"the High &amp;amp; Dry\" ... The Seattle Intergroup serves the Greater Seattle area's AA members and groups by ...",
            "url": "http://www.seattleaa.org/"
        },
        {
            "title": "Seattle Loftcam",
            "snippet": "... Seattle Loftcam brought to you by Mark - Bio ... Sign up for a FREE MEMBERSHIP with Seattle Loftcam and get ...",
            "url": "http://www.loftcam.com/"
        },
        {
            "title": "Local Weather Forecast for Seattle, WA - weather.com",
            "snippet": "Local Weather Forecast for Seattle, WA. Todays weather plus a 36 hour forecast and doppler radar. ... Home &amp;gt; Local Forecast for Seattle, WA. Yesterday. Today ... Right Now for. Seattle, WA. Save this Location ...",
            "url": "http://www.weather.com/weather/local/USWA0395"
        },
        {
            "title": "Washington State &amp;gt; Seattle in the Yahoo! Directory",
            "snippet": "Yahoo! reviewed these sites and found them related to Washington State &amp;gt; Seattle ... Search: the Web | the Directory | Seattle. Washington State &amp;gt; Seattle ...",
            "url": "http://dir.yahoo.com/Regional/U_S__States/Washington/Cities/Seattle"
        },
        {
            "title": "Seattle Channel",
            "snippet": "Seattle Channel -- Connecting With Life In The City ... Send in your thoughts and questions to talkback@seattle.gov ... Arts is an annual funding program that supports out-of-school arts training for Seattle middle and high school youth ...",
            "url": "http://www.seattlechannel.org/"
        },
        {
            "title": "Seattle",
            "snippet": "Sign up for. Amtrak Cascades. travel deals! Promotions, tips &amp;amp; travel. information is available. by e-mail. Learn more... Learn more about our. privacy policy... Visit Seattle, the 'Emerald City', and walk along the sparkling waterfront or tour the gems ... heart of downtown. The Seattle Center houses Seattle Repertory Theater, Intiman Theater ...",
            "url": "http://www.amtrakcascades.com/Seattle.aspx"
        },
        {
            "title": "Home Page: Coffee and Wireless in Seattle",
            "snippet": "... Seattle is rich in good, independent coffee shops that offer free, or mostly free wireless access ... Newer and betterer map of Seattle wireless coffee shops from Brandon and the new ...",
            "url": "http://seattle.wifimug.org/"
        },
        {
            "title": "Stranger, The",
            "snippet": "Weekly urban manual.",
            "url": "http://www.thestranger.com/"
        },
        {
            "title": "Seattle, Washington - Wikimedia Commons",
            "snippet": "... Seattle is a city in the state of Washington, USA ... View of downtown Seattle from Kerry Park. Mt. Rainier appears barely visible through the haze to the right of the ...",
            "url": "http://commons.wikimedia.org/wiki/Seattle"
        },
        {
            "title": "Seattle Restaurants, Washington Restaurants",
            "snippet": "Online Restaurant Reservations in Seattle / Washington: Seattle, North of Seattle, South of Seattle, Eastside, Tacoma, Walla Walla, and Whidbey Island ... Fish House - Seattle Morton's, The Steakhouse - Seattle Nell's Oceanaire Seafood Room - Seattle Palisade Palomino - Seattle Piatti - Seattle Ponti ...",
            "url": "http://www.opentable.com/start.aspx?m=2"
        },
        {
            "title": "NWsource",
            "snippet": "Includes a city guide, traffic information, and classifieds.",
            "url": "http://www.nwsource.com/"
        },
        {
            "title": "WTO | Seattle Ministerial, 1999",
            "snippet": "The WTO is the only international body dealing with the rules of trade between nations. At its heart are the WTO agreements, the legal ground-rules for international commerce and for trade policy. ... Third WTO Ministerial Conference was held in Seattle, Washington State, US between 30 November and 3 ... to the WTO General Council in preparation for the Seattle Ministerial Conference ...",
            "url": "http://www.wto.org/english/thewto_e/minist_e/min99_e/min99_e.htm"
        },
        {
            "title": "Puget Sound Traffic Conditions",
            "snippet": "From the Washington State Department of Transportation.",
            "url": "http://www.wsdot.wa.gov/PugetSoundTraffic"
        },
        {
            "title": "Internet Seattle Guide - All the facts, All the links, All the time!",
            "snippet": "This city guide for Seattle, Washington lists Web sites that give information about the city and its neighborhoods or that are directories of its institutions and organizations. ... Look here for all the facts about the city of Seattle, Washington, and its region ... frequently encountered in my work for. Seattle Public Library, from archives to zoos, and from ...",
            "url": "http://www.halcyon.com/tmend/seattle.htm"
        },
        {
            "title": "Beautiful Seattle",
            "snippet": "News/sports, traffic/transportation, and area attractions.",
            "url": "http://www.beautifulseattle.com/"
        },
        {
            "title": "Information Seattle, The Emerald City | [ seattle.net ] |&amp;nbsp; A Guide to Seattle",
            "snippet": "www.seattle.net. Welcome to Seattle! Get all your questions answered here. Don't see what you're looking for? Let us know! How to get to Seattle",
            "url": "http://www.seattle.net/information/visit.html"
        },
        {
            "title": "American Institute of Architects",
            "snippet": "AIA Seattle, entry point to the Seattle chapter of the American Institute of Architects ... This site offers resources for AIA Seattle Members, and for anyone ... design and building professions in the greater Seattle. Puget Sound region ...",
            "url": "http://www.aiaseattle.org/"
        },
        {
            "title": "IPMS Seattle Web Page",
            "snippet": "2007 Spring Show!! Be sure to note Saturday, April 21th, 2007. This is the date for the big IPMS-SEATTLE. Spring Show!! Search the Site! Enter the words to search for: Exact Match Only ... Welcome to the Web Page of the Seattle chapter of the International Plastic Modelers Society (IPMS). We are a ...",
            "url": "http://www.ipms-seattle.org/"
        },
        {
            "title": "Seattle city guide, Washington, USA.",
            "snippet": "Seattle city guide, Washington State, USA. ... Puget Sound, Washington. Seattle. You are here: Go Northwest HOME/... Washington/... Puget Sound/... Seattle ... Seattle is surrounded by water and mountains, and the city's attraction ...",
            "url": "http://www.gonorthwest.com/Washington/seattle/Seattle.htm"
        },
        {
            "title": "Seattle, Washington (98101) Conditions &amp; Forecast : Weather Underground",
            "snippet": "... Save money with Timeshare rentals. Seattle Condos and Vacations ... 11:35 PM PDT. Seattle. 57 °F / 14 °C ...",
            "url": "http://www.wunderground.com/cgi-bin/findweather/getForecast?query=Seattle"
        },
        {
            "title": "Seattle Seahawks NFL Football Front Page",
            "snippet": "... Seattle Seahawks NFL Football Seahawks.NET is the top fan site covering the NFL Seattle Seahawks. You must enable client-side ...",
            "url": "http://seahawks.scout.com/"
        },
        {
            "title": "RefreshSeattle.org",
            "snippet": "... Refresh: Seattle. BE FRESH WITH US ... committed to enlivening the culture of Internet professionals here in Seattle. Does your heart race when you talk about ...",
            "url": "http://www.refreshseattle.org/"
        },
        {
            "title": "Puget Sound Business Journal (Seattle): Local Business News",
            "snippet": "Seattle News, BizJournals is your best source for up to date local Seattle business news and resources. ... Seattle News - Seattle Newspaper - Puget Sound Business Journal ... Louis San Antonio San Francisco San Jose Seattle South Florida Tampa Bay Washington Wichita ...",
            "url": "http://www.bizjournals.com/seattle"
        },
        {
            "title": "Seattle Weather Forecasts on Yahoo! Weather",
            "snippet": "... Weather &amp;gt; North America &amp;gt; United States &amp;gt; Washington &amp;gt; Seattle. Your weather and ... Seattle Weather. at: 12:53 pm PDT ...",
            "url": "http://weather.yahoo.com/forecast/Seattle_WA_US_f.html"
        },
        {
            "title": "#Seattle-Chat",
            "snippet": "Undernet channel for people from all over western Washington.",
            "url": "http://www.seattle-chat.com/"
        },
        {
            "title": "Seattle Center",
            "snippet": "74-acre site with such attractions as the Space Needle, KeyArena, Memorial Stadium, Seattle Opera House, Pacific Science Center, and more. Home to the 1962 World's Fair.",
            "url": "http://www.seattlecenter.com/"
        },
        {
            "title": "seattlepi.com: Seahawks",
            "snippet": "Local coverage and analysis of the Seahawks from the Seattle Post-Intelligencer.",
            "url": "http://seattlepi.nwsource.com/football"
        },
        {
            "title": "NWS radar image from Seattle/Tacoma, WA",
            "snippet": "Latest weather radar images from the National Weather Service ... National Weather Service Enhanced Radar Image. Seattle/Tacoma, WA Radar ... One Hour Precipitation. NWS Seattle/Tacoma, WA. Radar Precip Est From 06:07 PM PDT Thu Jul 06 2006 ...",
            "url": "http://radar.weather.gov/radar.php?rid=atx&amp;product=N0R&amp;overlay=11101111&amp;loop=no"
        },
        {
            "title": "ESPN.com - Seattle Seahawks",
            "snippet": "Includes Seattle Seahawks team news, scores, player stats, and roster.",
            "url": "http://sports.espn.go.com/nfl/clubhouse?team=sea"
        },
        {
            "title": "seattle-tacoma writing/editing jobs classifieds and want ads - craigslist",
            "snippet": "craigslist writing/editing jobs classifieds and want ads for seattle-tacoma",
            "url": "http://seattle.craigslist.org/wri"
        },
        {
            "title": "HistoryLink Essay: Grand jury indicts Seattle Liberation Front (SLF) leaders on April 16, 1970, for conspiracy to ... ",
            "snippet": "HistoryLink is a historical database and Website devoted to chronicling the history of Seattle and Washington State history. ... planning a February 17, 1970 demonstration in Seattle. Charges are filed against ...",
            "url": "http://www.historylink.org/essays/output.cfm?file_id=2130"
        },
        {
            "title": "Seattle Public Library",
            "snippet": "July 8, 2006 Keyword Search: BROWSE LIBRARY LOCATOR ... Point Branch South Park Branch Southwest Branch University Branch Wallingford Branch West Seattle Branch Mobile Services ... Then vote for the 2006 - 2007 Seattle Poet Populist online ...",
            "url": "http://www.spl.lib.wa.us/"
        },
        {
            "title": "Seattle travel guide - Wikitravel",
            "snippet": "Seattle, Washington, is the largest city in the Pacific Northwest. Nicknames have included: the Queen City, Jet City, and, more recently, the Emerald City.",
            "url": "http://wikitravel.org/en/Seattle"
        },
        {
            "title": "Federal Home Loan Bank of Seattle",
            "snippet": "A member of the FHLB banking system ... June 22, 2006 - Seattle Bank Changes Call Report Submission Process ... May 18, 2006 - Seattle Bank's Written Response to the Federal Housing Finance Board on its Proposed Rule: Excess ...",
            "url": "http://www.fhlbsea.com/"
        },
        {
            "title": "Bill Speidel's Underground Tour",
            "snippet": "Walking tour of Seattle's subterranean level of historic Pioneer Square.",
            "url": "http://www.undergroundtour.com/"
        },
        {
            "title": "King County",
            "snippet": "Official site.",
            "url": "http://www.metrokc.gov/"
        },
        {
            "title": "Seattle Attractions Discounts",
            "snippet": "Find information and coupons for guided historic tours of the Pacific Northwest and Seattle zoos and aquariums, museums, sports tours, cruises, ferries, trains, planes, restaurants and more. ... Whether you are planning a Washington State vacation, Seattle day trip or you're a local ready to enjoy a few hours as a Seattle tourist, this city guide will help ...",
            "url": "http://www.seattleattractions.com/"
        },
        {
            "title": "Seattle Weather Forecasts on Yahoo! Weather",
            "snippet": "... Weather &amp;gt; North America &amp;gt; United States &amp;gt; Washington &amp;gt; Seattle. Your weather and ... Seattle Weather. at: 8:53 am PDT ...",
            "url": "http://weather.yahoo.com/forecast/USWA0395_f.html"
        },
        {
            "title": "Seattle Storm",
            "snippet": "Official site.",
            "url": "http://www.wnba.com/storm"
        },
        {
            "title": "Welcome to the Greater Seattle AIS Website",
            "snippet": "AIS provides live telephone support 24 hours a day. Volunteers make this service available. For information on volunteer opportunties, contact the AIS office or email volunteer@Seattle-Al-Anon.org. ... is created and maintained by the Greater Seattle Al-Anon Information Service ...",
            "url": "http://www.seattle-al-anon.org/"
        },
        {
            "title": "Seattle - Locations - About GGU - Golden Gate University",
            "snippet": "Golden Gate University Seattle. Joshua Green Building. Suite 404. 1425 Fourth Avenue. Seattle, WA 98101. Map. Golden Gate University. GGU has been serving the Seattle area since 1974. ... click here, or for all courses in Seattle click here. In Seattle, students have the flexibility to complete their degree ...",
            "url": "http://www.ggu.edu/about/Locations/Seattle"
        },
        {
            "title": "Seattle Cossacks Stunt Drill Team",
            "snippet": "Performance Schedule: Your browser does not support inline frames or is currently configured not to display inline frames. Seattle Cossacks Active Member List. 2005-2006. Team Captain - Andy Nicholson. Team Lieutenant - Sam Chedester Jr. ... Wherever the Seattle Cossacks ride, people watch and wonder in fascination, waiting for the next man to ...",
            "url": "http://www.seattlecossacks.com/"
        },
        {
            "title": "Seattle Chamber of Commerce",
            "snippet": "Seattle Chamber of Commerce Leading Investors Find out more about our Business Services: Technology Partners Providing technical solutions to the Chamber and its members: Copyright ) 1996-2005 Greater Seattle Chamber of Commerce",
            "url": "http://www.seattlechamber.com/"
        },
        {
            "title": "Seattle Real Estate Agents, Seattle Homes For Sale, REALTORS and Seattle",
            "snippet": "Seattle Real Estate - Find Seattle Homes For Sale, REALTORS, home values and see real estate information for Seattle, Washington home buyers and sellers. ... Find Seattle homes for sale, Seattle real estate agents, and Seattle home values ...",
            "url": "http://www.homegain.com/local_real_estate/WA/seattle.html"
        },
        {
            "title": "The Seattle Times: Pacific Northwest Magazine : Our Social Disease",
            "snippet": "seattletimes.com: Northwest news and information from the Seattle Times. Daily local news, sports, arts and entertainment, and classified ads. ... Beyond the smiles, the Seattle Freeze is on. SOON AFTER SETTLING in Seattle, nearly everyone acquires a version of the people-here-are-sooo-nice story ...",
            "url": "http://seattletimes.nwsource.com/pacificnw/2005/0213/cover.html"
        },
        {
            "title": "Seattle SuperSonics | NBA Basketball at CBS SportsLine.com",
            "snippet": "Complete Seattle SuperSonics NBA Basketball Coverage at CBS SportsLine.com. ... The Seattle Post-Intelligencer says there is no truth to rumor that Seattle and Phoenix are discussing a Shawn ...",
            "url": "http://cbs.sportsline.com/nba/teams/page/SEA"
        },
        {
            "title": "Seattle Marathon",
            "snippet": "Held annually.",
            "url": "http://www.seattlemarathon.org/"
        },
        {
            "title": "Seattle hotels and cheap hotels, discount lodgings and accommodation",
            "snippet": "Seattle hotels - cheap hotel lodgings and reservations by all-hotels(tm) - Seattle discount hotels and accommodation - Instant online hotel reservations ... Seattle Hotels. 100,000 luxury, chain &amp;amp; discount hotels worldwide ... Seattle: is the biggest city in the pacific northwest of the United States ...",
            "url": "http://www.all-hotels.com/seattle-hotels.htm"
        },
        {
            "title": "Seattle Apartments - Rent an apartment in Seattle Washington at RENTNET.",
            "snippet": "Find apartments for rent in Seattle, WA - pet-friendly apartments, see floorplans, prices, photos and virtual tours - toll-free phone number - Search for the perfect Seattle apt rental at RENTNET. ... University District. Northgate-North Seattle. Green Lake-Fremont-Wallingford ... Central District-Madrona-Leschi. West Seattle-Southwest Seattle. Seattle, Tacoma. Bremerton, Vashon ...",
            "url": "http://www.rentnet.com/apartments/fyp/search/msa.jhtml?city=seattle&amp;state=wa"
        },
        {
            "title": "See Seattle Walking Tours &amp; Events",
            "snippet": "Offers history and art walks, scavenger hunts, scrambles, and road rallies.",
            "url": "http://www.see-seattle.com/"
        },
        {
            "title": "Seattle Washington Apartments For Rent | Seattle Apartment Rentals | Apartments.com",
            "snippet": "Find an Apartment in Seattle on Apartments.com, your Seattle apartment guide! ... to start your search for an apartment in Seattle. Plug in to our Seattle apartments power search and ...",
            "url": "http://seattle.apartments.com/"
        },
        {
            "title": "University of Washington",
            "snippet": "Official site of the public research university, with campuses in Seattle, Tacoma, and Bothell, Washington.",
            "url": "http://www.washington.edu/"
        },
        {
            "title": "Seattle Apartments",
            "snippet": "Free search for Seattle apartment rentals and Seattle houses for rent. Report your lease to us and get $100! ... metropolitan areas in the United States, the Greater Seattle region is home to 3.6 million people (and counting ... culture and apartments for rent, Seattle should be high on your list ...",
            "url": "http://www.rent.com/rentals/washington/seattle-tacoma-and-vicinity/seattle/"
        },
        {
            "title": "#Seattle-Chat",
            "snippet": "Undernet channel for people from all over western Washington.",
            "url": "http://www.seattle-chat.com/"
        },
        {
            "title": "W Hotels Seattle: W Seattle - Hotel Rooms at whotels.com",
            "snippet": "... a beacon in the thriving heart of Seattle, W Seattle is a premier destination for the savvy ... of Seattle's classic towers, W Seattle combines elements of the city's architectural ...",
            "url": "http://www.starwoodhotels.com/whotels/search/hotel_detail.html?propertyID=1154"
        },
        {
            "title": "King County Metro Transit",
            "snippet": "Providing bus service throughout King County. Also features information about carpools, bikes, ferries, and more.",
            "url": "http://transit.metrokc.gov/"
        },
        {
            "title": "SONICS: SCHEDULE",
            "snippet": "... NO/Oklahoma City New York Orlando Philadelphia Phoenix Portland Sacramento San Antonio Seattle Toronto Utah Washington ...",
            "url": "http://www.nba.com/sonics/schedule"
        },
        {
            "title": "Sound Transit",
            "snippet": "Central Puget Sound regional transit authority developing bus, train, and light rail systems.",
            "url": "http://www.soundtransit.org/"
        },
        {
            "title": "Seattle Mariners - CBS SportsLine.com",
            "snippet": "News, schedule, rosters, and more.",
            "url": "http://www.sportsline.com/mlb/teams/page/SEA"
        },
        {
            "title": "All Seattle",
            "snippet": "Web directory and city guide.",
            "url": "http://www.allseattle.net/"
        },
        {
            "title": "Experience Washington",
            "snippet": "Official site of the state's tourist agency providing historical, cultural, transportation, and lodging information.",
            "url": "http://www.experiencewashington.com/"
        },
        {
            "title": "Seattle News",
            "snippet": "... Local news for Seattle, WA continually updated from thousands of sources on the web ... Mayor Greg Nickels honored Seattle police officer Steve Leonard on Wednesday for his quick ...",
            "url": "http://www.topix.net/seattle"
        },
        {
            "title": "KOMO ABC 4 SEATTLE : WEATHER",
            "snippet": "FEATURES. This is a live view from a camera on our broadcast tower atop Queen Anne Hill, at the north end of downtown Seattle. The timestamp on the image uses Pacific Time.",
            "url": "http://www.komotv.com/weather/index11.html"
        },
        {
            "title": "Seattle - Restaurants, Events, Entertainment, Concerts, Tickets, Movies, Hotels &amp; Weather - AOL CityGuide",
            "snippet": "Complete guide to Seattle including weather, restaurants, hotels, events, performances, maps, tickets, entertainment, real estate, autos, apartments, shopping and more. ... Local Lists: Best of Seattle. I Live at That Burger/Pizza/Beer Joint ... Wacky Events This Month. Classic Seattle. City Attractions. Annual Festivals and Events ...",
            "url": "http://cityguide.aol.com/seattle/"
        },
        {
            "title": "Seattle Hotels - Hilton Seattle",
            "snippet": "Seattle Hotels: Hilton Seattle in Seattle WA, Seattle's one of the kind hotel.",
            "url": "http://www.seattlehilton.com/"
        },
        {
            "title": "Seattle Hotels, WA Hotel Discounts , Washington Hotels",
            "snippet": "Where2lodge.com Seattle, WA Discount Hotels, Washington",
            "url": "http://seattle-hotels.where2lodge.com/"
        },
        {
            "title": "Seattle.rb: Seattle Ruby Brigade",
            "snippet": "Ruby facts, opinions, source code, links, and stuff.",
            "url": "http://www.zenspider.com/Languages/Ruby/Seattle/"
        },
        {
            "title": "Freedom Day Committee",
            "snippet": "Dedicated to organizing and promoting the annual pride parade, march, and freedom rally.",
            "url": "http://www.seattlepride.org/"
        },
        {
            "title": "Map of 1201 1st Ave S Seattle, WA by MapQuest",
            "snippet": "Map search for 1201 1st Ave S Seattle, WA provided by MapQuest. The consumer's choice for online maps and directions.",
            "url": "http://www.mapquest.com/maps/map.adp?country=US&amp;address=1201+1st+Avenue+S&amp;city=Seattle&amp;state=WA&amp;zipcode=98134&amp;homesubmit.x=32&amp;homesubmit.y=14"
        },
        {
            "title": "Seattle Seahawks - USA Today",
            "snippet": "Seattle Seahawks... OR Raleigh-Durham Salt Lake City San Antonio Seattle St. Louis Syracuse Tampa Bay Toronto Washington ... sheet packed with a poison pill that essentially prevented Seattle from matching ...",
            "url": "http://www.usatoday.com/sports/football/nfl/seahawks/home.htm"
        },
        {
            "title": "Seattle, Washington (Cities)",
            "snippet": "... Seattle is Washington's largest city and the seat of King County ... expeditions sighted the Washington area before the close of the 1800s, Seattle was settled comparatively late ...",
            "url": "http://www.ohwy.com/wa/s/seattle.htm"
        },
        {
            "title": "CATHOLIC ENCYCLOPEDIA: Seattle",
            "snippet": "Visit New Advent for the Summa Theologica, Church Fathers, Catholic Encyclopedia and more. ... The Diocese of Seattle (Seattlensis) comprises the entire State of Washington, U.S.A ... September, 1907, to that of the Diocese of Seattle, with the new cathedral and residence of the ...",
            "url": "http://www.newadvent.org/cathen/13665a.htm"
        },
        {
            "title": "Seattle Weekender Guide",
            "snippet": "Search: from Away.com. Related Guides. Popular Cities in Washington. CLOSE TO HOME. GORP City Weekender. Trail Team Member. Day Trips/Overnighters. Long Weekends. Community Spotlight. Seattle Outdoors ... Seattle Outdoors. Share inspiration, ask advice, find a partner for your next adventure — get the 411 on the outdoors in and around Seattle ...",
            "url": "http://gorp.away.com/gorp/location/cities/seattle.htm"
        },
        {
            "title": "Tie-Seattle Homepage",
            "snippet": "... TiE-Seattle is a WA based not-for-profit organization with a mission to foster and support entrepreneurship. TiE-Seattle shares the values and philosophy of ...",
            "url": "http://www.tie-seattle.org/"
        },
        {
            "title": "Seattle Center Monorail",
            "snippet": "Commercial monorail system with service bewteen downtown and the Seattle Center.",
            "url": "http://www.seattlemonorail.com/"
        },
        {
            "title": "Seattle School District 1 schools",
            "snippet": "Enter school, city, district, or keyword. Search within",
            "url": "http://www.greatschools.net/schools.page?district=229&amp;state=WA"
        },
        {
            "title": "Seattle real estate - Search Seattle area real estate listings on Brio Realty",
            "snippet": "... Seattle real estate and homes for sale ... rate real estate mortgage loans in Seattle, King County, Washington. Seattle Real Estate, King County, WA New ...",
            "url": "http://washington.briorealty.com/nwmls-mls/indexloc/WA/King/Seattle"
        },
        {
            "title": "Seattle Art Museum",
            "snippet": "Includes information on the Seattle Art Museum, Seattle Asian Art Museum, and the Olympic Scuplture Park.",
            "url": "http://www.seattleartmuseum.org/"
        },
        {
            "title": "REI",
            "snippet": "Outdoor gear, sporting goods, and camping equipment from REI. Find guaranteed products for backpacking, hiking, climbing, cycling, skiing, or snowboarding.",
            "url": "http://www.rei.com/"
        },
        {
            "title": "Seattle Travel Guide - Hotels, Restaurants, Sightseeing in Seattle - The New York Times Travel Section",
            "snippet": "A travel guide for Seattle from The Times and Fodor's. Find events, restaurants, museums, hotels, entertainment, shopping and more. ... Going to Seattle. On the Elliott Bay Water Taxi, from West Seattle to the city ...",
            "url": "http://travel2.nytimes.com/top/features/travel/destinations/unitedstates/washington/seattle/?inline=nyt-geo"
        },
        {
            "title": "SketchFest Seattle - North America's Original Sketch Comedy Festival - Seattle Sketch Comedy",
            "snippet": "Seattle SketchFest brings together the best international sketch comedy groups for a two week festival showcasing this unique artform. ... &amp;gt;&amp;gt; 05/30/2006 &amp;gt;&amp;gt; SKETCHFEST SEATTLE 2006 APPLICATION DEADLINE EXTENSION ... with the nation's finest and funniest sketch troupes at SketchFest Seattle 2006. Thanks for applying ...",
            "url": "http://www.sketchfest.org/"
        },
        {
            "title": "See Seattle Walking Tours",
            "snippet": "Walk rating: EASY WALK to MODERATE WALK. FUN! from. Bill Boeing. to. Bill Gates. WOW! This tour is memorable and fun! You won't soon forget the magic, mystery and romance that inspired Sleepless in Seattle.",
            "url": "http://www.see-seattle.com/seeseattle.htm"
        },
        {
            "title": "Ferrycam - live web cam views of Washington State ferries, plus fares, routes, schedules and info.",
            "snippet": "... This holding area is mostly for cars waiting to get on the Seattle to Bremerton ferry ... are usually part of the holding area for the Seattle to Bainbridge Island run ...",
            "url": "http://www.ferrycam.com/ccseabrem.htm"
        },
        {
            "title": "Read all about it -- oh, you already have: Seattle is most literate city",
            "snippet": "OUR AFFILIATES. Wednesday, November 30, 2005. Read all about it -- oh, you already have: Seattle is most literate city. Frasier would be so proud. ... has the best single bars (Seattle was named the best city ... All areas Seattle (Central) Seattle (Southeast) Seattle (Southwest) Seattle (Northwest) Seattle (Northeast) North ...",
            "url": "http://seattlepi.nwsource.com/books/250264_litseattle30.html?source=mypi"
        },
        {
            "title": "Seattle Intergroup of AA",
            "snippet": "Revealing, touching, sometimes startlingly frank stories of recovery from Seattle Intergroup's newsletter, \"the High &amp;amp; Dry\" ... The Seattle Intergroup serves the Greater Seattle area's AA members and groups by ...",
            "url": "http://www.seattleaa.org/"
        },
        {
            "title": "Long Yang Club",
            "snippet": "Support group for gay Asians.",
            "url": "http://www.longyangclub.org/seattle"
        },
        {
            "title": "Internet Seattle Guide - All the facts, All the links, All the time!",
            "snippet": "This city guide for Seattle, Washington lists Web sites that give information about the city and its neighborhoods or that are directories of its institutions and organizations. ... Look here for all the facts about the city of Seattle, Washington, and its region ... frequently encountered in my work for. Seattle Public Library, from archives to zoos, and from ...",
            "url": "http://www.halcyon.com/tmend/seattle.htm"
        },
        {
            "title": "Seattle Sightseeing and Tourist Information",
            "snippet": "Tourist information for sightseeing in Seattle: Downtown Seattle sightseeing suggestions and general area tourism information for travel planning. ... Enjoy Seattle! Seattle sightseeing &amp;amp; tourist information. Seattle, the Emerald city, sits on the shores of Puget Sound surrounded ...",
            "url": "http://www.enjoyseattle.com/"
        },
        {
            "title": "Seattle PFLAG Chapter",
            "snippet": "Seattle Chapter of Parents, Families and Friends of Lesbians, Gays, Bisexuals and Transgenders. PFLAG's Mission. One day, society will accept. all its members as equals, regardless of their sexual orientation",
            "url": "http://www.seattle-pflag.org/"
        },
        {
            "title": "The Seattle Public Library: Seattle Reads",
            "snippet": "... Center for the Book at The Seattle Public Library hosts a major author for ... is invited to participate in \"Seattle Reads\" (formerly known as \"If All of Seattle Read the ...",
            "url": "http://www.spl.org/?pageID=about_leaders_washingtoncenter_seattlereads"
        },
        {
            "title": "Seattle Sounders",
            "snippet": "Official site for the team featuring latest news, scores, and player information.",
            "url": "http://www.seattlesounders.net/"
        },
        {
            "title": "Speakeasy - Speed Test",
            "snippet": "Test the speed of your internet connection with Speakeasy's speed test.",
            "url": "http://sea.speakeasy.net/"
        },
        {
            "title": "Seattle Waldorf School: Parent-Tot, Preschool, Elementary, Middle School",
            "snippet": "Seattle, Washington, USA: Parent-Tot, Preschool, Kindergarten, Elementary, Middle School. Independent, private, developmentally based education embracing the whole child. ... secluded and wooded neighborhood in Northeast Seattle, the Seattle Waldorf School offers its students an ... The Seattle Waldorf School is a member of the Association of Waldorf ...",
            "url": "http://www.seattlewaldorf.org/"
        },
        {
            "title": "Women in Film/Seattle",
            "snippet": "Nonprofit organization composed of professional women committed to working with integrity in the art and business of film.",
            "url": "http://www.womeninfilm-seattle.org/"
        },
        {
            "title": "Seattle Bubble",
            "snippet": "... News and discussion about the real estate / housing bubble, specifically as it pertains to the Seattle area ... claim we've reached that point yet in Seattle. The market is clearly not ...",
            "url": "http://seattlebubble.blogspot.com/"
        },
        {
            "title": "Slow Food Seattle",
            "snippet": "... Slow Food Seattle. Celebrating Taste, Tradition, Artisanship and Sustainability ... We are the local Seattle convivium of Slow Food USA, a national non-profit educational organization ...",
            "url": "http://www.slowfoodseattle.org/"
        },
        {
            "title": "McNeel North America - Contact",
            "snippet": "... How to find us. Our Seattle office is on the north side of Lake Union just off Stone ... support offices and affiliates in Seattle, Miami, Buenos Aires, Barcelona, Rome, Tokyo ...",
            "url": "http://www.en.na.mcneel.com/contact.htm"
        },
        {
            "title": "Seattle, Washington - Free Encyclopedia",
            "snippet": "... Seattle is the largest city in the state of Washington, and in the northwestern United States ... Point, and the first plats for the Town of Seattle were filed in 1853 ...",
            "url": "http://www.wacklepedia.com/s/se/seattle__washington.html"
        },
        {
            "title": "Seattle City Charter",
            "snippet": "... Charter of the City of Seattle. Text as last amended by the voters ... now existing and known as The City of Seattle, shall remain and continue a body politic and ...",
            "url": "http://clerk.ci.seattle.wa.us/~public/charter.htm"
        },
        {
            "title": "Seattle Web Cams",
            "snippet": "Mosaic of changing perspectives.",
            "url": "http://www.splink.com/seattle"
        },
        {
            "title": "Seattle Web Cams",
            "snippet": "Mosaic of changing perspectives.",
            "url": "http://www.splink.com/seattle"
        },
        {
            "title": "Seattle",
            "snippet": "Seattle, Washington. reviewed by Elaine Sosa. $ A steal deal. $$ Your tummy and your wallet will smile. $$$ Yikes! But if it's on my list, it's worth it. All area codes are (206) ... you're going to make it to Pike Place Market while in Seattle (and you should), it makes sense to start your tour at the ...",
            "url": "http://www.sallys-place.com/food/dining_directory/north_america/seattle.htm"
        },
        {
            "title": "IABC Seattle Welcomes You",
            "snippet": "WHAT'S NEWS. IABC/Seattle; International Association of Business Communicators, Seattle chapter. Please feel free to contact us.",
            "url": "http://seattle.iabc.com/"
        },
        {
            "title": "Seattle",
            "snippet": "... Official Web Site. Tom Keogh's Seattle Times review ... Official Web Site. Moira Macdonald's Seattle Times review ...",
            "url": "http://www.landmarktheatres.com/Market/Seattle/SeattleInfo.htm"
        },
        {
            "title": "Seattle Sounders",
            "snippet": "Official site for the team featuring latest news, scores, and player information.",
            "url": "http://www.seattlesounders.net/"
        },
        {
            "title": "Seattle Cruises - Schedules of all Cruises from Seattle WA . Find Hotels Near the Seattle Cruise Port.",
            "snippet": "Check Rates 24 Hours A Day - Preview All Seattle Cruises and Hotels near Seattle Cruise Port. Specials: Alaska Cruise, Hawaii Cruise, Repositioning Panama Canal Cruise. ... Cruises, one port city comes to mind, SEATTLE!!! Seattle offers more cruises to the Pacific Northwest ... 18 day Hawaiin cruise from Seattle, Astoria, Hilo, Kailua-Kona, Honolulu, Kauai ...",
            "url": "http://www.cruisesfrom.com/seattle"
        },
        {
            "title": "Events &amp; Adventures",
            "snippet": "Singles club planning activities including camping, hiking, rafting, parties, dances, and dinners.",
            "url": "http://www.eventsandadventures.com/"
        },
        {
            "title": "del.icio.us/tag/seattle",
            "snippet": "All items tagged seattle view popular. related tags. Zoka Coffee Roaster and Tea Company is a Seattle artisan coffee roaster. Visit Zokacoffee.com to buy our coffees and learn more about our coffee roasting and selection process. ... We have two coffeehouses in Seattle and ship our fresh roasted coffee ...",
            "url": "http://del.icio.us/tag/seattle"
        },
        {
            "title": "Hostelling International Seattle",
            "snippet": "Includes information on group rates and links to other hostels.",
            "url": "http://www.hiseattle.org/"
        },
        {
            "title": "Skål International Seattle - Home",
            "snippet": "Skål International. Seattle. Club No. 119. Founded. March 2, 1954. Updated: 5/12/06. About Skål International. Founded in 1932 in Paris by travel managers ... View Bill Gates' hone and Seattle and Mercer Island Gold Coasts ...",
            "url": "http://www.seattleskal.org/"
        },
        {
            "title": "GoCityKids | Seattle",
            "snippet": "... ValleyNorth of SeattleNortheast of SeattleNorthgate/Lake CityQueen Anne/Seattle CenterSan Juan IslandsSeaTacSeattle Citywide ServicesSouth SeattleSouth SoundUniversity District ...",
            "url": "http://www.gocitykids.com/?area=182"
        },
        {
            "title": "Seattle - MSN Encarta",
            "snippet": "Web Search: Search Encarta. Feedback. Great books about your topic, Seattle, selected by Encarta editors. Click here. Related Items. Encarta Search. Search Encarta about Seattle. Spend less time searching and more time learning. Learn more ... Seattle, city in west central Washington State. The seat of King County, Seattle is the hub of the sprawling metropolitan region of Greater Seattle and is the largest ...",
            "url": "http://encarta.msn.com/encyclopedia_761555710/Seattle.html"
        },
        {
            "title": "The Seattle Times: Local news: Snow Storm Journal",
            "snippet": "seattletimes.com: Northwest news and information from the Seattle Times. Daily local news, sports, arts and entertainment, and classified ads.",
            "url": "http://blog.seattletimes.nwsource.com/snowstorm"
        },
        {
            "title": "Seattle Cricket Club - Home Page",
            "snippet": "... Seattle Cricket Club. the OLDEST and LARGEST cricket club in the US Pacific Northwest ... BCMCL schecule is out. Both Seattle I and Seattle II are playing Sat, April 29th. Seattle ...",
            "url": "http://www.seattlecricket.com/"
        },
        {
            "title": "KING5 Seattle News | Live Traffic",
            "snippet": "Seattle, Washington. On Air. Services. Seattle Street Cams. Seattle Surface Streets. Map and cameras provided by the City of Seattle. This text is invisible on the page, but this text is affected by the invisible item's flow.",
            "url": "http://www.king5.com/traffic/trafficcon.html?seattlestreets"
        },
        {
            "title": "WTO Ministerial Conference, Seattle 1999 - Social and Economic Policy - Global Policy Forum",
            "snippet": "The WTO Millennium Round's. Third Ministerial Conference. Seattle, USA. November 27 to December 3, 1999. External Links and Resources. Hector Mata/ Agence France Presse. WTO Watch Active Calendar of Activities in Seattle ... WTO Watch Active Calendar of Activities in Seattle. WTO Watch's web site informs on the WTO daily events in Seattle through an updated calendar of events ...",
            "url": "http://www.globalpolicy.org/socecon/bwi-wto/idxstl99.htm"
        },
        {
            "title": "LASIK Seattle - Surgeons Performing Laser Eye Surgery",
            "snippet": "Find top LASIK surgeons in the Seattle area. Read about their education, experience and LASIK techniques; e-mail them your questions. ... LASIK Seattle — Laser Eye Surgery in Seattle, Washington ... Surgeons in Seattle and the greater Seattle area who perform LASIK may also perform laser eye procedures such as PRK ...",
            "url": "http://www.allaboutvision.com/lasik-surgeons/seattle-wa.htm"
        },
        {
            "title": "seattle.indymedia.org",
            "snippet": "indymedia,imc ... seattle indymedia center. home about us donate search admin ... needed political analysis of what took place in Seattle on 24 September: http://seattle.indymedia.org/en/2005/09/248210 ...",
            "url": "http://seattle.indymedia.org/en/2005/09/248166.shtml"
        },
        {
            "title": "Men's Fitness",
            "snippet": "FREE Membership includes: • Newsletters. • Special Offers. Email Address. Seattle, WA. The Fittest City. America's Fattest Cities 2005 ... a study by the CDC, 85 percent of Seattle residents said they'd gotten at least some exercise in ... Pedestrian-friendly Seattle also offers better-than average air quality, tons of ...",
            "url": "http://www.mensfitness.com/rankings/298"
        },
        {
            "title": "CPOA-Seattle Chapter",
            "snippet": "... CPOA - Seattle Chapter. In respect for those who have gone before us and as a guide for those who follow ...",
            "url": "http://www.cpoa-seattle.org/"
        },
        {
            "title": "The Seattle Public Library: Seattle Reads",
            "snippet": "... Center for the Book at The Seattle Public Library hosts a major author for ... is invited to participate in \"Seattle Reads\" (formerly known as \"If All of Seattle Read the ...",
            "url": "http://www.spl.org/?pageID=about_leaders_washingtoncenter_seattlereads"
        },
        {
            "title": "Go Seattle Card",
            "snippet": "Provides unlimited admission to over 30 Seattle tourist attractions and tours for one price and includes a color guidebook and savings on shopping and dining.",
            "url": "http://www.goseattlecard.com/"
        },
        {
            "title": "Seattle University Athletics - Official Athletic Site",
            "snippet": "The Official Athletic Site for Seattle University, member of College Sports Online. The most comprehensive coverage of Seattle University Athletics on the internet. ... 6/30/06 ~ General Release Seattle University Names Bill Hogan Athletics Director Seattle, WA - Noting a 24-year career building ...",
            "url": "http://seattleredhawks.cstv.com/"
        },
        {
            "title": "Upcoming.org: Metros: Seattle",
            "snippet": "Sign In. Username: Password: What is Upcoming.org? ... Search Events in Seattle. Subscribe Options (Close ... All Events in Seattle. Date. Event Name ...",
            "url": "http://upcoming.org/metro/us/wa/seattle/"
        },
        {
            "title": "Seattle Behind the Scenes",
            "snippet": "Information about a number of behind-the-scenes tours that are available in Seattle, Washington. ... Sign Up Now for the Seattle / Tacoma, WA newsletter ... a native or a visitor, these tours will give you a fascinating look at the character of the Seattle metropolitan area ...",
            "url": "http://seattle.about.com/od/attractions/a/behindSEA.htm?terms=university+marketing"
        },
        {
            "title": "Seattle/ N30 1999: Reports &amp; Analysis",
            "snippet": "N30 Seattle. Protest against the 3rd WTO Ministerial. Global Action Day. November 30 1999. Contents. Reports &amp;amp; Analysis from Seattle. (Mainstream-Articles are marked red in the date) Prevues - Pretaste. Seattle-Reports. Evaluation &amp;amp; Analysis ... While the events unfolding in Seattle are historic, let us not forget that this is a global movement ...",
            "url": "http://www.nadir.org/nadir/initiativ/agp/free/seattle"
        },
        {
            "title": "Pima Medical Institute Campus in Seattle Washington WA",
            "snippet": "Pima Medical Institute will start you on your career as a dental assistant, veterinarian assistant, medical assistant or pharmacy technician. A PMI campus is located in Seattle, Washington WA. ... Why attend a Seattle school that has just introduced medical when you can choose a highly ... quick and affordable education. Our Seattle medical career college has been servicing ...",
            "url": "http://www.pmi.edu/locations/seattle.asp"
        },
        {
            "title": "Seattle City Pages on Yahoo! Local. Find Businesses, Services and Events near Seattle, WA",
            "snippet": "Yahoo! Local - Find top rated Businesses, Services and Events near Seattle, WA with Photos, Maps, Driving Directions and more. ... Weather Outlook for Seattle. Tomorrow: Partly Cloudy ... see all categories. Seattle Map. View neighborhood map ...",
            "url": "http://local.yahoo.com/?location_state=WA&amp;location_city=Seattle&amp;location_lat=47.606400&amp;location_lon=-122.330803"
        },
        {
            "title": "Local Weather Forecast for Seattle, WA (98101) - weather.com",
            "snippet": "Local Weather Forecast for Seattle, WA (98101). Todays weather plus a 36 hour forecast and doppler radar. ... Right Now for. Seattle, WA (98101) Save this Location ...",
            "url": "http://www.weather.com/weather/local/98101"
        },
        {
            "title": "Seattle - tribe.net",
            "snippet": "find it on tribe. 44,415 interest groups. featured tribe. 3,564 Seattle listings. Seattle event. 13,567 members. 701 member reviews. local favorite. \"Great Club...\" featured in. Copyright © 2006 Tribe Networks, Inc. ... 3,564 Seattle listings. Seattle event. Friday, July 7th: A very special POLYPHONIC to benefit Daniel \"Monk ...",
            "url": "http://seattle.tribe.net/local"
        },
        {
            "title": "Falun Gong In Washington",
            "snippet": "Important Links. What is Falun Gong? ... Falun Gong At 2004 29th. Seattle Chinatown Summer Festival ... Lotus Flowers Bloom at. the Seattle Chinese New Year Celebration ...",
            "url": "http://www.falungong-wa.org/"
        },
        {
            "title": "National Weather Service - NWS Seattle",
            "snippet": "Government Internet Service Home page. The starting point for official government weather forecasts, warnings, meteorological products for forecasting the weather, and information about meteorology. ... National Weather Service. Seattle Weather Forecast Office. 7600 Sandpoint Way NE. Seattle, Washington 98115-6349 ...",
            "url": "http://www.wrh.noaa.gov/sew/"
        },
        {
            "title": "Vedanta Society of Western Washington",
            "snippet": "Features the main temple and bookshop and Tapovan Retreat in Arlington.",
            "url": "http://www.vedanta-seattle.org/"
        },
        {
            "title": "Pacific Science Center - Entertainment - Seattle, WA, 98109 - Citysearch",
            "snippet": "Come to Citysearch to get information, directions, and reviews on Pacific Science Center and other yp listings in Seattle ... Select a Seattle Neighborhood Ballard Beacon Hill Bellevue/Mercer Island Belltown ... Park/Madrona Magnolia-Seattle North Seattle Pioneer Square Queen Anne Redmond Seattle-Tacoma Intl ...",
            "url": "http://seattle.citysearch.com/profile/11360478"
        },
        {
            "title": "Robert McNeel &amp; Associates - North America",
            "snippet": "... with sales and support offices and affiliates in Seattle, Miami, Barcelona, Tokyo, Taipei, Seoul, Kuala Lumpur, and ...",
            "url": "http://www.en.na.mcneel.com/"
        },
        {
            "title": "Seattle Linkup Events",
            "snippet": "Seattle Linkup is a unique social group whose fundamental basis is courtesy, consideration and accountability. After all, don't you prefer people you can truly count on? ... skills all in sub-area entire Seattle area Seattle Bellevue Renton Mercer Island Redmond Tacoma ...",
            "url": "http://seattlelinkup.com/"
        },
        {
            "title": "Seattle, Forbes.com The Best Cities For Singles",
            "snippet": "Seattle ranked 10 among The Best Cities For Singles In 2005 ... Home &amp;gt; Lists &amp;gt; Best Cities For Singles &amp;gt; Seattle. &amp;lt; Previous. Next &amp;gt; Seattle. Rank 10 (2004 Rank: 18 ...",
            "url": "http://www.forbes.com/lists/2005/3/2396.html"
        },
        {
            "title": "Seattle Space Needle",
            "snippet": "Includes information on the observation deck and restaurant located in the Seattle landmark.",
            "url": "http://www.spaceneedle.com/"
        },
        {
            "title": "Starbucks Coffee",
            "snippet": "Official site of the Starbucks Corporation.",
            "url": "http://www.starbucks.com/"
        },
        {
            "title": "SEATTLE Wedding Planning Resources",
            "snippet": "... makers to photographers and reception sites, find everything you need here to plan a Seattle or Tacoma wedding ... Q&amp;A: Seattle: A Bagpiper for Our Ceremony? Q&amp;A: Seattle: Can We Dress ...",
            "url": "http://www.theknot.com/kl_SEATTLE.shtml"
        },
        {
            "title": "Residence Inn Seattle Downtown/Lake Union: Suites and amenities for corporate travel",
            "snippet": "Residence Inn Seattle Downtown/Lake Union: Spacious suites with comfort that feels like home in Seattle. ... Free Residence Inn by Marriott in Seattle! The Residence Inn by Marriott Seattle Downtown Lake Union is located ...",
            "url": "http://marriott.com/property/propertypage/SEALU"
        },
        {
            "title": "KING 5",
            "snippet": "NBC affiliate.",
            "url": "http://www.king5.com/"
        },
        {
            "title": "Seattle Indian Restaurants, Grocery &amp; Travel Agents - Indian Restaurants in Seattle",
            "snippet": "... Seattle Indian Community Guide ... India Imports 124 1/2 Broadway Ave East, Seattle, WA 98102 Ph 206-709-7577 ...",
            "url": "http://www.seattleindia.us/"
        },
        {
            "title": "Seattle",
            "snippet": "... Seattle, also known as Sealth, was very young when George Vancouver came to Puget Sound to map the ... he was a young man Seattle inherited his father's position as chief ...",
            "url": "http://www.powersource.com/gallery/people/seattle.html"
        },
        {
            "title": "Seattle Outdoor Cinema | Home",
            "snippet": "The Seattle Outdoor Cinema is a summer long outdoor movie event that takes place in Seattle, Colorado. ... Good Old Fashioned Summer Fun in Fremont. 2006 Seattle Summer Schedule ... Copyright (c) 1997, 2006 Seattle Outdoor Cinema - All Rights Reserved ...",
            "url": "http://www.fremontoutdoormovies.com/"
        },
        {
            "title": "Seattle Gas Prices",
            "snippet": "Updated list of high and low gasoline prices throughout the city.",
            "url": "http://www.seattlegasprices.com/"
        },
        {
            "title": "NARA - Pacific Alaska Region, Seattle - Main Page",
            "snippet": "The National Archives Regional Archives facility in Seattle, Washington. ... Regional Archives in Seattle. Address, Hours, Directions ...",
            "url": "http://www.archives.gov/facilities/wa/seattle.html"
        },
        {
            "title": "KIROTV.com - WeatherCam",
            "snippet": "... Sponsored Links. Currently. Seattle, Washington. Currently: 63°F Clear. Seattle, Washington. Currently: 17°C Clear ...",
            "url": "http://www.kirotv.com/wxcam/1867908/detail.html"
        },
        {
            "title": "Intermedia.NET - Welcome to your new virtual server!",
            "snippet": "Intermedia.NET offers excellence in Web Hosting and Exchange Hosting",
            "url": "http://www.seattle.org/"
        },
        {
            "title": "MSNBC - Seattle, WA news from The Seattle Post Intelligencer Front Page",
            "snippet": "The Seattle Post Intelligencer—Seattle, WA. MORE NEWS AND OTHER FEATURES. MORE NEWS FROM The Seattle Post Intelligencer. MORE LOCAL LINKS FROM THE SEATTLE P-I. Most Popular. Most Viewed. Top Rated. Most E-mailed. MORE NEWS FROM YOUR REGION ... The Seattle Post Intelligencer—Seattle, WA. •MAKE THIS YOUR LOCAL NEWS ...",
            "url": "http://www.msnbc.msn.com/id/3084013/"
        }
    ]
}
}

a = Clustering(port=8081)

docs = [Document(title=i['title'], url=i['url'], content=i['snippet']) for i in x['searchresult']['documents']]


print(a.cluster(docs, algorithm='lingo'))