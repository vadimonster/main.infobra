from optparse import OptionParser
import twitterr
import instagramm
from controler import diez, data
import time

parser = OptionParser()

parser.add_option("-d", "--diez", dest="diez",
                  help="write diez for daemon", metavar="diez")
(options, args) = parser.parse_args()




def Worker(hashTag):
    if diez.check(hashTag) is None:
        diez.append(hashTag)
    i = diez.check(hashTag)
    id_hash = i.id
    for d in instagramm.Inst(hashTag):
        line = d.split('||')
        if data.check(id_hash, line[0], line[1]) is None:
            data.append(id_hash, '0', line[0], line[1])
    for d in twitterr.hasher(hashTag):
        line = d.split('||')
        if data.check(id_hash, line[0], line[1]) is None:
            data.append(id_hash, '1', line[0], line[1])



Worker(options.diez)