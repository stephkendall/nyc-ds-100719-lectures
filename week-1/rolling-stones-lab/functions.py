import csv

with open('data.csv') as f:
    reader = csv.DictReader(f)
    our_data = []
    for album in reader:
        our_data.append(album)

def name_search(our_data,name):
    for album in our_data:
        if album['album'] == name:
            return album

def rank_search(our_data,rank):
    for album in our_data:
        if album['number'] == str(rank):
            return album
        
def year_search(our_data,year):
    yearlist = []
    for album in our_data:
        if album['year'] == str(year):
            yearlist.append(album)
    return yearlist
        
def years_search(our_data, start, end):
    count = start
    yearslist = []
    while count <= end:
        yearslist.append(year_search(our_data,count))
        count += 1
    return yearslist

def ranks_search(our_data,start, end):
    count = start
    rankslist = []
    for rank in range(start, end):
        rankslist.append(rank_search(our_data, rank))
        
    INSTEAD OF
    
    while count <= end:
        rankslist.append(rank_search(our_data, count))
        count += 1
    return rankslist      

def all_titles(our_data):
    titlelist = []
    for album in our_data:
        titlelist.append(album['album'])
    return titlelist

def all_artists(our_data):
    artistlist = []
    for album in our_data:
        artistlist.append(album['artist'])
    return artistlist

def most_albums(our_data):
    artistcount = {}
    for artist in all_artists(our_data):
        if artist in artistcount:
            artistcount[artist] += 1
        else:
            artistcount[artist] = 1
    maxalbums = max(artistcount.values())
    artistlist = []
    for keys, values in artistcount.items():
        if values == maxalbums:
             artistlist.append(keys)
    return  artistlist

def most_wordy(our_data):
    wordcount = {}
    albumtitles = all_titles(our_data)
    title_words = []
    for album in albumtitles:
        title_words.append(album.split())
    
    all_words = []
    for lists in title_words:
        all_words.extend(lists)
    
    for word in all_words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
            
    k = list(wordcount.keys())
    v = list(wordcount.values())
    return k[v.index(max(v))]
    
def hist_decade(our_data):
    decade_dict = {}
    for album in our_data:
        decade = int(album['year'])//10
        if decade in decade_dict:
            decade_dict[decade] += 1
        else:
            decade_dict[decade] = 1
    return decade_dict


            







