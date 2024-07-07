# Text for locations
import textwrap

def print_clean_txt(txt: str) -> str:
    '''
    
    
    '''
    txt = txt.replace("  ","")
    txt = txt[1:]
    txt = textwrap.fill(txt, 100)

    print(txt)


def hagrid_hut_txt():
    introduction = (f'''
        The pathway leading to Hagrid's hut was a journey in itself, a
        testament to the half-giant's unique blend of practicality and charm.
        It began with a winding, stony track that snaked through the shadowed
        heart of the Hogwarts woodland, dappled sunlight barely penetrating the
        thick canopy overhead. The air hung heavy with the scent of damp earth
        and decaying leaves, punctuated by the occasional pungent whiff of
        something distinctly Hagrid-esque. Clumps of vibrant mushrooms, their
        caps resembling tiny umbrellas, punctuated the path, a touch of
        whimsical magic in the otherwise austere setting. As the path deepened
        into the woods, the air grew cooler, and the trees, gnarled and ancient,
        seemed to press in closer, whispering secrets in the rustling leaves.
        The gnarled roots of ancient oaks twisted across the path, creating a
        natural obstacle course, forcing visitors to clamber over them or
        carefully step around. Finally, emerging from the dense undergrowth,
        the hut came into view, a cozy, ramshackle abode built from rough-hewn
        logs and topped with a thatched roof that seemed to sag under the weight
        of years. A plume of smoke curled from the chimney, promising warmth and
        hospitality within, welcoming any weary traveller who dared to venture
        down the path.''')
    

    hagrids_shack = (f'''
        The door creaked open, revealing a scene of utter chaos.  The lingering
        scent of something dark and sinister. You frantically search the room,
        your hands trembling, a knot of fear twisting in your gut. Where were
        his creatures? The giant spider, Aragog, had vanished from his terrarium,
        leaving behind only a single, silken thread, stretching towards the dark
        woods beyond. His beloved Blast-Ended Skrewt, usually kept in a secure
        cage, had left a trail of destruction in its wake, its sharp claws
        tearing at the wood of the floorboards. A sense of dread washes over
        you, a gnawing fear that something terrible had happened,
        something that threatened not only Hagrid's home, but the very safety of
        Hogwarts. You know, with a certainty that chills you to the bone, that
        this wasn't just a simple break-in, this was something far darker, a
        deliberate act of sabotage, aimed at Hagrid and the creatures he cared
        for.''')
    
    print_clean_txt(introduction)
    print('')
    print_clean_txt(hagrids_shack)

hagrid_hut_txt()