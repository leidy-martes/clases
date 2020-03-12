def recite(start_verse, end_verse):
    verses = [
                ('first', 'a Partridge in a Pear Tree.'),
                ('second', 'two Turtle Doves, and '),
                ('third', 'three French Hens, '),
                ('fourth', 'four Calling Birds, '),
                ('fifth', 'five Gold Rings, '),
                ('sixth', 'six Geese-a-Laying, '),
                ('seventh', 'seven Swans-a-Swimming, '),
                ('eighth', 'eight Maids-a-Milking, '),
                ('ninth', 'nine Ladies Dancing, '),
                ('tenth', 'ten Lords-a-Leaping, '),
                ('eleventh', 'eleven Pipers Piping, '),
                ('twelfth', 'twelve Drummers Drumming, '),
            ]
    extended_verse = ""
    end_statement = ""
    full_song = []
    # print(start_verse)
    count = 1
    for i in verses:
        end_statement = i[1] + end_statement
        if count >= start_verse:
            extended_verse = "On the %s day of Christmas my true love gave to me: " % (i[0]) + end_statement
            full_song.append(extended_verse)
        if count == end_verse:
            print(full_song)
            return full_song            
        count += 1
