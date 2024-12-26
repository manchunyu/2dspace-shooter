from settings import *
from custom_timer import Timer

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Space Shooter")
# set_target_fps(60)

player = Player()
meteor = Meteor()
meteors = []
def create_meteor():
    meteors.append(Meteor())
stars = [Star() for _ in range(20)]
meteor_timer = Timer(METEOR_TIMER_DURATION, True, True, create_meteor)

while not window_should_close():
    # Updates
    dt = get_frame_time()
    player.update(dt)
    meteor_timer.update()
    for meteor in meteors:
        meteor.update(dt)
        if check_collision_recs(meteor.rect, player.rect):
            close_window()

    begin_drawing()

    # Background
    clear_background(BG_COLOR)
    for star in stars:
        draw_texture_v(star.texture, star.pos, WHITE)
    draw_fps(0, 0)
    
    # Draw moving sprites
    for meteor in meteors:
        draw_texture_v(meteor.texture, meteor.pos, WHITE)
    draw_texture_v(player.texture, player.pos, WHITE)


    end_drawing()

close_window()
