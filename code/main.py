from settings import *
from custom_timer import Timer

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Space Shooter")
# set_target_fps(60)

player = Player()
meteors = [Meteor() for _ in range (20)]
stars = [Star() for _ in range(20)]


while not window_should_close():
    dt = get_frame_time()
    player.update(dt)
    if meteors:
        for meteor in meteors:
            meteor.update(dt)


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
