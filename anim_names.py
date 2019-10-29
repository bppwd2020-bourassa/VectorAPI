import anki_vector

with anki_vector.Robot("00406214") as robot:
    print("List all animation names:")
    anim_names = robot.anim.anim_list
    for anim_name in anim_names:
        print(anim_name)
