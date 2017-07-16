
import random

#  The checkpoints will be listed here
checkpoints = ['checkpoint0',
               'checkpoint1',
               'checkpoint2',
               'checkpoint3',
               'checkpoint4',
               'checkpoint5',
               'checkpoint6',
               'checkpoint7',
               'checkpoint8',
               'checkpoint9']

#  This is the empty list of manifests to fill out, and the manifest counter
manifest = []
manifestCount = int(0)

#  As written, this will make 10 manifests with 10 jobs each
while manifestCount < 10:
    while len(manifest) < 10:
        #  These two lines will randomly select two checkpoints from the list
        pick = random.choice(checkpoints)
        drop = random.choice(checkpoints)
        while pick == drop:  #  Ensure pick and drop aren't the same
            drop = random.choice(checkpoints)
        manifest.append([pick, drop])  #  Add the job to manifest

    #  Print out manifest
    print('\nManifest #'+str(manifestCount))
    for each in manifest:
        print(each)

    manifestCount+=1  #  Completed writing one more manifest
    manifest = []  #  Clear manifest to write the next one

##    Here's a sample output:
##
##    Manifest #0
##    ['checkpoint2', 'checkpoint9']
##    ['checkpoint2', 'checkpoint6']
##    ['checkpoint5', 'checkpoint8']
##    ['checkpoint9', 'checkpoint2']
##    ['checkpoint1', 'checkpoint9']
##    ['checkpoint5', 'checkpoint8']
##    ['checkpoint3', 'checkpoint1']
##    ['checkpoint1', 'checkpoint3']
##    ['checkpoint0', 'checkpoint1']
##    ['checkpoint6', 'checkpoint8']
##
##    Manifest #1
##    ['checkpoint9', 'checkpoint4']
##    ['checkpoint6', 'checkpoint8']
##    ['checkpoint5', 'checkpoint9']
##    ['checkpoint0', 'checkpoint5']
##    ['checkpoint5', 'checkpoint9']
##    ['checkpoint9', 'checkpoint4']
##    ['checkpoint7', 'checkpoint2']
##    ['checkpoint2', 'checkpoint0']
##    ['checkpoint3', 'checkpoint1']
##    ['checkpoint3', 'checkpoint2']
##
##    Manifest #2
##    etc...
##
##    It's possible to not go to a particular checkpoint at
##    all. It's possible to have an entire manifest with 10 jobs
##    going from only one pick to only one drop. The arrangement
##    is randomized, so it's a roll of the dice!

print('\nGOODBYE, WORLD!')
